
# Miscellaneous

.. index:: layerapi2, layerapi2_dependencies, .layerapi2_dependencies, dependencies
## The `.layerapi2_dependencies` file

When you create a plugin with the :ref:`bootstap_plugin <mfserv_create_plugins:Create and customize the plugin>` command, a `.layerapi2_dependencies` file is created in the plugin root directory. This file contains the module/package dependencies you need for the plugin.

By default, the `.layerapi2_dependencies` file contains only minimal dependencies, e.g.:
```cfg
root@mfserv
python3@mfserv
```
means the plugin will use the :doc:`layer_root` and :doc:`layer_python3` supplied in MFSERV.

For more details on `layerapi2`, check :doc:`MFEXT layerapi2 <mfext:layerapi2>` and :ref:`MFEXT layerapi2 syntax <mfext:layerapi2_syntax>` documentation.

Let's assume you need a module or package which is available in the MFEXT 'scientific' package, you have to add this dependencies to the `.layerapi2_dependencies` file:
```cfg
root@mfserv
python3@mfserv
python3_scientific@mfext
```

Let's assume now, you want to build your plugin relies on Python2 instead of Python3, the `.layerapi2_dependencies` file will look like this:
```cfg
root@mfserv
python2@mfserv
python2_scientific@mfext
```

.. index:: layerapi2, layerapi2_extra_env, .layerapi2_extra_env
## The `.layerapi2_extra_env` file

The `.layerapi2_extra_env` file allows you to defined environment variable only in the plugin context. Check `layerapi2` MFEXT documentation.

By default, this `.layerapi2_extra_env` doesn't exist. If you need to add extra environment variables, create this file in the plugin root directory.

.. seealso::
    :ref:`MFEXT layerapi2 syntax <mfext:layerapi2_syntax>` documentation.


.. index:: multiple applications
## Plugins with more than one application

.. important::
    | This section doesn't apply to :ref:`Node.js plugins <mfserv_create_plugins_the_node_template>`. For those plugins, only ONE section `[app_xxx]` is allowed.

A plugin may one or more application.

In most cases, when you create a plugin with `bootstrap_plugin.py`, only one application called `main` is created with the corresponding script(s) (i.e. in the `main` directory).

However, you may create a plugin with more than one application. 

For instance, let's add a second application in the :ref:`foo_default plugin example <mfserv_quick_start:Create the plugin>`.

First, **duplicate the** `main` **directory** of the `foo_default` plugin directory and name it `second`

Then duplicate the  `[app_main]` section of the `config.ini` file of the plugin, rename the duplicated section `[app_second]` and change its `main_arg` parameter value as follows: 
```cfg
main_arg = second.wsgi:application
```

Edit the `second/wsgi.py` script as follows (just change the response message):
```python
import os

from mflog import get_logger

logger = get_logger("myapp")


def application(environ, start_response):
    my_url = os.environ.get("MFSERV_PLUGIN_FOO_DEFAULT_MY_URL", "")

    status = '200 OK'
    output = '<h1>Hello World from second application!</h1>'
    if my_url != "":
        output = '{}</br></br><a href="{}">Visit Metwork Framework blog</a>'.format(output, my_url)
    logger.info("this is a test message")
    response_headers = [('Content-Type', 'text/html; charset=utf-8'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output.encode('utf-8')]

```

Let's now **install (as dev build)** the plugin by entering the command (from the `foo_default` plugin directory):

```bash
make develop
```

From a web browser, enter the url of your `second` application: `http://localhost:18868/foo_default/second` or  `http://{remote_host}:18868/foo_default/second`. A 'Hello World from second application!.' HTML page with a link to `my_url` should be displayed.

Enter the url of your `main` application: `http://localhost:18868/foo_default/main`. A 'Hello World from second application!.' HTML page with a link to `my_url` should be displayed.

.. note::
    | Because your application is named `main`, you don't need to specify the application name in the url. This is the default application. `http://localhost:18868/foo_default` and `http://localhost:18868/foo_default/main` do the same.
    | However, if you rename the `[app_main]` section of the `config.ini` by `[app_first]`, the `http://localhost:18868/foo_default` url won't work anymore, you have to specify the application name, i.e. `http://localhost:18868/foo_default/first` (you don't need to rename the `main` directory and the `main_arg` value).
    

.. index:: outside command
.. _outside_metwork_command:

## The `outside` Metwork command

The `outside` is a command utility that allow you execute commands outside the Metwork environment.

For instance, let's assume the Python version of Metwork is 3.5.6 and the Python version installed on your system is Python 2.7.5.

For instance:

- Entering the command from the Metwork environment:

```bash
python --version
```
```
Python 3.5.6
```

- Entering the command from the Metwork environment:

```bash
outside python --version
```
```
Python 2.7.5
```
.. index:: crontab support
.. _mfserv_crontab_support:
## The `crontab` support

Each plugin has a `crontab` support to schedule the execution of programs.

In order to enable your plugin `crontab`, just create a `crontab` file in the root directory of the plugin and set the tasks you want to schedule. For further details about `crontab`, check the Linux documentation (`man crontab` command or http://man7.org/linux/man-pages/man5/crontab.5.html)

In order to (re)load the contab file:
- If the crontab file does not exist and you create it, you have to restart MFSERV by entering `mfserv.stop` then `mfserv.start` commands (or reinstall the plugin)
- If the crontab file exists and you just change its content, you have just to wait a few seconds for the changes to be automatically taken into account.

.. tip::
    - you may use environment variable in your command surrounded with {% raw %}{{ }} {% endraw %}. Environment variables are substituted when cron is installed
    - you may use the wrapper `cronwrap.sh` in order to execute the command in the Metwork context.

.. warning::
	- Never use `crontab -e` to edit the crontab file inline.
	- Never override the crontab file by entering the command `crontab [your_crontab_file]`


If you need to execute your `cron` command in the Metwork context, you should use the cron wrapper script `${MFSERV_HOME}/bin/cronwrap.sh`, e.g. :
```cfg
{% raw %}
{{MFSERV_HOME}}/bin/cronwrap.sh --lock --low "find {{MFMODULE_RUNTIME_HOME}}/var/archive/ -type f -mtime +5 -exec rm -f {} \;" >/dev/null 2>&1

{{MFSERV_HOME}}/bin/cronwrap.sh --log-capture-to [your_log_filename] -- plugin_wrapper [your_plugin_name]  [your_sh_command]
{% endraw %}
```

Enter `cronwrap.sh --help` for more details.

.. index:: Extra daemon, daemon
## Extra daemon

You can add extra daemons which will be launched within your plugin. In order to do this, edit the `config.ini` plugin configuration file and add an `[extra_daemon_xxx]` section.
You have to provide a command to daemonize (the command must run in foreground and not daemonize by itself):
```cfg
[extra_daemon_foo]
cmd_and_args = /your/foreground/command command_arg1 command_arg2
# numprocesses=1
```
The `numprocesses` argument is the the number of processes allocated to you daemon command. The default value is 1.

Of course, you can define as many daemon as you want by adding `[extra_daemon_*]` section:
```cfg
[extra_daemon_xxx]
cmd_and_args = /your/foreground/command1 command_arg1 command_arg2

[extra_daemon_yyy]
cmd_and_args = /your/foreground/command2 command_arg1

[extra_daemon_zzz]
cmd_and_args = /your/foreground/command3

...
```

## Extra route

You may add redirection of incoming http request, you can set the `prefix_based_routing_extra_routes` in the `config.ini` file of the plugin.

For instance, let's assume you access to your application by invoking the URL http://localhost:18868/foo_nodejs, if you set `prefix_based_routing_extra_routes=/hello_from_nodejs`, this url will be also redirected to your application.

.. warning::
    | If you add extra routes, you may perhaps also change change/add routes in your code, otherwise the response of the request may be `HTTP 404 Not found`. 

.. tip:: 
    | If you have only one plugin and if you want that all incoming http requests to be routed to this plugin, you can now use '/' as an extra route in your plugin configuration.


## Access a database

A plugin can access a database through Python ORMs, like [SQLAlchemy](https://www.sqlalchemy.org/), [Records](https://github.com/kennethreitz/records), [Django ORM](https://www.djangoproject.com/), [peewee](http://docs.peewee-orm.com/), and so on.

Metwork supplies :index:`PostgreSQL`/:index:`PostGIS` database through the MFBASE storage module. If you want to easily and quickly install a Postgres database, check the :doc:`MFBASE documentation <mfbase:index>`.

.. tip::
    | If your plugin needs to access PostgreSQL database, you may have to install the corresponding Python library (e.g. `psycopg2`) and to load the layer (`scientific_core@mfext`) containing the postgreSQL binaries.
    | Don't forget to add :
    | - the Python library in the :ref:`requirements-to-freeze.txt file <plugins_guide:Python virtualenv>` file
    | - the `scientific_core@mfext` layer in the `.layerapi2_dependencies` file of your plugin


.. index:: request ID, X-Request-ID
## Disable request ID to be appeared in the logs

By default, for each HTTP request, a unique request ID is added in the  `X-Request-ID` attributes of the HTTP header. This request ID is also added into the log files.

To disable this behaviour, you just have to set to 0 the `add_request_id_header` parameter in the `config/config.ini` file configuration of the MFSERV module.

.. index:: aiohttp, middleware
## Disable middleware (asyncio, aiohttp plugins)

Thi section applies only for plugin based on [aiohttp](https://aiohttp.readthedocs.io/en/stable/web.html).

You can disable some (or all) middlewares by changing (omitting) the `middlewares` parameter in the `web.Application()` [aiohttp API](https://docs.aiohttp.org/en/stable/web_reference.html#application), e.g.:

.. seealso::
    | :ref:`mfserv_tutorials:aiohttp python plugin` tutorial


<!--
Intentional comment to prevent m2r from generating bad rst statements when the file ends with a block .. xxx ::
-->

