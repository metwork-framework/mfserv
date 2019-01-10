#!/usr/bin/env python3


"""Tasks to be run before the project is generated.

It checks that :
- the project name to create is not empty
- the application name is not empty and different from the project name
"""


import sys


# the project name and the application name must be significant
if not '{{cookiecutter.project_name}}'.strip():
    print('ERROR: project_name cannot be empty')
    sys.exit(1)
if not '{{cookiecutter.app_name}}'.strip():
    print('ERROR: app_name cannot be empty; if you do not want to create '
          'an application now set the value "None".')
    sys.exit(1)

# the application name cannot be the same as its project name
if '{{cookiecutter.app_name}}' == '{{cookiecutter.project_name}}':
    print('ERROR: app_name cannot have the same name as its project name.')
    sys.exit(1)
