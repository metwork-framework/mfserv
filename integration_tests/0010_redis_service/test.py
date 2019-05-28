#!/usr/bin/env python3

import datetime
import sys
import requests
import os
import time
from mfutil import BashWrapperOrRaise

NGINX_PORT = int(os.environ['MFSERV_NGINX_PORT'])

VERSION = 3
BashWrapperOrRaise("rm -Rf foobar")
BashWrapperOrRaise("plugins.uninstall foobar || true")

print(BashWrapperOrRaise("bootstrap_plugin.py create --template=default "
                         "foobar <stdin_python%i" % VERSION))
cmd = "cat foobar/config.ini |sed 's/^redis_service=.*$/redis_service=1/g' " \
    ">foobar/config.ini2"
BashWrapperOrRaise(cmd)
BashWrapperOrRaise("mv -f foobar/config.ini2 foobar/config.ini")
BashWrapperOrRaise("cp -f wsgi.py foobar/main/wsgi.py")
with open("foobar/python%i_virtualenv_sources/"
          "requirements-to-freeze.txt" % VERSION, "w") as f:
    f.write("redis\n")
print(BashWrapperOrRaise("cd foobar && make release"))
print(BashWrapperOrRaise('cd foobar && plugins.install "$(ls *.plugin)"'))

now_fn = datetime.datetime.now
before = now_fn()
code = 1
while (now_fn() - before).total_seconds() <= 30:
    time.sleep(1)
    url = "http://127.0.0.1:%i/foobar" % NGINX_PORT
    print("trying GET %s..." % url)
    try:
        x = requests.get(url, timeout=3)
    except Exception:
        continue
    if x.status_code == 200:
        if x.text.strip() == "Hello World!":
            code = 0
            break

if code != 0:
    print("ERROR: can't get a valid output")
    sys.exit(code)
else:
    BashWrapperOrRaise("plugins.uninstall foobar")
    BashWrapperOrRaise("rm -Rf foobar")
    print("ok")

sys.exit(0)
