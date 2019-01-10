"""
WSGI config for {{cookiecutter.project_name}} project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/{% if cookiecutter.type == "gunicorn3_sync" %}2.1{% elif cookiecutter.type == "gunicorn2_sync" %}1.11{% endif %}/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', '{{cookiecutter.project_name}}.settings')

application = get_wsgi_application()
