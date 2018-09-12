#!/bin/bash

set -x
set -e

MODULE=$1
BRANCH_NAME=$2
BUILD_ID=$3

mkdir -p /home/${MODULE}/src
mkdir -p /opt/metwork-${MODULE}-${BRANCH_NAME}
cp -Rf /working_directory/* /home/${MODULE}/src/
cp -f /working_directory/.layerapi2* /home/${MODULE}/src/
cp -Rf /working_directory/.git* /home/${MODULE}/src/
chown -R ${MODULE}:metwork /home/${MODULE}/src
chown -R ${MODULE}:metwork /opt/metwork-${MODULE}-${BRANCH_NAME}
su --command="/home/${MODULE}/src/docker_build/__build_in_docker.sh ${MODULE} ${BRANCH_NAME} ${BUILD_ID}" - ${MODULE}
cp -f /opt/metwork-${MODULE}-${BRANCH_NAME}/*.rpm /working_directory/
cp -f /opt/metwork-${MODULE}-${BRANCH_NAME}/*.tar.bz2 /working_directory/
rm -Rf /working_directory/html_doc
rm -Rf /working_directory/html_coverage
if test -d /opt/metwork-${MODULE}-${BRANCH_NAME}/html_doc; then
  cp -Rf /opt/metwork-${MODULE}-${BRANCH_NAME}/html_doc /working_directory/
else
  mkdir /working_directory/html_doc
  echo "<html><head></head><body><p>nothing yet</p></body></html>" >/working_directory/html_doc/index.html
fi
if test -d /opt/metwork-${MODULE}-${BRANCH_NAME}/html_coverage; then
  cp -Rf /opt/metwork-${MODULE}-${BRANCH_NAME}/html_coverage /working_directory/
else
  mkdir /working_directory/html_coverage
  echo "<html><head></head><body><p>nothing yet</p></body></html>" >/working_directory/html_coverage/index.html
fi
chmod -R a+w /working_directory/*.rpm
chmod -R a+w /working_directory/*.tar.bz2
chmod -R a+w /working_directory/html_doc
chmod -R a+w /working_directory/html_coverage
