#!/usr/bin/env python3

import os
import glob
import hashlib
import collections
from mfplugin.configuration import Configuration
from mfplugin.app import App
from mfplugin.utils import NON_REQUIRED_BOOLEAN, NON_REQUIRED_INTEGER, \
    NON_REQUIRED_STRING_DEFAULT_EMPTY, NON_REQUIRED_STRING, \
    NON_REQUIRED_BOOLEAN_DEFAULT_FALSE

HOT_SWAP_PREFIX = "__hs_"
MFMODULE_RUNTIME_HOME = os.environ.get("MFMODULE_RUNTIME_HOME", "/unknown")
HOSTNAME = os.environ.get('MFCOM_HOSTNAME', 'unknown')
HOSTNAME_FULL = os.environ.get('MFCOM_HOSTNAME_FULL', 'unknown')


def extra_nginx_check(field, value, error):
    if value is not None and value != "null" and value != "":
        path = os.path.join(os.environ["MFSERV_CURRENT_PLUGIN_DIR"], value)
        if not os.path.isfile(path):
            error(field, "must exist as a relative path under plugin home "
                  "(%s is not a file)" % path)


def extra_routes_check(field, value, error):
    if value is not None and value != "null" and value != "":
        tmp = value.split(";")
        for route in tmp:
            r = route.strip()
            if r == "/":
                continue
            if not r.startswith('/'):
                error(field, "all routes must start by /")
            if r.endswith('/'):
                error(field, "all routes must not end by / "
                      "(but '/' is allowed)")


EXTRA_NGINX_FRAGMENT = {
    **NON_REQUIRED_STRING,
    "check_with": extra_nginx_check
}
MFSERV_SCHEMA_OVERRIDE = {
    "__advanced": {
        "required": False,
        "type": "dict",
        "schema": {
            "disable_nginx_conf": {
                **NON_REQUIRED_BOOLEAN_DEFAULT_FALSE
            }
        }
    },
    "general": {
        "schema": {
            "_extra_nginx_http_conf_filename": {**EXTRA_NGINX_FRAGMENT},
            "_extra_nginx_server_conf_filename": {**EXTRA_NGINX_FRAGMENT},
            "_extra_nginx_init_worker_by_lua_block_filename": {
                **EXTRA_NGINX_FRAGMENT
            }
        }
    },
    "app_*": {
        "schema": {
            "smart_stop_signal": {**NON_REQUIRED_INTEGER, "default": 15},
            "smart_stop_delay": {**NON_REQUIRED_INTEGER, "default": 3},
            "smart_start_delay": {**NON_REQUIRED_INTEGER, "default": 3},
            "timeout": {**NON_REQUIRED_INTEGER, "default": 0},
            "_debug_extra_options": {**NON_REQUIRED_STRING_DEFAULT_EMPTY},
            "_prefix_based_routing": {**NON_REQUIRED_BOOLEAN, "default": True},
            "_virtualdomain_based_routing": {
                **NON_REQUIRED_BOOLEAN,
                "default": False
            },
            "_static_routing": {**NON_REQUIRED_BOOLEAN, "default": True},
            "_static_url_prefix": {
                **NON_REQUIRED_STRING,
                "default": "/static"
            },
            "_static_directory": {
                **NON_REQUIRED_STRING,
                "default": "/static"
            },
            "_prefix_based_routing_extra_routes": {
                **NON_REQUIRED_STRING_DEFAULT_EMPTY,
                "check_with": extra_routes_check
            },
            "_extra_nginx_conf_filename": {**EXTRA_NGINX_FRAGMENT},
            "_extra_nginx_conf_static_filename": {**EXTRA_NGINX_FRAGMENT},
            "_add_plugin_dir_to_python_path": {
                **NON_REQUIRED_BOOLEAN,
                "default": True
            },
            "_http_test_endpoint": {**NON_REQUIRED_STRING_DEFAULT_EMPTY},
            "_http_test_expected_status_code": {
                **NON_REQUIRED_INTEGER,
                "default": 200
            },
            "_http_test_expected_body": {
                **NON_REQUIRED_STRING,
                "default": "OK"
            },
            "_http_test_timeout": {
                **NON_REQUIRED_INTEGER,
                "default": 10
            }
        }
    }
}


# See https://gist.github.com/angstwad/bf22d1822c38a92ec0a9
def dict_merge(dct, merge_dct):
    for k, v in merge_dct.items():
        if (k in dct and isinstance(dct[k], dict)
                and isinstance(merge_dct[k], collections.Mapping)):
            dict_merge(dct[k], merge_dct[k])
        else:
            dct[k] = merge_dct[k]


class MfservConfiguration(Configuration):

    def get_schema(self):
        schema = Configuration.get_schema(self)
        dict_merge(schema, MFSERV_SCHEMA_OVERRIDE)
        return schema

    def get_final_document(self, validated_document):
        sections = ["general"]
        sections = sections + [x for x in validated_document.keys()
                               if x.startswith('app_')]
        for section in sections:
            for option in ('_extra_nginx_http_conf_filename',
                           '_extra_nginx_server_conf_filename',
                           '_extra_nginx_conf_filename',
                           '_extra_nginx_conf_static_filename',
                           '_extra_nginx_init_worker_by_lua_block_filename'):
                if option in validated_document[section]:
                    val = validated_document[section][option]
                    path = os.path.join(
                        os.environ["MFSERV_CURRENT_PLUGIN_DIR"], val)
                    if validated_document[section][option] != "":
                        with open(path, 'r') as f:
                            content = f.read()
                    else:
                        content = ""
                    new_option = option.replace('_filename', '_string')
                    validated_document[section][new_option] = content

        if len(glob.glob(os.path.join(self.plugin_home, '*.lua'))) > 0:
            validated_document['general']['_lua_package_path'] = \
                os.path.join(self.plugin_home, '?.lua')
        else:
            validated_document['general']['_lua_package_path'] = ''
        app_sections = [x for x in validated_document.keys()
                        if x.startswith('app_')]
        for section in app_sections:
            app_name = section.replace('app_', '', 1)
            validated_document[section]['_workdir'] = \
                os.path.join(self.plugin_home, app_name)
            virtualdomains = set()
            for host in (HOSTNAME, HOSTNAME_FULL, "localhost"):
                virtualdomains.add("%s.%s.%s" % (app_name, self.plugin_name,
                                                 host))
                if section == "app_main" or len(app_sections) == 1:
                    virtualdomains.add("%s.%s" % (self.plugin_name, host))
            validated_document[section]['_virtualdomains'] = \
                list(virtualdomains)
        return validated_document

    @property
    def extra_nginx_http_conf_filename(self):
        self.load()
        return self._doc['general']['_extra_nginx_http_conf_filename']

    @property
    def extra_nginx_server_conf_filename(self):
        self.load()
        return self._doc['general']['_extra_nginx_server_conf_filename']

    @property
    def extra_nginx_http_conf_string(self):
        self.load()
        return self._doc['general']['_extra_nginx_http_conf_string']

    @property
    def extra_nginx_server_conf_string(self):
        self.load()
        return self._doc['general']['_extra_nginx_server_conf_string']

    @property
    def extra_nginx_init_worker_by_lua_block_filename(self):
        self.load()
        return self._doc['general']['_extra_nginx_init_worker_'
                                    'by_lua_block_filename']

    @property
    def extra_nginx_init_worker_by_lua_block_string(self):
        self.load()
        return self._doc['general']['_extra_nginx_init_worker_'
                                    'by_lua_block_string']

    @property
    def disable_nginx_conf(self):
        self.load()
        if '__advanced' in self._doc:
            return self._doc['__advanced']['disable_nginx_conf']
        return False

    @property
    def lua_package_path(self):
        self.load()
        return self._doc['general']['_lua_package_path']


class MfservApp(App):

    def __init__(self, plugin_name, name, doc_fragment):
        App.__init__(self, plugin_name, name, doc_fragment)
        self.alias = "no"
        self.prefix = "/%s/%s" % (plugin_name, name)
        tmp = "%s/%s" % (plugin_name, name)
        self.hash = hashlib.md5(tmp.encode('utf8')).hexdigest()
        self.hot_swap_prefix = ""
        self.hot_swap_home = ""
        if self.numprocesses > 0 and self.debug:
            # we force numprocesses to 1 in debug mode
            self.numprocesses = 1
        if self.max_age > 0 and self.debug:
            # we force max_age to 0 in debug mode
            self.max_age = 0

    def _get_unix_socket_name(self, worker):
        return (
            f"{MFMODULE_RUNTIME_HOME}/var/"
            f"app_{self.hot_swap_prefix}{self.plugin_name}_{self.name}_"
            f"{worker}.socket"
        )

    @property
    def unix_sockets(self):
        if self.numprocesses == 0:
            return []
        return [self._get_unix_socket_name(i + 1)
                for i in range(0, self.numprocesses)]

    @property
    def virtualdomains(self):
        return self._doc_fragment['_virtualdomains']

    @property
    def smart_stop_signal(self):
        return self._doc_fragment['smart_stop_signal']

    @property
    def workdir(self):
        return self._doc_fragment['_workdir']

    @property
    def smart_stop_delay(self):
        return self._doc_fragment['smart_stop_delay']

    @property
    def smart_start_delay(self):
        return self._doc_fragment['smart_start_delay']

    @property
    def timeout(self):
        # we add 2 to kill the backend first
        return self._doc_fragment['timeout'] + 2

    @property
    def debug_extra_options(self):
        return self._doc_fragment['_debug_extra_options']

    @property
    def prefix_based_routing(self):
        return self._doc_fragment['_prefix_based_routing']

    @property
    def virtualdomain_based_routing(self):
        return self._doc_fragment['_virtualdomain_based_routing']

    @property
    def static_routing(self):
        return self._doc_fragment['_static_routing']

    @property
    def static_url_prefix(self):
        return self._doc_fragment['_static_url_prefix']

    @property
    def static_directory(self):
        return self._doc_fragment['_static_directory']

    @property
    def prefix_based_routing_extra_routes(self):
        return self._doc_fragment['_prefix_based_routing_extra_routes']

    @property
    def extra_nginx_conf_filename(self):
        return self._doc_fragment['_extra_nginx_conf_filename']

    @property
    def extra_nginx_conf_static_filename(self):
        return self._doc_fragment['_extra_nginx_conf_static_filename']

    @property
    def extra_nginx_conf_string(self):
        return self._doc_fragment['_extra_nginx_conf_string']

    @property
    def extra_nginx_conf_static_string(self):
        return self._doc_fragment['_extra_nginx_conf_static_string']

    @property
    def add_plugin_dir_to_python_path(self):
        return self._doc_fragment['_add_plugin_dir_to_python_path']

    @property
    def http_test_endpoint(self):
        return self._doc_fragment['_http_test_endpoint']

    @property
    def http_test_expected_status_code(self):
        return self._doc_fragment['_http_test_expected_status_code']

    @property
    def http_test_expected_body(self):
        return self._doc_fragment['_http_test_expected_body']

    @property
    def http_test_timeout(self):
        return self._doc_fragment['_http_test_timeout']
