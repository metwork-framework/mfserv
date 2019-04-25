#!/usr/bin/env python3


"""Tasks to be run before the project is generated.

It checks that :
- the plugin name is != hello (because it's the default app name)
"""


import sys

# the application name cannot be the same as its plugin name
if 'hello' == '{{cookiecutter.name}}':
    print('ERROR: you cant use hello as plugin name '
          'because we create a default app named hello')
    sys.exit(1)
