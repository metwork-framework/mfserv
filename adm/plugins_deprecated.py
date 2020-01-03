#!/usr/bin/env python3

from mfext.plugins_common import get_log_proxy_args, \
    get_layer_wrapper_extra_args
from mfserv.plugins_common import get_unix_socket_name


def is_typ_valid(typ):
    return typ in ["python3_sync", "python2_sync", "aiohttp", "static", "node",
                   "empty"]


def typ_to_cmd_args(typ, plugin_conf, app_conf):
    log_proxy_args = \
        get_log_proxy_args("app", plugin_conf['name'], app_conf['name'],
                           app_conf["split_stdout_stderr"],
                           app_conf["split_multiple_workers"],
                           app_conf["numprocesses"])
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
                log_proxy_args,
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
            "--timeout %i %s %s" % (log_proxy_args,
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
                log_proxy_args, layer_wrapper_extra_args,
                app_conf['timeout'], bind, app_conf['node_opts'], node_server,
                bind, app_conf['timeout'])
    else:
        raise Exception("unknown type: %s", typ)
