#!/usr/bin/env python3

import os

MFMODULE_RUNTIME_HOME = os.environ['MFMODULE_RUNTIME_HOME']


def get_plugin_format_version(logger, parser):
    if not parser.has_option("general", "__version"):
        # if logger is not None:
        #    logger.warning("Deprecated config.ini format for plugin: %s => "
        #                   "it's still ok for this release but it won't work "
        #                   "anymore with mfserv 0.11 release")
        return 0
    else:
        return int(parser.get("general", "__version"))


def get_unix_socket_name(plugin_name, app_name, worker, hot_swap_prefix=''):
    return (
        f"{MFMODULE_RUNTIME_HOME}/var/"
        f"plugin_{hot_swap_prefix}{plugin_name}_{app_name}_{worker}.socket"
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
