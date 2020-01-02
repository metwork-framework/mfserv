#!/usr/bin/env python3

import os
from mfutil import BashWrapperOrRaise

NGINX_PORT = int(os.environ['MFSERV_NGINX_PORT'])

for template in ("python3_noweb", "python2_noweb", "node_noweb"):

    BashWrapperOrRaise("rm -Rf foobar")
    BashWrapperOrRaise("plugins.uninstall foobar || true")

    print(BashWrapperOrRaise("bootstrap_plugin.py create --template=%s "
                             "--no-input foobar" % template))
    print(BashWrapperOrRaise("cd foobar && make release"))
    print(BashWrapperOrRaise('cd foobar && plugins.install "$(ls *.plugin)"'))

    print("ok")
