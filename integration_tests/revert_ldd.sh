#!/bin/bash

function usage() {
    echo "revert_ldd.sh /path"
    echo "  => execute this in a directory and it will try to find who"
    echo "     need this shared library"
}

if test "$1" = ""; then
    usage
    exit 1
fi
if test "$1" = "--help"; then
    usage
    exit 0
fi

for F in $(find . -type f -name "*.so*" ; find . -type f -wholename "*/bin/*"); do
    N=$(ldd "${F}" 2>/dev/null |grep "=>" |awk -F '=>' '{print $2;}' |grep -c "$1")
    if test "$N" -gt 0; then
        echo "${F}"
    fi
done
