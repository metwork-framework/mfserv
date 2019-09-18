
# How to create custom plugins
In order to use MFSERV and create your custom plugin, one of the first thing, you have to load the "MFSERV environment" in your shell session. There are several ways to do that: check :doc:`the related documentation <mfserv_load_env>`.

Plugins can be custom made quickly and easily by using existing templates. Making plugins with mfserv is as simple as editing a configuration file. You just have to create a plugin using an existing template, then edit the configuration file so that the plugin fulfills your need, and finally release the plugin. 

Predefined templates are available in order to create your plugin (see [Plugin templates section](#plugin-templates)).

## Create and customize the plugin
To create a plugin, simply **run the command**.
```bash
bootstrap_plugin.py create --template={TEMPLATE} {PLUGIN_NAME}
```
where `{TEMPLATE}` is the tmplate you want to use and `{PLUGIN_NAME}` the name of ypur plugin.

Notice if you omit the `--template` argument, [the default template](#id1) will be used.

Once you have entered this command, you will be asked to fill in some fields to configure and customize your plugin. 
You can also configure your plugin anytime by **editing the** `mfserv/{PLUGIN_NAME}/config.ini` **config file**. For more details about each field, check the documentation in the `mfserv/{PLUGIN_NAME}/config.ini` file.


:doc:`mfserv_quick_start`  and :doc:`mfserv_tutorials` may help you to create your plugin.


## Custom plugin configuration

You may need to customize the :index:configuration of your plugin (application). In order to do this, set your parameter(s) in the MFSERV module configuration file `config/config.ini`. This configuration file can contain a section per plugin. The section must be named `[plugin_{plugin_name}]`.

Each parameter will be will transform into an environment variable whose pattern is `{MFMODULE}_{SECTION_NAME}_{PARAMETER_NAME}`.

.. note::
    - Environment variables are always in uppercase.
    - To get the new value, you have to close/reopen your terminal to force a new profile loading.
    - To change daemons and services behaviour (like `nginx` listening port in your example), you have to restart services from a newly restarted terminal or from a `root` user through `service metwork restart` command.

For more details, see :doc:`../configure_a_metwork_package`.


.. index:: plugin templates, templates
## Plugin templates

Predefined templates are available in order to create your plugin.

The following command allows to display the available templates:
```bash
bootstrap_plugin.py list
```

```
List of available plugin templates:
     * default
     * empty
     * node
     * django
     * static  
     * flask  
```

.. index:: default template, python3_sync, python2_sync, aiohttp
.. _mfserv_create_plugins_the_default_template:
### The `default` template

This template allows you to create either a Python WSGI web server (synchronous/standard web server) or a Python asynchronous/asyncio web server.

When you create a plugin with this template, we will asked what kind (type) of plugin to create:

.. _mfserv_create_plugins_python3_sync:
- **python3_sync**: for synchronous/standard web Python3 applications (implemented with the ["new way"](https://medium.com/metwork-framework/a-new-way-to-serve-python-web-apps-d5662ab69dc0))
- **python2_sync**: for synchronous/standard web Python2 applications (implemented with the ["new way"](https://medium.com/metwork-framework/a-new-way-to-serve-python-web-apps-d5662ab69dc0))
.. _mfserv_create_plugins_aiohttp_sync
- **aiohttp**: for asynchronous Python3/asyncio web applications (implemented with the ["new way"](https://medium.com/metwork-framework/a-new-way-to-serve-python-web-apps-d5662ab69dc0) with the [aiohttp framework](https://aiohttp.readthedocs.io/))
- **gunicorn3_sync**: for synchronous/standard web Python3 applications (implemented with the ["old way"](https://medium.com/metwork-framework/a-new-way-to-serve-python-web-apps-d5662ab69dc0))
- **gunicorn2_sync**: for synchronous/standard web Python2 applications (implemented with the ["old way"](https://medium.com/metwork-framework/a-new-way-to-serve-python-web-apps-d5662ab69dc0))
- **gunicorn3_asyncio**: for asynchronous Python3/asyncio applications (implemented with the ["old way"](https://medium.com/metwork-framework/a-new-way-to-serve-python-web-apps-d5662ab69dc0))

.. index:: deprecated, gunicorn_arg, debug
.. note::
    | The `gunicorn` implementation ("old way") will be **deprecated** in the future.
    | `gunicorn_arg` parameter is **deprecated** in `config.ini` file of the plugin (it works but you will get a warning, just change the parameter name to `main_arg` to fix that).

.. tip::
    | For **python3_sync**, **python2_sync** and **aiohttp** choices, you will find the following features in the `config.ini` file of your plugin:
    | `timeout`: the timeout (in seconds) for one request
    | `max_age`: if set, then the process will be restarted sometime after max_age and max_age + random(0, max_age) seconds (this is great to avoid leaks in badly written code)
    | `debug`: if you set debug=1, then you will get an **interactive debugger** in your browser when you got an exception in your code and mflog minimal level will be set to DEBUG. See :ref:`Interactive debugger section <mfserv_debug_plugin:Interactive debugger>`

.. note::
    | If you have created an MFSERV plugin with MetwWork version < 0.7, all these new features won’t be available. 
    | To take advantage of these new features, create a new plugin with MetWork version >= 0.7 and migrate your code inside (it’s easy). Of course, this is not mandatory.

.. seealso::
    | `A new way to serve (python) web apps article <https://medium.com/metwork-framework/a-new-way-to-serve-python-web-apps-d5662ab69dc0>`_

.. index:: Django template, postinstall
.. _mfserv_create_plugins_the_django_template:
### The `django` template

The `django` plugin template enables you to initialize a plugin containing a single rough :index:`Django` project and a first `Hello World!` application in this project.

One your plugin is initialized, you will have a python virtual environment containing a collection of modules, including Django.

The Django version provided by MetWork can be check in the `python3_virtualenv_sources/requirements-to-freeze.txt` file in the plugin directory. You can change it if needed.

.. important::
    | Since MetWork MFSERV version 0.7:
    | - This template works with Python3 only
    | - This template is limited to a single “django project” in a plugin (of course, you can still have multiple “django applications” in your plugin)
    | - This template provides a default `SQLITE <https://www.sqlite.org/index.html>`_ file. If you want to use a `PostgreSQL <http://postgresql.org/>`_ database or other :ref:`database engines <mfserv_miscellaneous:Access a database>`, you have to configure it by yourself (it is not difficult), please read `Django databases documentation <https://docs.djangoproject.com/en/stable/ref/databases/>`_
    |
    | Of course, Django plugins bootstrapped with the old plugin template (MetWork MFSERV version < 0.7) will continue to work. These changes are only for new plugins.


The :index:`Django secret key` of your first project is randomly generated during the  process. Your project will own a secret key similar to the one that is set when you
create a new Django project with the Django command `django-admin startproject` (see [Django secret key documentation](https://docs.djangoproject.com/en/stable/ref/settings/#std:setting-SECRET_KEY)).

Once you bootstrapped a plugin with the Django template, a **postinstall** script is create in the plugin directory. It is executed when you launch the `make develop` or `plugins.install` command. 
    
The **postinstall** script do the following:
- Create the Django project `django-admin startproject {PLUGIN_NAME}` (see [django-admin startproject documentation](https://docs.djangoproject.com/en/stable/ref/django-admin/#startproject))
- Create the "Hello World!" application `django-admin startapp hello` (see [django-admin startapp documentation](https://docs.djangoproject.com/en/stable/ref/django-admin/#startapp))
- Configure the project 
- Run `python manage.py migrate` (see [Django migrate documentation](https://docs.djangoproject.com/en/stable/ref/django-admin/#django-admin-migrate))
- Run `python manage.py collectstatic` (see [Django collectstatic documentation](https://docs.djangoproject.com/en/stable/ref/contrib/staticfiles/#collectstatic))

You may modify **postinstall** script, for example if you want to do the same for other Django projects inside your plugin.
 
.. note::
    | The **postinstall** script does not run `python manage.py createsuperuser`. You have to run the command by yourself if you want to create a superuser (see [Django createsuperuser documentation](https://docs.djangoproject.com/en/stable/ref/django-admin/#createsuperuser)).

.. danger::
    | Each time the **postinstall** script is executed, it remove project directories. 
    | **It's highly recommended** to rename (or delete) this script otherwise you will loose source and code you added or changed if you build again or install the plugin.
    
.. important::
    | Django has a security :index:`ALLOWED_HOSTS` parameter in order to prevent HTTP Host header attacks.
    | By default, the template set ALLOWED_HOSTS=['localhost', '127.0.0.1', '[::1]']. You will definitely need to change this setting. In order to do this, change it:
    | - either in the **postinstall** script file before building the plugin:
    |       cat >>foo_django/settings.py <<EOF
    |   ...
    |       # ADDED BY METWORK/MFSERV/DJANGO PLUGIN TEMPLATE
    |       # TO PROVIDE DEBUG FEATURE
    |       DEBUG = (os.environ.get('MFSERV_CURRENT_PLUGIN_DEBUG', '0') == '1')
    |       import mflog
    |       if DEBUG:
    |           mflog.set_config(minimal_level="DEBUG")
    |       else:
    |           mflog.set_config()
    |       
    |       **ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']**
    |       EOF
    |   ...
    |
    | - or in the **settings.py** Django python configuration file after building the plugin:
    |   ...
    |       # ADDED BY METWORK/MFSERV/DJANGO PLUGIN TEMPLATE
    |       # TO PROVIDE DEBUG FEATURE
    |       DEBUG = (os.environ.get('MFSERV_CURRENT_PLUGIN_DEBUG', '0') == '1')
    |       import mflog
    |       if DEBUG:
    |           mflog.set_config(minimal_level="DEBUG")
    |       else:
    |           mflog.set_config()
    |       
    |       **ALLOWED_HOSTS = ['localhost', '127.0.0.1', '[::1]']**
    |   ...
    |
    | For further details about ALLOWED_HOSTS, see `Django documentation <https://docs.djangoproject.com/en/stable/ref/settings/#allowed-hosts>`_


.. seealso::
    | :ref:`mfserv_tutorials:Django project plugin` tutorial

.. index:: Flask template, Jinja2
.. _mfserv_create_plugins_the_flask_template:
### The `flask` template

The `flask` plugin template allows you to create a Python WSGI web server through the [Flask framework](http://flask.pocoo.org/).

One your plugin is initialized, you will have a python virtual environment containing a collection of modules, including Flask and Jinja2.

.. important::
    This template works with Python3 only

The Flask version provided by MetWork can be check in the `python3_virtualenv_sources/requirements-to-freeze.txt` file in the plugin directory. You can change it if needed.

.. seealso::
    :ref:`Flask plugin tutorial <mfserv_tutorials:Flask plugin>`.

.. index:: Node.js template, node template
.. _mfserv_create_plugins_the_node_template:
### The `node` template

This template allows you to create a [Node.js](https://nodejs.org/) server plugin through the [Express web application framework](https://expressjs.com/).

.. seealso::
    | :ref:`MFSERV Layer nodejs <layer_nodejs>` documentation
    | :ref:`Node.js version <mfext:layer_nodejs:packages>` provided by MetWork.
    | :ref:`Node.js plugin tutorial <mfserv_tutorials:Node.js plugin>`.

.. _mfserv_create_plugins_the_static_template:
### The `static` template

This template allows you to create a static website plugin.

The template generate an `main` directory with just contains a `index.html`. Then, you have to create your static files.

.. _mfserv_create_plugins_the_empty_template:
### The `empty` template

This template is a special template that must be used as a container e.g. a crontab container (by selecting `crontab_support=yes`) or one or more daemons (it doesn't create any web application)

If you need to only run daemon(s), you have to configure an `[extra_daemon_xxx] per daemon in the `config.ini` file in the plugin directory.

.. seealso::
    | :ref:`mfserv_miscellaneous:Extra daemon` section
    | :ref:`mfserv_crontab_support` section




<!--
Intentional comment to prevent m2r from generating bad rst statements when the file ends with a block .. xxx ::
-->    
