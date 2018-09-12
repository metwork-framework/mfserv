#!/bin/bash

BRANCH_NAME=$1
PACKAGE=$2

RES=`docker run --rm -t centos:centos6 bash -c 'echo -e "[metwork]\nname=Metwork Continuous Integration Branch '${BRANCH_NAME}'\nbaseurl=ftp://synapse.meteo.fr/pub/metwork/releases/rpms/continuous_integration/centos6/'${BRANCH_NAME}'\ngpgcheck=0\nenabled=1\nmetadata_expire=0\n" >/etc/yum.repos.d/metwork.repo ; yum --disablerepo=* --enablerepo=metwork -q list available '${PACKAGE} |grep "^${PACKAGE}"`
if test $? -ne 0; then
    BRANCH_NAME=master
    RES=`docker run --rm -t centos:centos6 bash -c 'echo -e "[metwork]\nname=Metwork Continuous Integration Branch master\nbaseurl=ftp://synapse.meteo.fr/pub/metwork/releases/rpms/continuous_integration/centos6/master\ngpgcheck=0\nenabled=1\nmetadata_expire=0\n" >/etc/yum.repos.d/metwork.repo ; yum --disablerepo=* --enablerepo=metwork -q list available '${PACKAGE} |grep "^${PACKAGE}"`
    if test $? -ne 0; then
        echo "notfound~~~notfound"
        exit 1
    fi
fi
MD5SUM=`echo ${RES} |md5sum |awk '{print $1;}'`
echo "${BRANCH_NAME}~~~${MD5SUM}"
exit 0
