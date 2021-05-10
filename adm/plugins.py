#!/usr/bin/env python3

import os
import jinja2
import glob
import hashlib
import collections
from mfplugin.configuration import Configuration
from mfplugin.app import App
from mfplugin.utils import NON_REQUIRED_BOOLEAN, NON_REQUIRED_INTEGER, \
    NON_REQUIRED_STRING_DEFAULT_EMPTY, NON_REQUIRED_STRING, \
    NON_REQUIRED_BOOLEAN_DEFAULT_FALSE, get_current_envs, BadPlugin, \
    NON_REQUIRED_BOOLEAN_DEFAULT_TRUE

HOT_SWAP_PREFIX = "__hs_"
MFMODULE_RUNTIME_HOME = os.environ.get("MFMODULE_RUNTIME_HOME", "/unknown")
HOSTNAME = os.environ.get('MFHOSTNAME', 'unknown')
HOSTNAME_FULL = os.environ.get('MFHOSTNAME_FULL', 'unknown')
MFSERV_NGINX_TIMEOUT = int(os.environ['MFSERV_NGINX_TIMEOUT'])


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


def coerce_timeout(value):
    try:
        if int(value) <= 0:
            return MFSERV_NGINX_TIMEOUT
    except Exception:
        return MFSERV_NGINX_TIMEOUT
    return int(value)


EXTRA_NGINX_FRAGMENT = {
    **NON_REQUIRED_STRING,
    "check_with": extra_nginx_check
}
MFSERV_SCHEMA_OVERRIDE = {
    "internal": {
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
            },
            "_add_plugin_dir_to_lua_path": {
                **NON_REQUIRED_BOOLEAN_DEFAULT_TRUE
            }
        }
    },
    "app_*": {
        "schema": {
            "smart_stop_signal": {**NON_REQUIRED_INTEGER, "default": 15},
            "smart_stop_delay": {**NON_REQUIRED_INTEGER, "default": 3},
            "smart_start_delay": {**NON_REQUIRED_INTEGER, "default": 3},
            "timeout": {
                **NON_REQUIRED_INTEGER,
                "default": MFSERV_NGINX_TIMEOUT,
                "coerce": coerce_timeout
            },
            "_debug_extra_options": {**NON_REQUIRED_STRING_DEFAULT_EMPTY},
            "_prefix_based_routing": {**NON_REQUIRED_BOOLEAN, "default": True},
            "_virtualdomain_based_routing": {
                **NON_REQUIRED_BOOLEAN,
                "default": False
            },
            "virtualdomain_based_routing_extra_vhosts": {
                **NON_REQUIRED_STRING_DEFAULT_EMPTY
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
            "prefix_based_routing_extra_routes": {
                **NON_REQUIRED_STRING_DEFAULT_EMPTY,
                "check_with": extra_routes_check
            },
            "_extra_nginx_conf_filename": {**EXTRA_NGINX_FRAGMENT},
            "_extra_nginx_conf_static_filename": {**EXTRA_NGINX_FRAGMENT},
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
    def __init__(self, *args, **kwargs):
        Configuration.__init__(self, *args, **kwargs)
        self.jinja2_env = jinja2.Environment(
            extensions=[
                "jinja2_shell_extension.ShellExtension",
                "jinja2_getenv_extension.GetenvExtension",
                "jinja2_fnmatch_extension.FnMatchExtension",
            ],
            undefined=jinja2.StrictUndefined,
        )

    def get_schema(self):
        schema = Configuration.get_schema(self)
        dict_merge(schema, MFSERV_SCHEMA_OVERRIDE)
        return schema

    def after_load(self):
        # Let's evaluate jinja2 in nginx strings
        sections = ["general"]
        sections = sections + [x for x in self._doc.keys()
                               if x.startswith('app_')]
        context = {x: y for x, y in os.environ.items() if x.startswith("MF")}
        context.update(
            self.get_configuration_env_dict(ignore_keys_starting_with='_')
        )
        context.update(get_current_envs(self.plugin_name, self.plugin_home))
        for section in sections:
            for option in ('_extra_nginx_http_conf_string',
                           '_extra_nginx_server_conf_string',
                           '_extra_nginx_conf_string',
                           '_extra_nginx_conf_static_string',
                           '_extra_nginx_init_worker_by_lua_block_string'):
                if option in self._doc[section]:
                    try:
                        template = self.jinja2_env.from_string(
                            self._doc[section][option]
                        )
                        self._doc[section][option] = template.render(**context)
                    except Exception as e:
                        raise BadPlugin("problem during jinja2 eval of "
                                        "[%s]/%s with context: %s" %
                                        (section, option, context),
                                        original_exception=e)
        self._doc['general']['_lua_package_path'] = ''
        if self.add_plugin_dir_to_lua_path:
            if len(glob.glob(os.path.join(self.plugin_home, '*.lua'))) > 0:
                self._doc['general']['_lua_package_path'] = \
                    os.path.join(self.plugin_home, '?.lua')

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
        app_sections = [x for x in validated_document.keys()
                        if x.startswith('app_')]
        for section in app_sections:
            app_name = section.replace('app_', '', 1)
            validated_document[section]['_workdir'] = \
                os.path.join(self.plugin_home, app_name)
            virtualdomains = set()
            tmp = validated_document[section].get(
                'virtualdomain_based_routing_extra_vhosts', ''
            )
            for x in tmp.split(','):
                if x.strip() not in ("", "null"):
                    virtualdomains.add(x.strip())
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
    def add_plugin_dir_to_lua_path(self):
        self.load()
        key = "_add_plugin_dir_to_lua_path"
        if key in self._doc['general']:
            return self._doc['general'][key]
        return True

    @property
    def disable_nginx_conf(self):
        self.load()
        if 'internal' in self._doc:
            return self._doc['internal']['disable_nginx_conf']
        return False

    @property
    def lua_package_path(self):
        self.load()
        return self._doc['general']['_lua_package_path']


class MfservApp(App):

    def __init__(self, plugin_home, plugin_name, name, doc_fragment,
                 custom_fragment):
        App.__init__(self, plugin_home, plugin_name, name, doc_fragment,
                     custom_fragment)
        self.hot_swap_prefix = ""
        self.hot_swap_home = ""
        self.alias = "no"
        self.prefix = "/%s/%s" % (plugin_name, name)
        if self.numprocesses > 0 and self.debug:
            # we force numprocesses to 1 in debug mode
            self._doc_fragment['numprocesses'] = 1
        if self.max_age > 0 and self.debug:
            # we force max_age to 0 in debug mode
            self._doc_fragment['max_age'] = 0
        # we force graceful timeout with a value > timeout
        # because we don't want circus to sigkill signal_wrapper
        # (it can lead to process leaks)
        self._doc_fragment["graceful_timeout"] = \
            self.timeout + self._doc_fragment["smart_stop_delay"] + 10

    def duplicate(self, new_name=None):
        new_app = App.duplicate(self, new_name=new_name)
        new_app.hot_swap_prefix = self.hot_swap_prefix
        new_app.hot_swap_home = self.hot_swap_home
        new_app.alias = self.alias
        new_app.prefix = self.prefix
        return new_app

    def _get_unix_socket_name(self, worker):
        return (
            f"{MFMODULE_RUNTIME_HOME}/var/"
            f"app_{self.hot_swap_prefix}{self.plugin_name}_{self.name}_"
            f"{worker}.socket"
        )

    @property
    def cmd_and_args(self):
        old = self._doc_fragment['_cmd_and_args']
        unix_socket = self._get_unix_socket_name("$(circus.wid)")
        new = "signal_wrapper.py --timeout=%i --signal=%i " \
            "--timeout-after-signal=%i --socket-up-after=%i %s -- %s" % \
            (self.timeout, self.smart_stop_signal, self.smart_stop_delay,
                self.smart_start_delay, unix_socket, old)
        new = new.replace('{unix_socket_path}', unix_socket)
        new = new.replace('{timeout}', str(self.timeout))
        if self.debug:
            new = new.replace('{debug_extra_options}',
                              str(self.debug_extra_options))
        else:
            new = new.replace('{debug_extra_options}', '')
        return new

    @property
    def hash(self):
        tmp = "%s%s/%s" % (self.hot_swap_prefix, self.plugin_name, self.name)
        return hashlib.md5(tmp.encode('utf8')).hexdigest()

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
        return self._doc_fragment['timeout']

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
    def virtualdomain_based_routing_extra_vhosts(self):
        tmp = self._doc_fragment['virtualdomain_based_routing_extra_vhosts']
        return [
            x.strip() for x in tmp.split(',') if x.strip() not in ("", "null")
        ]

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
        return self._doc_fragment['prefix_based_routing_extra_routes']

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
