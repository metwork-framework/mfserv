#!/bin/bash


OK_DEPS=$(cat list.txt|xargs)
OK_NOT_FOUND=$(cat list_ok_not_found.txt |xargs)

#N=$(cat /etc/redhat-release 2>/dev/null |grep -c "^CentOS release 6")
#if test "${N}" -eq 0; then
#    echo "We test this only on centos6"
#    exit 0
#fi

export PATH=${PATH}:${PWD}/..
RET=0


cd "${MFMODULE_HOME}" || exit 1
cd opt
for layer in `ls`; do
    cd "${layer}"
    echo
    echo "=== System extra dependencies layer ${layer} ==="
    echo
    echo "--- external dependencies ---" ${DEPS2}
    current_layer=`cat .layerapi2_label`
    DEPS1=$(layer_wrapper --layers=${current_layer} -- external_dependencies.sh |awk -F '/' '{print $NF}' |xargs)
    # We don t consider libraries available in the layer (they should not be here, probably a LD_LIBRARY_PATH issue)
    DEPS2=""
    for lib in ${DEPS1}; do
        found=$(find . -name ${lib} -print)
        if test "${found}" != ""; then
            DEPS2="${DEPS2} ${lib}"
        fi
    done
    for DEP in ${DEPS2}; do
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
    echo "--- dependencies not found ---" ${DEPS4}
    DEPS3=$(layer_wrapper --layers=${current_layer} -- external_dependencies_not_found.sh |xargs)
    # We don t consider libraries available in the layer (they should not be here, probably a LD_LIBRARY_PATH issue)
    DEPS4=""
    for lib in ${DEPS3}; do
        found=$(find . -name ${lib} -print)
        if test "${found}" != ""; then
            DEPS4="${DEPS4} ${lib}"
        fi
    done
    for DEP in ${DEPS4}; do
        FOUND=0
        for OK_DEP in ${OK_NOT_FOUND}; do
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
