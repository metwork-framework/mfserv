#!/usr/bin/env python3

from cookiecutter_hooks import post_gen_project
import random
import shutil
import os


post_gen_project()

"""Tasks to be run once the project has been generated.

It includes :
- the creation secret key for the Django project
- the deletion of the unnecessary files (disabled by the user or empty)
- the initialisation of a git repository if asked
"""


def get_random_string(len):
    """Generate a random string with the given length."""
    chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
    return ''.join([random.choice(chars) for _ in range(len)])


def set_django_secret_key(file_path):
    """Set the secret key of a Django project."""
    value = get_random_string(50)
    flag = 'DJANGO_SECRET_KEY_TO_BE_SET'
    with open(file_path, 'r+') as f:
        file_contents = f.read().replace(flag, value)
        f.seek(0)
        f.write(file_contents)
        f.truncate()


# generate a random secret key for the Django project
set_django_secret_key(os.path.join('{{cookiecutter.project_name}}',
                                   '{{cookiecutter.project_name}}',
                                   'settings.py'))


# remove the default application in the Django project if none is wanted
if '{{cookiecutter.app_name}}' == 'None':
    shutil.rmtree(os.path.join('{{cookiecutter.project_name}}',
                               '{{cookiecutter.app_name}}'))
