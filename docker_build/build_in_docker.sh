#!/bin/bash

set -x

function usage() {
    echo "usage: build_in_docker.sh IMAGE MODULE BRANCH_NAME BUILD_ID"
    echo "example: build_in_docker.sh buildimage-mfext-centos7 mfext master 1"
}

if test "$1" = "--help" -o "$1" = "-h"; then
    usage
    exit 0
fi
if test "$1" = ""; then
    usage
    exit 1
else
    IMAGE=$1
fi
if test "$2" = ""; then
    usage
    exit 1
else
    MODULE=$2
fi
if test "$3" = ""; then
    usage
    exit 1
else
    BRANCH_NAME=$3
fi
if test "$4" = ""; then
    usage
    exit 1
else
    BUILD_ID=$4
fi
N=`echo ${IMAGE} |grep ':' |wc -l`
if test ${N} -eq 0; then
    IMAGE="${IMAGE}:${BRANCH_NAME}"
fi

CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SOURCE_ROOT=`readlink -m ${CURRENT_DIR}/..`

docker run -t -v ${SOURCE_ROOT}:/working_directory ${IMAGE} /working_directory/docker_build/_build_in_docker.sh ${MODULE} ${BRANCH_NAME} ${BUILD_ID}
