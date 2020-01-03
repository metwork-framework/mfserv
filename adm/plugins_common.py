#!/usr/bin/env python3

from mfext.plugins_common import get_unix_socket_name


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
