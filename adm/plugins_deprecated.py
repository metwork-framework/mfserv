#!/usr/bin/env python3

import os
from mfserv.plugins_common import get_unix_socket_name, \
    get_std_redirect_args, get_layer_wrapper_extra_args

MFMODULE_RUNTIME_HOME = os.environ["MFMODULE_RUNTIME_HOME"]
DEPRECATED_IGNORED_GENERAL_OPTIONS = ["extra_nginx_conf_filename", "name"]
DEPRECATED_IGNORED_APP_OPTIONS = ["proxy_timeout"]
DEPRECATED_GENERAL_OPTIONS = ["redis_service"]
DEPRECATED_APP_OPTIONS = []


def test_deprecated_options(logger, parser, section=None):
    if section is None:
        ignored_options = DEPRECATED_IGNORED_GENERAL_OPTIONS
        options = DEPRECATED_GENERAL_OPTIONS
        section = "general"
    else:
        ignored_options = DEPRECATED_IGNORED_APP_OPTIONS
        options = DEPRECATED_APP_OPTIONS
    for option in ignored_options:
        if parser.has_option(section, option):
            logger.warning(
                "%s option in [%s] section is DEPRECATED => ignoring" %
                (option, section))
    for option in ignored_options:
        if parser.has_option(section, option):
            logger.warning(
                "%s option in [%s] section is DEPRECATED => ignoring" %
                (option, section))
    for option in options:
        if parser.has_option(section, option):
            logger.warning(
                "%s option in [%s] section is DEPRECATED => "
                "it will be removed in next release" %
                (option, section))


def is_typ_valid(typ):
    return typ in ["python3_sync", "python2_sync", "aiohttp", "static", "node",
                   "empty"]


def typ_to_cmd_args(typ, plugin_conf, app_conf):
    fof = (app_conf["numprocesses"] == "1")
    std_redirect_extra_args = \
        get_std_redirect_args("app", plugin_conf['name'], app_conf['name'],
                              force_one_file=fof)
    bind = get_unix_socket_name(plugin_conf['name'], app_conf['name'],
                                "$(circus.wid)",
                                plugin_conf["hot_swap_prefix"])
    if typ == "aiohttp":
        layer_wrapper_extra_args = get_layer_wrapper_extra_args(
            plugin_conf['name'], plugin_conf['dir'],
            app_conf['name'],
            apdtpp=app_conf["add_plugin_dir_to_python_path"],
            aadtpp=app_conf["add_app_dir_to_python_path"]
        )
        return "%s -- plugin_wrapper %s -- signal_wrapper.py " \
            "--timeout=%i %s -- python %s %s %i" % (
                std_redirect_extra_args,
                layer_wrapper_extra_args, app_conf["timeout"], bind,
                app_conf["main_arg"], bind, app_conf["timeout"])
    elif typ in ['python3_sync', 'python2_sync']:
        layer_wrapper_extra_args = get_layer_wrapper_extra_args(
            plugin_conf['name'], plugin_conf['dir'], app_conf['name'],
            apdtpp=app_conf['add_plugin_dir_to_python_path'],
            aadtpp=app_conf['add_app_dir_to_python_path'])
        debug_arg = ""
        if app_conf['debug']:
            debug_arg = "--debug --debug-evalex"
        return "%s -- plugin_wrapper %s -- bjoern_wrapper.py %s " \
            "--timeout %i %s %s" % (std_redirect_extra_args,
                                    layer_wrapper_extra_args, debug_arg,
                                    app_conf['timeout'], app_conf['main_arg'],
                                    bind)
    elif typ == "node":
        layer_wrapper_extra_args = get_layer_wrapper_extra_args(
            plugin_conf['name'], plugin_conf['dir'])
        node_server = "%s/%s/%s" % (plugin_conf['dir'], app_conf['name'],
                                    app_conf['main_arg'])
        return "%s -- plugin_wrapper %s -- signal_wrapper.py " \
            "--timeout=%i %s -- node %s %s %s %i" % (
                std_redirect_extra_args, layer_wrapper_extra_args,
                app_conf['timeout'], bind, app_conf['node_opts'], node_server,
                bind, app_conf['timeout'])
    else:
        raise Exception("unknown type: %s", typ)
