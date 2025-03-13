#!/usr/bin/env python3

import datetime
import sys
import requests
import os
import time
from mfutil import BashWrapperOrRaise

NGINX_PORT = int(os.environ['MFSERV_NGINX_PORT'])

BashWrapperOrRaise("rm -Rf foophp")
BashWrapperOrRaise("plugins.uninstall foophp || true")

print(BashWrapperOrRaise("bootstrap_plugin.py create --template=php "
                         "--no-input foophp"))
print(BashWrapperOrRaise("cd foophp && make release"))
print(BashWrapperOrRaise('cd foophp && plugins.install "$(ls *.plugin)"'))

now_fn = datetime.datetime.now
before = now_fn()
code = 1
while (now_fn() - before).total_seconds() <= 30:
    time.sleep(1)
    url = "http://127.0.0.1:%i/foophp/index.php" % NGINX_PORT
    print("trying GET %s..." % url)
    try:
        x = requests.get(url, timeout=3)
    except Exception:
        continue
    if x.status_code == 200:
        if "Hello world !" in x.text:
            code = 0
            break

if code != 0:
    print("ERROR: can't get a valid output")
    sys.exit(code)
else:
    BashWrapperOrRaise("plugins.uninstall foophp")
    BashWrapperOrRaise("rm -Rf foophp")
    print("ok")

sys.exit(0)
