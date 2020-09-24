#!/usr/bin/env python3

import datetime
import sys
import os
import time
from mfutil import BashWrapperOrRaise, get_unique_hexa_identifier

NGINX_PORT = int(os.environ['MFSERV_NGINX_PORT'])

UNIQUE = get_unique_hexa_identifier()
BashWrapperOrRaise("rm -Rf foobar")
BashWrapperOrRaise("plugins.uninstall foobar || true")

print(BashWrapperOrRaise("bootstrap_plugin.py create --template=python3_noweb "
                         "--no-input foobar"))
with open("foobar/config.ini", "a") as f:
    f.write("\n\n[extra_daemon_foo]\n")
    f.write("_cmd_and_args = foo.sh %s\n" % UNIQUE)
    f.write("numprocesses=1\n")
BashWrapperOrRaise("mkdir -p foobar/bin")
BashWrapperOrRaise("cp -f foo.sh foobar/bin/")
BashWrapperOrRaise("chmod +x foobar/bin/foo.sh")

print(BashWrapperOrRaise("cd foobar && make develop"))

now_fn = datetime.datetime.now
before = now_fn()
code = 1
while (now_fn() - before).total_seconds() <= 30:
    time.sleep(1)
    print("waiting for /tmp/foobar.%s" % UNIQUE)
    c = None
    try:
        with open("/tmp/foobar.%s" % UNIQUE, "r") as f:
            c = f.read().strip()
    except Exception:
        continue
    if c == "foobar":
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
