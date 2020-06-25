# Introduction to MFSERV

.. index:: aiohttp, Node.js
## What is mfserv?

This in the **M**etwork **F**ramework "**SERV**ices" module. This module is a kind of private [PAAS](https://en.wikipedia.org/wiki/Platform_as_a_service) which help to develop, run and manage webservices applications.

With this module, you can easily implement robust webservices with:

- synchronous Python3 and synchronous Python2 (with a custom virtualenv including the framework you want like [Django](https://www.djangoproject.com/), [Flask](http://flask.pocoo.org/)...)
- asynchronous Python3 (with [aiohttp](https://aiohttp.readthedocs.io/) and your custom virtualenv)
- [nodejs](http://nodejs.org) (and your custom `node_modules`)

All these technologies are managed in a "production ready" with:

- a dynamically configured `nginx` webserver in front
- some multiple workers in back
- memory limits
- autorestart features
- logs and metrics

.. index:: WSGI server, Node.js server, templates, plugin templates, Django, Flask
## How it works?

![image](overall_architecture.svg)

**MSERV relies on the following components:**

- [Circus](https://circus.readthedocs.io/en/latest/) monitors and controls processes and sockets. Circus acts as a process watcher and runner. You may check the full `circus.ini` configuration file in the `tmp/config_auto/` in the root directory of the `mfadmin` user. Check the [Circus architecture](https://circus.readthedocs.io/en/latest/design/architecture/)
- [Telegraf](https://docs.influxdata.com/telegraf/) acts as a server agent for collecting and sending metrics and events from databases, systems, and IoT sensors.
- [Elasticsearch](https://www.elastic.co/products/elasticsearch) is a distributed, RESTful search and analytics engine.
- [Nginx](https://www.nginx.com/) acts as a web server container.
- [jsonlog2elasticsearch](https://github.com/metwork-framework/jsonlog2elasticsearch) is a daemon to send json logs read from a log file to elasticsearch.
- mflog2mfadmin (based jsonlog2elasticsearch) is a daemon to send [mflog](https://github.com/metwork-framework/mflog) logs to elasticsearch.
- `conf_monitor` is a Metwork tool in order to monitor the configuration files.

Circus acts as a process watcher and runner. You may check the full `circus.ini` configuration file in the `/home/mfserv/tmp/config_auto/` directory. Check the [Circus architecture](https://circus.readthedocs.io/en/latest/design/architecture/)

`{% raw %}app-{{PLUGIN.name}}.{{APP.name}}{% endraw %}` is the app defines in your plugin.  There are as many `{% raw %}app-{{PLUGIN.name}}.{{APP.name}}{% endraw %} ` as plugins. You may have more than one `app` in the same plugin.


Thanks to its :ref:`plugin templates <mfserv_create_plugins:Plugin templates>`,  MFSERV ease you into a web server implementation:
- a [WSGI server](https://www.python.org/dev/peps/pep-3333/) for running Python web applications. Available MFSERV templates are:
    - the :ref:`default template <mfserv_create_plugins_the_default_template>`
    - the :ref:`django template <mfserv_create_plugins_the_django_template>`
    - the :ref:`flask template <mfserv_create_plugins_the_flask_template>`
- a [Node.js](https://nodejs.org/) server through the [Express web application framework](https://expressjs.com/). The corresponding MFSERV template is the :ref:`node template <mfserv_create_plugins_the_node_template>`.
- a [asynchronous HTTP Server for asyncio and Python (aiohttp)](https://aiohttp.readthedocs.io/en/stable/web.html). The corresponding MFSERV template is the :ref:`default template <mfserv_create_plugins_the_default_template>`.
- a :index:`static web server`. The corresponding MFSERV template is the :ref:`static template <mfserv_create_plugins_the_static_template>`.
- a :index:`crontab container` or a :index:`daemon`. The corresponding MFSERV template is the :ref:`empty template <mfserv_create_plugins_the_empty_template>`.

If the MFSERV plugin is :ref:`configured for monitoring <mfserv_tuning_monitoring:Monitor a plugin>`, the metrics are send via [Telegraf](https://docs.influxdata.com/telegraf/) to the [InfluxDB](https://docs.influxdata.com/influxdb/) database on the MFADMIN server.

.. seealso::
    | :doc:`MFADMIN Documentation <mfadmin:index>`
    | :doc:`mfadmin:mfadmin_monitoring_plugins`
    | :ref:`mfadmin:mfadmin_miscellaneous:Circus hooks`
    | `A new way to serve (python) web apps article <https://medium.com/metwork-framework/a-new-way-to-serve-python-web-apps-d5662ab69dc0>`_

.. index:: configuration
## MFSERV configuration

The configuration of the MFSERV and its components is stored in the `config/config.ini` file of the root directory of the `mfserv` user. Check this file for further information.

<!--
Intentional comment to prevent m2r from generating bad rst statements when the file ends with a block .. xxx ::
-->
