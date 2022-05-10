#!/usr/bin/env python3


"""Tasks to be run before the project is generated.

It checks that :
- the plugin name is != main (because it's the default app name)
"""


import sys

# the application name cannot be the same as its plugin name
if 'main' == '{{cookiecutter.name}}':
    print('ERROR: you cant use main as plugin name '
          'because we create a default app named main')
    sys.exit(1)
