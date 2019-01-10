{% if cookiecutter.type == "gunicorn3_sync" %}from django.contrib import admin

# Register your models here.{% elif cookiecutter.type == "gunicorn2_sync" %}# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.{% endif %}
