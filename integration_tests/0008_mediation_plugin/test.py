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
BashWrapperOrRaise("rm -Rf foobar2")
BashWrapperOrRaise("plugins.uninstall foobar2 || true")

print(BashWrapperOrRaise("bootstrap_plugin.py create --template=static "
                         "--no-input foobar2"))
print(BashWrapperOrRaise("cd foobar2 && make release"))
print(BashWrapperOrRaise('cd foobar2 && plugins.install "$(ls *.plugin)"'))
print(BashWrapperOrRaise("bootstrap_plugin.py create --template=mediation "
                         "--no-input foobar"))
with open("foobar/main/application.py", "r") as f:
    c = f.read()
c2 = c.replace('mybackend%s" % url_path_qs',
               '127.0.0.1:%i/foobar2/index.html"' %
               int(os.environ['MFSERV_NGINX_PORT']))
with open("foobar/main/application.py", "w") as f:
    f.write(c2)
print(BashWrapperOrRaise("cd foobar && make release"))
print(BashWrapperOrRaise('cd foobar && plugins.install "$(ls *.plugin)"'))

now_fn = datetime.datetime.now
before = now_fn()
code = 1
while (now_fn() - before).total_seconds() <= 20:
    time.sleep(1)
    url = "http://127.0.0.1:%i/foobar" % NGINX_PORT
    print("trying GET %s..." % url)
    try:
        x = requests.get(url, timeout=3)
    except Exception:
        continue
    if x.status_code == 200:
        if "Hello" in x.text.strip():
            code = 0
            break

if code != 0:
    print("ERROR: can't get a valid outpu")
else:
    BashWrapperOrRaise("plugins.uninstall foobar")
    BashWrapperOrRaise("rm -Rf foobar")
    BashWrapperOrRaise("plugins.uninstall foobar2")
    BashWrapperOrRaise("rm -Rf foobar2")
    print("ok")

sys.exit(code)
