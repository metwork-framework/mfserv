# Introduction to MFSERV

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


Thanks to its [plugin templates](../040-mfserv_create_plugins/#3-plugin-templates),  MFSERV ease you into a web server implementation:

- a [WSGI server](https://www.python.org/dev/peps/pep-3333/) for running Python web applications. Available MFSERV templates are:

    - the [default template](../040-mfserv_create_plugins/#31-the-default-template)
    - the [django template](../040-mfserv_create_plugins/#32-the-django-template)
    - the [flask template](../040-mfserv_create_plugins/#33-the-flask-template)

- a [Node.js](https://nodejs.org/) server through the [Express web application framework](https://expressjs.com/). The corresponding MFSERV template is the [node template](../040-mfserv_create_plugins/#34-the-node-template).
- a [asynchronous HTTP Server for asyncio and Python (aiohttp)](https://aiohttp.readthedocs.io/en/stable/web.html). The corresponding MFSERV template is the [default template](../040-mfserv_create_plugins/#31-the-default-template).
- a `static web server`. The corresponding MFSERV template is the [static template](../040-mfserv_create_plugins/#35-the-static-template).
- a `crontab container` or a `daemon`. The corresponding MFSERV template is the [empty template](../040-mfserv_create_plugins/#36-the-empty-template).

If the MFSERV plugin is [configured for monitoring](../080-mfserv_tuning_monitoring/#21-monitor-a-plugin), the metrics are send via [Telegraf](https://docs.influxdata.com/telegraf/) to the [InfluxDB](https://docs.influxdata.com/influxdb/) database on the MFADMIN server.

!!! info "See also"

    - [MFADMIN Documentation](../../../mfadmin)
    - [MFADMIN monitoring plugins](../../../mfadmin/950-old_docs/mfadmin_monitoring_plugins)
    - [Circus hooks](../../../mfadmin/950-old_docs/mfadmin_miscellaneous/#27-circus-hooks)
    - [A new way to serve (python) web apps article](https://medium.com/metwork-framework/a-new-way-to-serve-python-web-apps-d5662ab69dc0)

## MFSERV configuration

The configuration of the MFSERV and its components is stored in the `config/config.ini` file of the root directory of the `mfserv` user. Check this file for further information.

<!--
Intentional comment to prevent m2r from generating bad rst statements when the file ends with a block .. xxx ::
-->
