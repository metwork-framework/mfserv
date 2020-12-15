#!/bin/bash

function usage() {
    echo "usage: external_dependencies.sh"
    echo "  => execute this is a directory and it will try to find all "
    echo "     external (not metwork) dependencies (with ldd)"
}

if test "${1:-}" = "--help"; then
    usage
    exit 0
fi

( find . -type f -name "*.so*" -exec ldd {} 2>/dev/null \; ; find . -type f -wholename "./bin/*" -exec ldd {} 2>/dev/null \;) |grep "=>" | grep "not found" |awk -F '=>' '{print $1;}' |sort |uniq
