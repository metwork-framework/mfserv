#!/bin/bash

# find external dependencies (system) with a dynamic link with metwork libs

export PATH=${PATH}:${PWD}/..
RET=0
FIC_DEPS=`pwd`/deps

cd "${MFMODULE_HOME}" || exit 1
external_dependencies.sh >${FIC_DEPS}
for F in $(cat ${FIC_DEPS}); do
    N=$(ldd "${F}" 2>/dev/null |grep -c metwork)
    if test "$N" -gt 0; then
        echo "***** $F *****"
        echo "=== ldd |grep metwork ==="
        ldd "${F}" |grep metwork
        echo
        echo "=== revert ldd ==="
        revert_ldd.sh "${F}"
        echo
        echo
        RET=1
    fi
done


rm -f ${FIC_DEPS}
if test "${RET}" = "1"; then
    echo "suspicious dependencies found but not exiting 1"
    #exit 1
fi
