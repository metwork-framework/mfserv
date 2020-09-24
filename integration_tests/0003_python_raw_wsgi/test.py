#!/usr/bin/env python3

import datetime
import sys
import requests
import os
import time
from mfutil import BashWrapperOrRaise

NGINX_PORT = int(os.environ['MFSERV_NGINX_PORT'])

#python2@mfext may not be installed
bash_wrapper = BashWrapperOrRaise("is_layer_installed python2@mfext")
if bash_wrapper.stdout != "1":
    VERSIONS = [ 3 ]
else:
    VERSIONS= [ 3, 2 ]

for VERSION in VERSIONS:
    BashWrapperOrRaise("rm -Rf foobar")
    BashWrapperOrRaise("plugins.uninstall foobar || true")

    print(BashWrapperOrRaise("bootstrap_plugin.py create --no-input "
                             "--template=python%i_raw_wsgi "
                             "foobar" % VERSION))
    with open("foobar/python%i_virtualenv_sources/"
              "requirements-to-freeze.txt" % VERSION, "w") as f:
        f.write("falcon\n")
    BashWrapperOrRaise('echo "import falcon" >foobar/main/wsgi2.py')
    BashWrapperOrRaise('cat foobar/main/wsgi.py >>foobar/main/wsgi2.py')
    BashWrapperOrRaise('mv -f foobar/main/wsgi2.py foobar/main/wsgi.py')
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
