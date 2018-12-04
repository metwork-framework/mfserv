#!/bin/bash

set -eu

function get_md5() {
    cat "$1" |md5sum |awk '{print $1;}'
}

function log() {
    command log --application-name=conf_monitor "$1" "$2"
}

function handle_sigterm() {
    log INFO "SIGTERM catched => scheduling shutdown..."
    RUN=0
}

function handle_sigint() {
    log INFO "SIGINT catched => scheduling shutdown..."
    RUN=0
}

function test_status_or_exit() {
    EXIT=0
    if ! test -f "${MODULE_RUNTIME_HOME}/var/status"; then
        EXIT=1
    else
        # shellcheck disable=SC2126
        N=$(cat "${MODULE_RUNTIME_HOME}/var/status" 2>/dev/null |grep RUNNING |wc -l)
        if test "${N}" -ne 1; then
            EXIT=1
        fi
    fi
    if test "${EXIT}" = "1"; then
        log WARNING "${MODULE_RUNTIME_HOME}/var/status is not RUNNING => exit"
        exit 0
    fi
    N=$(pgrep -u "${MODULE_RUNTIME_USER}" -f "plugins\\.install" |wc -l)
    if test "${N}" -gt 0; then
        log WARNING "plugin installation in progress => exit"
        exit 0
    fi
    N=$(pgrep -u "${MODULE_RUNTIME_USER}" -f "plugins\\.uninstall" |wc -l)
    if test "${N}" -gt 0; then
        log WARNING "plugin uninstallation in progress => exit"
        exit 0
    fi
}

log INFO "started"

RUN=1
trap handle_sigterm TERM
trap handle_sigterm INT

log DEBUG "sleeping 5 seconds..."
sleep 5
test_status_or_exit

while test "${RUN}" -eq 1; do
    OLD_CIRCUS_CONF="${MODULE_RUNTIME_HOME}/tmp/config_auto/circus.ini"
    if test -f "${OLD_CIRCUS_CONF}"; then
        OLD_CIRCUS_MD5=$(get_md5 "${OLD_CIRCUS_CONF}")
        NEW_CIRCUS_CONF="${MODULE_RUNTIME_HOME}/tmp/tmp_circus_conf"
        _make_circus_conf >"${NEW_CIRCUS_CONF}"
        if test $? -ne 0; then
            log WARNING "bad return code from _make_circus_conf => exiting"
            exit 1
        fi
        NEW_CIRCUS_MD5=$(get_md5 "${NEW_CIRCUS_CONF}")
        if test "${OLD_CIRCUS_MD5}" != "${NEW_CIRCUS_MD5}"; then
            test_status_or_exit
            log INFO "circus conf changed => reload"
            mv -f "${NEW_CIRCUS_CONF}" "${OLD_CIRCUS_CONF}" >/dev/null 2>&1
            timeout 30s layer_wrapper --layers=python3_circus@mfext -- circusctl --endpoint "${MFSERV_CIRCUS_ENDPOINT}" restart >/dev/null 2>&1 || true
            sleep 3
            log INFO "exiting"
            exit 0
        fi
        rm -f "${NEW_CIRCUS_CONF}"
    fi
    OLD_NGINX_CONF="${MODULE_RUNTIME_HOME}/tmp/config_auto/nginx.conf"
    if test -f "${OLD_NGINX_CONF}"; then
        OLD_NGINX_MD5=$(get_md5 "${OLD_NGINX_CONF}")
        NEW_NGINX_CONF="${MODULE_RUNTIME_HOME}/tmp/tmp_nginx_conf"
        _make_nginx_conf >"${NEW_NGINX_CONF}"
        if test $? -ne 0; then
            log WARNING "bad return code from _make_nginx_conf => exiting"
            exit 1
        fi
        NEW_NGINX_MD5=$(get_md5 "${NEW_NGINX_CONF}")
        if test "${OLD_NGINX_MD5}" != "${NEW_NGINX_MD5}"; then
            test_status_or_exit
            log INFO "nginx conf changed => reload"
            mv -f "${NEW_NGINX_CONF}" "${OLD_NGINX_CONF}" >/dev/null 2>&1
            timeout 10s layer_wrapper --layers=python3_circus@mfext -- circusctl --endpoint "${MFSERV_CIRCUS_ENDPOINT}" signal nginx SIGHUP || true
        fi
        rm -f "${NEW_NGINX_CONF}"
    fi
    OLD_CRONTAB_CONF="${MODULE_RUNTIME_HOME}/tmp/config_auto/crontab"
    if test -f "${OLD_CRONTAB_CONF}"; then
        OLD_CRONTAB_MD5=$(get_md5 "${OLD_CRONTAB_CONF}")
        NEW_CRONTAB_CONF="${MODULE_RUNTIME_HOME}/tmp/tmp_crontab_conf"
        _make_crontab.sh >"${NEW_CRONTAB_CONF}"
        if test $? -ne 0; then
            log WARNING "bad return code from _make_crontab.sh => exiting"
            exit 1
        fi
        NEW_CRONTAB_MD5=$(get_md5 "${NEW_CRONTAB_CONF}")
        if test "${OLD_CRONTAB_MD5}" != "${NEW_CRONTAB_MD5}"; then
            test_status_or_exit
            log INFO "crontab conf changed => reload"
            mv -f "${NEW_CRONTAB_CONF}" "${OLD_CRONTAB_CONF}" >/dev/null 2>&1
            _uninstall_crontab.sh
            deploycron_file "${OLD_CRONTAB_CONF}"
        fi
        rm -f "${NEW_CRONTAB_CONF}"
    fi
    if test "${RUN}" -eq 1; then
        sleep 5
        test_status_or_exit
    fi
done

log INFO "stopped"
