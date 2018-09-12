#!/bin/bash

set -x
set -e

MODULE=$1
BRANCH_NAME=$2
BUILD_ID=$3

cd /home/${MODULE}/src
if test "${MODULE}" = "mfext"; then
  ./bootstrap.sh /opt/metwork-${MODULE}-${BRANCH_NAME}
  pwd
  ls .
  ls adm
  cat adm/root.mk
elif test "${MODULE}" = "mfcom"; then
  ./bootstrap.sh /opt/metwork-${MODULE}-${BRANCH_NAME} $(readlink -f /opt/metwork-mfext)
else
  ./bootstrap.sh /opt/metwork-${MODULE}-${BRANCH_NAME} $(readlink -f /opt/metwork-mfcom)
fi
export RELEASE_BUILD=${BUILD_ID}
export MODULE_LOWERCASE=${MODULE}
make
make doc
make archive
make test
make _coverage
make rpm
