#!/usr/bin/env python3

import datetime
import sys
import requests
import os
import time
from mfutil import BashWrapperOrRaise

NGINX_PORT = int(os.environ['MFSERV_NGINX_PORT'])

BashWrapperOrRaise("rm -Rf foobar")
BashWrapperOrRaise("plugins.uninstall foobar || true")

print(BashWrapperOrRaise("bootstrap_plugin.py create --template=empty "
                         "--no-input foobar"))
print(BashWrapperOrRaise("cd foobar && make release"))
print(BashWrapperOrRaise('cd foobar && plugins.install "$(ls *.plugin)"'))

print("ok")
