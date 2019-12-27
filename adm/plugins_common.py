#!/usr/bin/env python3

import os
import envtpl

MFMODULE_RUNTIME_HOME = os.environ['MFMODULE_RUNTIME_HOME']


def get_plugin_format_version(logger, parser):
    if not parser.has_option("general", "__version"):
        if logger is not None:
            logger.warning("Deprecated config.ini format for plugin: %s => "
                           "it's still ok for this release but it won't work "
                           "anymore with mfserv 0.11 release")
        return 0
    else:
        return int(parser.get("general", "__version"))


def get_unix_socket_name(plugin_name, app_name, worker, hot_swap_prefix=''):
    return (
        f"{MFMODULE_RUNTIME_HOME}/var/"
        f"app_{hot_swap_prefix}{plugin_name}_{app_name}_{worker}.socket"
    )


def get_unix_sockets(plugin_name, app_name, workers, hot_swap_prefix=''):
    if workers == 0:
        return []
    return [
        get_unix_socket_name(plugin_name, app_name, i + 1, hot_swap_prefix)
        for i in range(0, workers)
    ]


def get_hot_swap_prefix(hot_swap_plugin=True):
    if hot_swap_plugin is True:
        return "__hs_"
    else:
        return ""


def get_std_redirect_args(prefix, plugin_name, app=None,
                          force_one_file=False,
                          split_stdout_sterr=True):
    if not force_one_file:
        if app:
            std_prefix = \
                "%s/log/%s_%s_%s_worker$(circus.wid)" % \
                (MFMODULE_RUNTIME_HOME, prefix, plugin_name, app)
        else:
            std_prefix = \
                "%s/log/%s_%s_worker$(circus.wid)" % \
                (MFMODULE_RUNTIME_HOME, prefix, plugin_name)
    else:
        if app:
            std_prefix = "%s/log/%s_%s_%s" % \
                (MFMODULE_RUNTIME_HOME, prefix, plugin_name, app)
        else:
            std_prefix = "%s/log/%s_%s" % \
                (MFMODULE_RUNTIME_HOME, prefix, plugin_name)
    if split_stdout_sterr:
        return "-o %s.stdout -e %s.stderr" % (std_prefix, std_prefix)
    else:
        return "-o %s.log -e %s.log" % (std_prefix, std_prefix)


def get_layer_wrapper_extra_args(plugin_name, plugin_dir, app=None,
                                 apdtpp=False, aadtpp=False):
    layer_wrapper_extra_args = plugin_name
    if not apdtpp:
        layer_wrapper_extra_args = layer_wrapper_extra_args + \
            " --do-not-add-plugin-dir-to-python-path"
    if aadtpp and app:
        app_dir = os.path.join(plugin_dir, app)
        layer_wrapper_extra_args = layer_wrapper_extra_args + \
            " --add-extra-dir-to-python-path=%s" % app_dir
    return layer_wrapper_extra_args


def get_cmd_and_args(cmd_and_args, plugin_conf, app_conf):
    tmp = cmd_and_args.replace("{timeout}", str(app_conf["timeout"]))
    tmp = tmp.replace("{plugin_name}", plugin_conf["name"])
    tmp = tmp.replace("{app_name}", app_conf["name"])
    tmp = tmp.replace("{plugin_dir}", plugin_conf["dir"])
    tmp = tmp.replace("{debug_extra_options}", app_conf["debug_extra_options"])
    unix_socket = get_unix_socket_name(plugin_conf["name"], app_conf["name"],
                                       "$(circus.wid)",
                                       plugin_conf["hot_swap_prefix"])
    tmp = tmp.replace("{unix_socket_path}", unix_socket)
    fof = (app_conf["numprocesses"] == "1")
    std_redirect_extra_args = \
        get_std_redirect_args("app", plugin_conf['name'], app_conf['name'],
                              force_one_file=fof)
    layer_wrapper_extra_args = get_layer_wrapper_extra_args(
        plugin_conf['name'], plugin_conf['dir'], app_conf['name'],
        apdtpp=app_conf['add_plugin_dir_to_python_path'],
        aadtpp=app_conf['add_app_dir_to_python_path'])
    tmp = "signal_wrapper.py --timeout=%i --signal=%i " \
        "--timeout-after-signal=%i --socket-up-after=%i %s -- %s" % (
            app_conf["timeout"], app_conf["smart_stop_signal"],
            app_conf["smart_stop_delay"], app_conf["smart_start_delay"],
            unix_socket, tmp)
    return (
        f"{std_redirect_extra_args} -- plugin_wrapper "
        f"{layer_wrapper_extra_args} -- {tmp}"
    )


def get_workers(logger, parser, section):
    workers = 0
    if parser.has_option(section, "numprocesses"):
        workers = \
            int(envtpl.render_string(parser.get(section, "numprocesses"),
                                     keep_multi_blank_lines=False))
    if workers == 0 and parser.has_option(section, "workers"):
        logger.warning("the workers option is deprecated => "
                       "use numprocesses instead")
        workers = int(envtpl.render_string(parser.get(section, "workers"),
                                           keep_multi_blank_lines=False))
    return workers
