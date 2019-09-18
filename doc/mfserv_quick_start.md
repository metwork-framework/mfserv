# Quick Start

## Activate the MFSERV environment

One of the first thing, you have to do is to load the "MFSERV environment" in your shell session. There are several ways to do that: check :doc:`the related documentation <../mfserv_load_env>`.

In this tutorial, follow :ref:`this way <activate_mfserv_user>`, i.e. log in as the `mfserv` user.

## Create your first plugin

**This step will teach you how to create, run, release and deploy a simple MFSERV plugin with a MFSERV template.**

We are going to create a plugin with the :ref:`default template <mfserv_create_plugins_the_default_template>` implementing a simple WSGI `hello-world` web applications (type :ref:`python3_sync <mfserv_create_plugins_python3_sync>`) . We will called it **foo_default**.

If it's the first time you log in as mfserv, you have to set a password before (`passwd mfserv` or `sudo passwd mfserv`).


### Create the plugin

First, list the available templates, see :ref:`plugin templates <mfserv_create_plugins:Plugin templates>`.

Use the :ref:`default template <mfserv_create_plugins_the_default_template>` template to create the plugin : run the following command:
```bash
bootstrap_plugin.py create --template=default foo_default
```

or you can omit the `--template` parameter, in this case the the :ref:`default template <mfserv_create_plugins_the_default_template>` template will be used:

```bash
bootstrap_plugin.py create foo_default
```
Once you have entered this command, you will be asked to fill in some fields to configure and customize your plugin: for now, press `[ENTER]` to set the default value, you will be able to modify your plugin configuration anytime later. 

The `/home/mfserv` directory now contains a `foo_default` sub-directory with files:

> config.ini: configuration file of the plugin  
Makefile: directives to build the plugin   
main/\_\_init\_\_.py: package initialization file (may be empty, but file must exist so that the package to be found)    
main/wsgi.py: python entry point of the application 


You may check the `config.ini` file of the plugin, especially :
- the `[app_main]` section:

    - type: type of the plugin (ideally, this setting may not be changed)

    ```cfg
    [app_main]
    type=python3_sync
    ```

    - timeout:

    ```cfg
    [app_main]
    type=python3_sync
    # timeout (in seconds) for one request
    # (if null or <=0, the MFSERV_NGINX_TIMEOUT is used)
    timeout=0
    ```
    - main_arg: the entry point of the application,e.g. `main.wsgi:application` means the entry point is the `application` function defined in the `wsgi.py` script of the `main` python package.
    
    ```cfg
    # main arg (module.submodule:application_function)
    # (for example, with regular mfserv plugin, if you set here a value like "
    # "main.application:app", then "app" must be a WSGI function available in
    # "application.py" file in "main" directory (this directory must have a
    # "__init__.py" file to be considered as a module)
    main_arg = main.wsgi:application
    ```

    - debug: check also :ref:`Interactive debugger section <mfserv_debug_plugin:Interactive debugger>`
         
    ```cfg    
    # if you set debug=1, then you will get an interactive debugger
    # when you got an exception in your code
    # (max age will also be automatically set to 0 and mflog minimal level will be
    #  set to DEBUG)
    # DON'T USE IT ON PRODUCTION!!!
    debug=0
    ```
    - resource limits: see :ref:`mfserv_tuning_monitoring:Resource limits`            


- the `[extra_daemon_xxx]` section: see :ref:`mfserv_miscellaneous:Extra daemon`.

.. tip::
	Every time you change the plugin configuration, this configuration will be always automatically reloaded.

Let's now **install (as dev build)** the plugin by entering the command (from the `foo_default` plugin directory):

```bash
make develop
```

Check the plugin is installed:

```bash
plugins.list
```

You should show the plugin is installed as dev build, i.e. `dev_link`
{% raw %}
    ┌Installed plugins (2)─────────────────┬──────────┬────────────────────────────────────────┐    
    │ Name          │ Version              │ Release  │ Home                                   │    
    ├───────────────┼──────────────────────┼──────────┼────────────────────────────────────────┤    
    │ welcome       │ master.ci295.ea4af67 │ 1        │ /home/mfserv/var/plugins/welcome       │    
    │ foo_default   │ dev_link             │ dev_link │ /home/mfserv/var/plugins/foo_default   │    
    └───────────────┴──────────────────────┴──────────┴────────────────────────────────────────┘    
{% endraw %}


Now we will see how to add specific configuration to our application. Let's assume we want to add a configurable link to our main page. We will add this parameter in the `config/config.ini` file of the MFSERV module (:ref:`read more about this purpose <mfserv_create_plugins:Custom plugin configuration>`).

Edit the `config/config.ini` file and add the following line at the end:
```cfg
[plugin_foo_default]
my_url=https://medium.com/metwork-framework
```


Edit and change the `main/wsgi.py` script as follows:
```python

import os

from mflog import get_logger

logger = get_logger("myapp")


def application(environ, start_response):
    my_url = os.environ.get("MFSERV_PLUGIN_FOO_DEFAULT_MY_URL", "")

    status = '200 OK'
    output = '<h1>Hello World!</h1>'
    if my_url != "":
        output = '{}</br></br><a href="{}">Visit Metwork Framework blog</a>'.format(output, my_url)
    logger.info("this is a test message")
    response_headers = [('Content-Type', 'text/html; charset=utf-8'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output.encode('utf-8')]

```
Build the plugin:
```bash
make develop
```

Restart MFSERV in order to reload the new configuration (`~/config/config.ini` MFSERV configuration file)
```bash
mfserv.stop;mfserv.start
```

.. seealso::
    | :doc:`../configure_a_metwork_package`.
    | :ref:`mfserv_create_plugins:Custom plugin configuration`

### Run the plugin

From a web browser, enter the url of your application: `http://localhost:18868/foo_default` or  `http://{remote_host}:18868/foo_default`. A 'Hello World!.' HTML page with a link to `my_url` should be displayed.

.. note::
    | Because your application is named `main`  you don't need to specify the application name in the url. `http://localhost:18868/foo_default` and `http://localhost:18868/foo_default/main` do the same.
    
You can check the plugin log files. Log files are stored in the `${HOME}/log` directory:
- app_foo_default_main_worker`n`.stdout (`n` depends on the numbers of workers defined in the `config.ini` file of you plugin (see :ref:`MFSERV log section <mfserv_log:Default logs files>`):

>2019-07-02T16:22:16.730181Z     [INFO] (myapp#26959) this is a test message {request_id=1bee1c4ce15ee370e98fb64285f9bfa6}


You will notice the `request_id` is automatically logged: see  :ref:`mfserv_miscellaneous:Disable request ID to be appeared in the logs`

- app_foo_default_main_worker`n`.stdout: empty

You mays also check the `nginx_access.log` file ((Nginx information messages, in JSON format) and `nginx_error.log` (Nginx general error messages).

### Release the plugin

We will now release the `foo_default` plugin (considering it as a stable version). Releasing a plugin makes it production-ready, ready to be deployed.

To do this, go to the `foo_default` plugin directory and enter the command:
```bash
make release
```

This will create a `.plugin` file that will be used to deploy the plugin, e.g. `foo_default-[version]-1.metwork.mfserv.plugin` where `[version]` is the value of the `version` parameter of the move_image `config.ini` you enter when you create the plugin (default value is `${MFMODULE_VERSION}`). You may change it:
```cfg
# Version of the plugin (X.Y.Z)
# If the value is [MFMODULE_VERSION],
# the current module version is used
version=1.0.0
```

### Deploy the plugin

Let's now deploy the `foo_default` plugin on a production environment.

**Prerequisites**:

- Metwork have to be installed on this environment (at least MFSERV and its dependencies MFEXT and MFCOM).
- You be logged in as mfserv user

In order to deploy the plugin on a production environment,  put down the `foo_default-[version]-1.metwork.mfserv.plugin` in a directory on this target environment, e.g. `/home/mfserv/released_plugins`

.. note::
    for this tutorial, if your production environment is the same as your development environment, you have to uninstall the `foo_default` plugin which is already installed (by the `make develop` command). To uninstall the plugin, enter:

```bash
plugins.uninstall foo_default
```

Then, check the `foo_default` plugin is no longer installed, enter:

```bash
plugins.list
```

You should not show the `foo_default` plugin
{% raw %}
    ┌Installed plugins (1)─────────────────┬──────────┬────────────────────────────────────────┐    
    │ Name          │ Version              │ Release  │ Home                                   │    
    ├───────────────┼──────────────────────┼──────────┼────────────────────────────────────────┤    
    │ welcome       │ master.ci295.ea4af67 │ 1        │ /home/mfserv/var/plugins/welcome       │    
    └───────────────┴──────────────────────┴──────────┴────────────────────────────────────────┘    
{% endraw %}
   


Let's now install the plugin on the production environment, enter:

```bash
plugins.install /home/mfserv/released_plugins/foo_default-1.0.0-1.metwork.mfserv.plugin
```

Then, check the `foo_default` plugin is installed, enter:

```bash
plugins.list
```

{% raw %}
    ┌Installed plugins (2)─────────────────┬──────────┬────────────────────────────────────────┐    
    │ Name          │ Version              │ Release  │ Home                                   │    
    ├───────────────┼──────────────────────┼──────────┼────────────────────────────────────────┤    
    │ welcome       │ master.ci295.ea4af67 │ 1        │ /home/mfserv/var/plugins/welcome       │    
    │ foo_default   │ 1.0.0                │ 1        │ /home/mfserv/var/plugins/foo_default   │    
    └───────────────┴──────────────────────┴──────────┴────────────────────────────────────────┘    
{% endraw %}


In practice, the plugins are installed in the `${HOME}/var/plugins` directory.

.. tip::
	Another way to install the MFSERV `foo_default` plugin in a production environment is to put down the `.plugin` file into `/etc/metwork.config.d/mfserv/external_plugins` directory. Then to install the plugin, you just restart the MFSERV service by entering `service metwork restart mfdata` command (as root user).
	Check :doc:`mfserv_deploy_plugin`.


<!--
Intentional comment to prevent m2r from generating bad rst statements when the file ends with a block .. xxx ::
-->
