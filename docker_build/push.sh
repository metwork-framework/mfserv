#!/bin/bash

if test "${NOPUSH}" = "1"; then
    echo "NOPUSH=1, we don't push"
    exit 0
fi

MODULE=${1}
BRANCH=${2}
OS=${3}

ssh mfftp@synapse mkdir -p /data/var_ftp/pub/metwork/releases/tar.bz2/continuous_integration/${OS}/${BRANCH}
scp *.tar.bz2 mfftp@synapse:/data/var_ftp/pub/metwork/releases/tar.bz2/continuous_integration/${OS}/${BRANCH}/
ssh mfftp@synapse mkdir -p /data/var_ftp/pub/metwork/releases/rpms/continuous_integration/${OS}/${BRANCH}
scp *.rpm mfftp@synapse:/data/var_ftp/pub/metwork/releases/rpms/continuous_integration/${OS}/${BRANCH}/
ssh mfftp@synapse createrepo --update /data/var_ftp/pub/metwork/releases/rpms/continuous_integration/${OS}/${BRANCH}
ssh mfftp@synapse mkdir -p /data/var_ftp/pub/metwork/docs/${BRANCH}/${MODULE}
ssh mfftp@synapse mkdir -p /data/var_ftp/pub/metwork/coverages/${BRANCH}/${MODULE}
scp -r html_doc/* mfftp@synapse:/data/var_ftp/pub/metwork/docs/${BRANCH}/${MODULE}/
scp -r html_coverage/* mfftp@synapse:/data/var_ftp/pub/metwork/coverages/${BRANCH}/${MODULE}/
