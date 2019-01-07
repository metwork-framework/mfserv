#!/bin/bash

plugins.uninstall foobar >/dev/null 2>&1
rm -Rf foobar*

set -x
set -e

mfserv.start
bootstrap_plugin.py create --no-input foobar

cd foobar
echo django >python3_virtualenv_sources/requirements-to-freeze.txt
make release
plugins.install "*.plugin"
plugins.uninstall foobar
mfserv.stop
rm -Rf foobar*
