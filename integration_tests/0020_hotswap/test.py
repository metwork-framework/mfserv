#!/usr/bin/env python3

import datetime
import sys
import requests
import os
import time
import threading
from mfutil import BashWrapperOrRaise

NGINX_PORT = int(os.environ['MFSERV_NGINX_PORT'])
RUN = True
RES = True

BashWrapperOrRaise("rm -Rf foobar")
BashWrapperOrRaise("plugins.uninstall foobar || true")

print(BashWrapperOrRaise("bootstrap_plugin.py create "
                         "--template=python3_django "
                         "--no-input foobar"))
print(BashWrapperOrRaise("cd foobar && make release"))
print(BashWrapperOrRaise('cd foobar && plugins.install "$(ls *.plugin)"'))


def continuous_check():
    global RES
    while RUN:
        url = "http://127.0.0.1:%i/foobar" % NGINX_PORT
        x = requests.get(url, timeout=3)
        if x.status_code != 200:
            print("bad status code: %i" % x.status_code)
            print(x)
            RES = False
        if "Hello World" not in x.text:
            print("bad output: %s" % x.text)
            print(x)
            RES = False
        time.sleep(0.1)


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
        if "Hello World" in x.text:
            code = 0
            break

if code != 0:
    print("ERROR: can't get a valid output")
    sys.exit(code)

# let's start a continuous_check
t = threading.Thread(target=continuous_check)
t.start()
print(BashWrapperOrRaise('cd foobar && plugins.hotswap "$(ls *.plugin)"'))
RUN = False
t.join()
if RES is False:
    sys.exit(1)
BashWrapperOrRaise("plugins.uninstall foobar || true")
BashWrapperOrRaise("rm -Rf foobar")
print("ok")
sys.exit(0)
