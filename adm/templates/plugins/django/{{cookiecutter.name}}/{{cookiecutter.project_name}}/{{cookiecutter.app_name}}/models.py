{% if cookiecutter.type == "gunicorn3_sync" %}from django.db import models
{% elif cookiecutter.type == "gunicorn2_sync" %}# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
{% endif %}
# Create your models here.
