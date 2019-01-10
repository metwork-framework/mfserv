{% if cookiecutter.type == "gunicorn3_sync" %}from django.apps import AppConfig
{% elif cookiecutter.type == "gunicorn2_sync" %}# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig
{% endif %}

class {{cookiecutter.app_name | capitalize }}Config(AppConfig):
    name = '{{cookiecutter.app_name}}'
