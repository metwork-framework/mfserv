#!/usr/bin/env python3

import datetime
import sys
import requests
import os
import time
from mfutil import BashWrapperOrRaise

NGINX_PORT = int(os.environ['MFSERV_NGINX_PORT'])

BashWrapperOrRaise("plugins.uninstall mystatic || true")

print(BashWrapperOrRaise('plugins.install "$(ls *.plugin)"'))

now_fn = datetime.datetime.now
before = now_fn()
code = 0
for url in ("http://127.0.0.1:%i/mystatic/index.html" % NGINX_PORT,
            "http://127.0.0.1:%i/mystatic/" % NGINX_PORT,
            "http://127.0.0.1:%i/mystatic" % NGINX_PORT):
    res = False
    while (now_fn() - before).total_seconds() <= 30:
        time.sleep(1)
        print("trying GET %s..." % url)
        try:
            x = requests.get(url, timeout=3)
        except Exception:
            continue
        if x.status_code == 200:
            if "Hello" in x.text.strip():
                res = True
                break
    if not res:
        code = 1
        break

if code != 0:
    print("ERROR: can't get a valid works.txt")
else:
    BashWrapperOrRaise("plugins.uninstall mystatic")
    print("ok")

sys.exit(code)
