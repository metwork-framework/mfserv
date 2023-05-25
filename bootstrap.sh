#!/bin/bash



set -eu

function get_abs_filename() {
    echo "$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
}

function usage() {
    echo "usage: ./bootstrap.sh INSTALL_PREFIX_DIRECTORY MFEXT_INSTALL_ROOT_DIRECTORY"
}

if test "${1:-}" = "" -o "${2:-}" = ""; then
    usage
    exit 1
fi
if test "${1:-}" = "--help"; then
    usage
    exit 0
fi

MFEXT_HOME=$(get_abs_filename "$2")
export MFEXT_HOME
if ! test -d "${MFEXT_HOME}"; then
    usage
    echo "ERROR: ${MFEXT_HOME} is not a directory"
    exit 1
fi
MFEXT_HOME=$(get_abs_filename "${MFEXT_HOME}")
export MFEXT_HOME
MFEXT_VERSION=$(cat "${MFEXT_HOME}/config/version")
export MFEXT_VERSION
MFSERV_VERSION=$("${MFEXT_HOME}/bin/guess_version.sh")
export MFSERV_VERSION
MFMODULE_VERSION=$("${MFEXT_HOME}/bin/guess_version.sh")
export MFMODULE_VERSION

MFMODULE_HOME=$(get_abs_filename "$1")
export MFMODULE_HOME
if ! test -d "${MFMODULE_HOME}"; then
    usage
    echo "ERROR: ${MFMODULE_HOME} is not a directory"
    exit 1
fi

if ! test -f "${MFEXT_HOME}/bin/guess_version.sh"; then
    echo "ERROR: configured mfext home (${MFEXT_HOME}) is not a mfext home"
    exit 1
fi

export MFMODULE=MFSERV
export MFMODULE_LOWERCASE=mfserv
SRC_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
export SRC_DIR

export MODULE_HAS_HOME_DIR=1

rm -f adm/root.mk
touch adm/root.mk

ROOT_PATH=${MFEXT_HOME}/bin:${MFEXT_HOME}/opt/core/bin:/usr/sbin:/usr/bin:/sbin:/bin
ROOT_LD_LIBRARY_PATH=""
ROOT_PKG_CONFIG_PATH=""
ROOT_LAYERAPI2_LAYERS_PATH=${MFMODULE_HOME}/opt:${MFMODULE_HOME}:${MFEXT_HOME}/opt:${MFEXT_HOME}

echo "Making adm/root.mk..."
rm -f adm/root.mk
touch adm/root.mk

echo "unexport MFMODULE_RUNTIME_HOME" >>adm/root.mk
echo "unexport MFMODULE_RUNTIME_SUFFIX" >>adm/root.mk
echo "unexport MFMODULE_RUNTIME_USER" >>adm/root.mk

echo "export MFMODULE := ${MFMODULE}" >>adm/root.mk
echo "export MFMODULE_LOWERCASE := $(echo ${MFMODULE} | tr '[:upper:]' '[:lower:]')" >>adm/root.mk
echo "export LAYERAPI2_LAYERS_PATH := ${ROOT_LAYERAPI2_LAYERS_PATH}" >>adm/root.mk
echo "export MFEXT_HOME := ${MFEXT_HOME}" >>adm/root.mk
echo "export MFEXT_VERSION := ${MFEXT_VERSION}" >>adm/root.mk
echo "export MFMODULE_HOME := ${MFMODULE_HOME}" >>adm/root.mk
echo "export MFMODULE_VERSION := ${MFSERV_VERSION}" >>adm/root.mk
echo "export SRC_DIR := ${SRC_DIR}" >>adm/root.mk
echo "ifeq (\$(FORCED_PATHS),)" >>adm/root.mk
echo "  export PATH := ${ROOT_PATH}" >>adm/root.mk
echo "  export LD_LIBRARY_PATH := ${ROOT_LD_LIBRARY_PATH}" >>adm/root.mk
echo "  export PKG_CONFIG_PATH := ${ROOT_PKG_CONFIG_PATH}" >>adm/root.mk
echo "  LAYER_ENVS:=\$(shell env |grep '^LAYERAPI2_LAYER_.*_LOADED=1\$\$' |awk -F '=' '{print \$\$1;}')" >>adm/root.mk
echo "  \$(foreach LAYER_ENV, \$(LAYER_ENVS), \$(eval unexport \$(LAYER_ENV)))" >>adm/root.mk
echo "endif" >>adm/root.mk
echo "export ${MFMODULE}_HOME := ${MFMODULE_HOME}" >>adm/root.mk
echo "export ${MFMODULE}_VERSION := ${MFSERV_VERSION}" >>adm/root.mk
if test "${MODULE_HAS_HOME_DIR:-}" = "1"; then
    echo "export MODULE_HAS_HOME_DIR := 1" >>adm/root.mk
fi
if test "${FTP_PROXY:-}" != ""; then
    echo "export FTP_PROXY:=${FTP_PROXY:-}" >>adm/root.mk
fi
if test "${http_proxy:-}" != ""; then
    echo "export http_proxy:=${http_proxy:-}" >>adm/root.mk
fi
if test "${https_proxy:-}" != ""; then
    echo "export https_proxy:=${https_proxy:-}" >>adm/root.mk
fi
if test "${HTTPS_PROXY:-}" != ""; then
    echo "export HTTPS_PROXY:=${HTTPS_PROXY:-}" >>adm/root.mk
fi
if test "${HTTP_PROXY:-}" != ""; then
    echo "export HTTP_PROXY:=${HTTP_PROXY:-}" >>adm/root.mk
fi
echo "export PYTHON3_SHORT_VERSION := 3.11" >>adm/root.mk

echo "BOOTSTRAP DONE !"
echo "MFEXT_HOME=${MFEXT_HOME}"
