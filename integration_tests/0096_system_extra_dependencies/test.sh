#!/bin/bash


OK_DEPS=$(cat list.txt list_ok_not_found.txt |xargs)

N=$(cat /etc/redhat-release 2>/dev/null |grep -c "^CentOS release 6")
if test "${N}" -eq 0; then
    echo "We test this only on centos6"
    exit 0
fi

export PATH=${PATH}:${PWD}/..
RET=0


cd "${MFMODULE_HOME}" || exit 1
cd opt
for layer in `ls`; do
    cd "${layer}"
    echo
    echo "=== System extra dependencies layer ${layer} ==="
    echo
    current_layer=`cat .layerapi2_label`
    DEPS1=$(layer_wrapper --layers=${current_layer} -- external_dependencies.sh |awk -F '/' '{print $NF}' |xargs)
    echo "--- extra dependencies ---" ${DEPS1}
    DEPS2=$(layer_wrapper --layers=${current_layer} -- external_dependencies_not_found.sh |xargs)
    echo "--- dependencies not found ---" ${DEPS2}
    DEPS=$(echo $DEPS1 $DEPS2)
    for DEP in ${DEPS}; do
        FOUND=0
        for OK_DEP in ${OK_DEPS}; do
            if test "${DEP}" = "${OK_DEP}"; then
                FOUND=1
                break
            fi
        done
        if test "${FOUND}" = "1"; then
            continue
        fi
        echo "***** ${DEP} *****"
        echo "=== revert ldd ==="
        revert_ldd.sh "${DEP}"
        echo
        echo
        RET=1
    done
    cd ..
done


if test "${RET}" = "1"; then
    echo "extra dependencies found"
    exit 1
fi
