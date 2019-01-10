"""{{cookiecutter.project_name}} URL Configuration

{% if cookiecutter.type == "gunicorn3_sync" %}The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

inc = [
    path('{{cookiecutter.project_name}}/{{cookiecutter.app_name}}/', include('{{cookiecutter.app_name}}.urls')),
    path('{{cookiecutter.project_name}}/admin/', admin.site.urls),
]

urlpatterns = [
    path('{{cookiecutter.name}}/', include(inc))
]{% elif cookiecutter.type == "gunicorn2_sync" %}The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include, url

inc = [
    url('mysite/firstapp/', include('firstapp.urls')),
    url('mysite/admin/', admin.site.urls),
]

urlpatterns = [
    url('blabla/', include(inc))
]{% endif %}
