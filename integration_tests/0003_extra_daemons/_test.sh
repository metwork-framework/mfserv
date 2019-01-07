#!/bin/bash

plugins.uninstall foobar >/dev/null 2>&1

set -x
set -e

mfserv.start

rm -f "${MODULE_RUNTIME_HOME}/log/extra_daemon_foo_plugin_foobar.log"

cd foobar
make develop

sleep 5
cat "${MODULE_RUNTIME_HOME}/tmp/config_auto/circus.ini"
cat "${MODULE_RUNTIME_HOME}/tmp/config_auto/nginx.conf"
_circusctl --endpoint "${MFSERV_CIRCUS_ENDPOINT}" --timeout=10 status

timeout 10s wget -O toto "http://127.0.0.1:${MFSERV_NGINX_PORT}/foobar"
N=$(cat toto |grep -c Hello)
if test "${N}" -ne 1; then
    echo "bad output"
    cat toto
fi
circus_status_watcher.sh extra_daemon_foo_for_plugin_foobar
N=$(cat "${MODULE_RUNTIME_HOME}/log/extra_daemon_foo_plugin_foobar.log" |grep -c foobar)
if test "${N}" -ne 1; then
    echo "bad log"
    cat "${MODULE_RUNTIME_HOME}/log/extra_daemon_foo_plugin_foobar.log"
fi

plugins.uninstall foobar >/dev/null 2>&1
mfserv.stop
