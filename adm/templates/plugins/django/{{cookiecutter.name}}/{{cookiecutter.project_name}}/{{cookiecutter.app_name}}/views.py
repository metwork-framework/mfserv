{% if cookiecutter.type == "gunicorn2_sync" %}# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render{% endif %}
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world!")
