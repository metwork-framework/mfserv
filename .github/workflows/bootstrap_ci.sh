#!/bin/bash

#set -eu
set -x

#We keep the names DRONE_* with github_actions because they are used by guess_version.sh
export DRONE_BRANCH=${BRANCH}
export DRONE_TAG=${TAG}
export DRONE=true


    

cd /src

mkdir -p /opt/metwork-mfserv-${TARGET_DIR}
./bootstrap.sh /opt/metwork-mfserv-${TARGET_DIR} /opt/metwork-mfext-${DEP_DIR}

cat adm/root.mk
env | sort
