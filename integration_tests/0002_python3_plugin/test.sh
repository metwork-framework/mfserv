#!/bin/bash

plugins.uninstall foobar >/dev/null 2>&1
rm -Rf foobar*

set -x
set -e

bootstrap_plugin.py create --no-input foobar

cd foobar
echo django >python3_virtualenv_sources/requirements-to-freeze.txt
make release
plugins.install "$(ls *.plugin)"
plugins.uninstall foobar
rm -Rf foobar*
