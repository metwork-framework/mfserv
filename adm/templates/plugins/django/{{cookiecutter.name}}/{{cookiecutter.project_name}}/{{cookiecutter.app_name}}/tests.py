{% if cookiecutter.type == "gunicorn3_sync" %}from django.test import TestCase
{% elif cookiecutter.type == "gunicorn2_sync" %}# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
{% endif %}
# Create your tests here.
