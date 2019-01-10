{% if cookiecutter.type == "gunicorn3_sync" %}from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]{% elif cookiecutter.type == "gunicorn2_sync" %}from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.index, name='index'),
]{% endif %}
