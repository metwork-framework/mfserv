#!/usr/bin/env python3

import os
from mfutil import BashWrapperOrRaise

NGINX_PORT = int(os.environ['MFSERV_NGINX_PORT'])

#python2@mfext may not be installed
bash_wrapper = BashWrapperOrRaise("is_layer_installed python2@mfext")
if bash_wrapper.stdout != "1":
    templates = ("python3_noweb", "node_noweb")
else:
    templates = ("python3_noweb", "python2_noweb", "node_noweb")

for template in templates:

    BashWrapperOrRaise("rm -Rf foobar")
    BashWrapperOrRaise("plugins.uninstall foobar || true")

    print(BashWrapperOrRaise("bootstrap_plugin.py create --template=%s "
                             "--no-input foobar" % template))
    print(BashWrapperOrRaise("cd foobar && make release"))
    print(BashWrapperOrRaise('cd foobar && plugins.install "$(ls *.plugin)"'))

    print("ok")
