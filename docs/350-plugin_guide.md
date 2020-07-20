# Plugins guide

This document is about "MetWork plugins" which are available in `mfserv`, `mfdata` and `mfbase`
MetWork modules (only).

## Concepts

### What is a *plugin*?

In MetWork framework, the *plugin* is the place where you put your code.

For example with `mfserv`, if you want to develop a new webservice or website,
you develop it in a *plugin*.

A *plugin* can contain:

- some metadata (including versioning)
- one or several applications
- some custom configuration
- some base initialization
- some extra nginx configuration (in `mfserv` only)
- one or several daemons (which will be automatically launched/managed)
- some execution limits (number of files, address space...)
- a `cron` configuration
- a dedicated `virtualenv` (`python`) or `node_modules` (`nodejs`)
- [...]

You can have some "plugins dependencies" but in most cases, a *plugin* is self-contained in
a single directory called the *plugin directory* or the *plugin home*.

Everything is packaged by the framework during the *release process* in a single `.plugin` file.

### What is a *plugin template*?

A *plugin template* is just a way to start a new plugin faster. Instead of starting
your new plugin from an empty directory, you can start from a provided *plugin template*.

But of course, it is not mandatory.

!!! info
    For example, in the `mfserv` MetWork module, you will find *plugin templates* for
    boostrapping new plugins with `nodejs` or `python3 async with tornado`, `python2 with WSGI`...

The process of starting a new *plugin* from a *plugin template* is called *bootstrapping* (see workflow).

### Roles

In the classic MetWork workflow, we have two roles (of course it can be the same person):

- the developer
- the administrator

#### The developer (DEV)

The developer build *plugins* (eventually from *plugin templates*). He probably
needs internet access on his development computer.

He tests his plugin mainly in *development mode* or *devlink mode*.

Last, he releases his plugin as a single `.plugin` file.

#### The administrator (OP)

The administrator work starts with some released `.plugin` files. He installs them
with a single command (or with the provisioning feature) and optionally changes
their configuration.

On the deployment machine, no internet access is necessary because `.plugin` files
are completely self-contained (even for `virtualenv` or `node_modules`).

## The *plugin* workflow

### DEV actions

#### Bootstrapping

The *developer* can **boostrap** a *plugin* from a *plugin template*.

Use the command:

`bootstrap_plugin.py list`

to see available *plugin templates*.

To create a plugin directory from a template, use the command:

`boostrap_plugin.py create --template={template_name} {your_plugin_name}`

!!! info
    If you don't set the `--template=` option in the previous command, you will
    use the default *plugin template*.

#### Working in development mode

After bootstrapping, the *developer* can work in *development mode* (or *devlink mode*).

To install a plugin in this *development mode*, go to the plugin directory
(you must find a `Makefile` file in it) and use:

`make develop`

In this mode, the plugin is restarted automatically when the code is edited
in the plugin directory.

#### Updating the `virtualenv` or the `node_modules`

If the *developer* want to add some custom python or node libraries not included
in MetWork layers, he can add this dependency in:

- `{plugin_dir}/python3_virtualenv_src/requirements-to-freeze.txt` (for `python3` plugins)
- `{plugin_dir}/python2_virtualenv_src/requirements-to-freeze.txt` (for `python2` plugins)
- `{plugin_dir}/packages.json` (for `nodejs` plugins)

After that, use `make` in the plugin directory to rebuild the `virtualenv`.

??? question "When should I rebuild the `virtualenv`/`node_modules` manually?"
    When you install a plugin (in *normal* or *devlink* mode), the corresponding
    `virtualenv`/`node_modules` is automatically built. So you don't need to
    rebuild it manually. This operation is only required when you modify the
    `virtualenv`/`node_sources` after the installation. Just use `make` to do
    that inside the plugin directory.

??? question "What is the difference between `requirements-to-freeze.txt` and `requirements3.txt` (or `requirements2.txt`) files?"
    The second one if automatically generated (and overwritten!) from the first one (when it is more recent in terms of *last modification date*)

    **=> So don't modify `requirements3.txt` manually unless you know exactly what you're doing!**

    In the first one (`requirements-to-freeze.txt` you should describe your [PyPi](https://pypi.org/) requirements
    with the [PEP508](https://pip.pypa.io/en/stable/reference/pip_install/#requirement-specifiers) format. The idea
    is to describe only **your requirements** (probably with some flexibility in versions) and not necessary **all exact requirements**.

    Let's take an example. You want to use `Django` in your plugin. You can put `Django >= 3.0,<3.1` in `requirements-to-freeze.txt`
    to say "I want the latest Django 3.0.x package". During the virtualenv build, MetWork
    will request [PyPi](https://pypi.org/) to download your requirements (`Django` here) but
    also all requirements (recursively). In the generated `requirements3.txt`, you will find all
    requirements with exact versions. In this example, something like:
    ```
    asgiref==3.2.9
    certifi==2019.3.9
    Django==3.0.7
    lazy-import==0.2.2
    sqlparse==0.3.1
    tuna==0.4.5
    ```

    If you commit and distribute this `requirements3.txt` file, you are sure to have
    exactly these versions when you deploy on another machine (for example). But, if you delete
    this `requirements3.txt` file or if you modify the `requirements-to-freeze.txt` file (to
    add something for example), the file will be generated automatically again (potentially
    with newer versions).

    Note: same idea for `requirements2.txt` file (but for Python2 plugins)

#### Plugin env

Your plugin code runs in a *plugin env*. A *plugin env* is a bunch of `PATH`, `LD_LIBRARY_PATH`, `PYTHONPATH`, `NODE_PATH`
env var dynamic changes to run your code inside a specific environment with your specific binaries, libraries and dependencies.

With this feature, you can have a "1.0 library/dependency" running in your plugin `foo` and a "1.1 library" running in another plugin.

It's a generalization of the Python concept of [`virtualenv`](https://virtualenv.pypa.io/en/latest/).

It works for Python and NodeJS exactly in the same way. But you can also provide binaries (in any language) in the `bin/` subdirectory
of your plugin (be sure that these files are executable) or C/C++ libraries in the `lib/` subdirectory. They will be available
in the `PATH` and/or in the `LD_LIBRARY_PATH` when you are inside the *plugin_env*.

??? question "can I use pip for my Python plugins?"
    Yes, you can use `pip` command inside your *plugin env*.

    But, **be careful** : the `pip` command can change python packages in your *plugin env*
    but without reflecting these changes in the `requirements-to-freeze.txt` file. It's great
    for testing but if you want to release your plugin with its new dependencies, don't forget
    to also change the `requirements-to-freeze.txt` file!

??? question "can I use npm for my NodeJS plugins?"
    Yes, you can use `npm` command inside your *plugin env*.

When your plugin/code is executed by the MetWork framework, it's automatically run in the corresponding *plugin_env*.
But, **if you want to test things interactively in a terminal, you have to enter the plugin_env manually.**

To do that, use `plugin_env` with no argument if you are in the plugin directory or `plugin_env {the_plugin_name}` anywhere else.

!!! tip "plugin_wrapper"
    In some cases, you could want to execute a single command in a *plugin_env* (for example from a `crontab`. For this, you can use the `plugin_wrapper {plugin_name} -- command [command_args]` utility.

#### Defining configuration options

To define configuration options, add some key/values at the end of the `config.ini` file of your
plugin in the `[custom]` configuration group.

Thanks to the [library used](https://github.com/metwork-framework/opinionated_configparser), you
can also use configuration variants in this file (for different profiles of machine). See [the documentation of opinionated_configparser library]
(https://github.com/metwork-framework/opinionated_configparser/blob/master/README.md) for details about this feature (note that the *configuration name*
is set in `/etc/metwork.config` file in MetWork framework).

!!! warning
    Don't parse the `config.ini` file by yourself. This file and the plugin framework will automatically generate some environment variables from the file with the value corresponding to your configuration variant.

For example, if you have in your plugin `config.ini`:

```
[custom]
foo=value1
bar=value2
```

=> you will get two environment variables in your *plugin env*:

```
MFSERV_CURRENT_PLUGIN_CUSTOM_FOO=value1
MFSERV_CURRENT_PLUGIN_CUSTOM_BAR=value2
```

The naming schema if (of course) always the same:

```
{METWORK_MODULE}_CURRENT_PLUGIN_CUSTOM_{CONFIGURATION_KEY_IN_UPPERCASE}
```

!!! warning
    **VERY IMPORTANT**: always read the environment to get your configuration values
    as these values can be overriden with other files by an administrator
    during deployment (see further).

#### Configuring cron jobs

FIXME

#### Configuring "extra-daemons"

FIXME

#### Releasing

When the development is done, the developer can release his plugin with:

`make release`

He will get a self-contained `.plugin` file with everything needed inside.

**After that, no internet connection is needed for deploying it.**

### OP actions

#### Installing a plugin

##### Manually

To install a released plugin manually, the *administrator* use:

`plugins.install /path/to/the/dot/plugin/file.plugin`

as `mfserv/mfdata/mfbase` user (or in corresponding MetWork env for custom installations).

After that, the `.plugin` is no longer useful.

##### Automatically with the provisioning feature

To automatically install a released plugin with the provisioning feature, just put the
`.plugin` file in `/etc/metwork.config.d/mfserv/plugins/` directory (change `mfserv` by `mfdata` or `mfbase` depending on the module).

Then, restart the corresponding module by restarting the corresponding service with
your favorite system services manager or with `/etc/rc.d/init.d/metwork restart mfserv` (as root user) (change `mfserv` by `mfdata` or `mfbase` depending on the module).

#### Configuring a plugin

When a plugin is installed, some configuration options can be changed by OPs (after installation). Available keys are keys in plugin `config.ini` which don't start with underscore.

##### Manually

These keys are available in `${MFMODULE_RUNTIME_HOME}/config/plugins/{plugin_name}.ini`. So for example in `~mfserv/config/config.ini` (for a standard `MFSERV` module). By default, all keys
are commented, so standard values (defined by the developer) are used. If you want (as an OP)
to override these default values, uncomment the corresponding key in `${MFMODULE_RUNTIME_HOME}/config/plugins/{plugin_name}.ini` and change its value.

Note: this file itself can be overriden by the provisioning feature (see further).

##### Automatically with the provisioning feature

If you create a file in `/etc/metwork.config.d/mfserv/plugins/{plugin_name}.ini` (change `mfserv` by `mfdata` or `mfbase` depending on the module) with a configuration part you want to override:

For example:

```
[custom]
foo=new_value
```

to override (only) `foo` key of the `[custom]` configuration group.


### Removing a plugin

To remove a plugin, use:

```
plugins.uninstall {plugin_name}
```

!!! tip
    The plugin name is given in the first column of the `plugins.list` output.

!!! note
    If you made some changes in the `${MFMODULE_RUNTIME_HOME}/config/plugins/{plugin_name}.ini`
    configuration override file, the uninstallation process won't delete it. If you are sure
    you don't need it anymore, you can delete this file manually or add the `--clean` option
    with the `plugins.uninstall` command.

!!! note
    The uninstallation process (with or without the `--clean` option) can't delete
    the `/etc/metwork.config.d/mfserv/plugins/{plugin_name}.ini` configuration
    override root file (as this file belongs to the root account).

### Updating a plugin

To update a plugin, there is no specific command. You have to remove it. Then, reinstall it.

!!! tip
    Don't use the `--clean` option during `plugins.uninstall` to keep your configuration
    overrides.

??? tip "hotswapping with `mfserv`"
    With `mfserv`, there is another way to replace a plugin with a different
    version called "hot-swapping". This feature is a bit slow but this guarantees
    that you don't loose any HTTP request during the switch.

    Let's take an example:

    ```
    # Standard install of the foo.plugin (version 1)
    plugins.install /path/foo-1.plugin

    # [...]

    # Hotswapping the installed version 1 by the version 2 of the same plugin
    plugins.hotswap /path/foo-2.plugin
    ```

### (advanced) Installing several times the same plugin

You can't install several plugins with the same name.

But sometimes, it can be useful to install the same plugin several times. For example:

- to test a new version
- to use the same plugin but with a different configuration

If the plugin didn't hardcode its name in its code, you can use an advanced option
to install a plugin file with another name:

```
# Standard install of the foo.plugin
plugins.install /path/foo.plugin

# Install of the same plugin file but with another name
plugins.install --new-name bar /path/foo.plugin
```

!!! warning
    It can't work if the plugin hardcodes its name in its code. Developers should use `MFSERV_CURRENT_PLUGIN_NAME` or `MFDATA_CURRENT_PLUGIN_NAME` env var to avoid that.



### (advanced) Repackaging a plugin

If you have installed a plugin with another name (see above) or if you change
the configuration (as an administrator), you can be interested in producing a
new corresponding `.plugin` file (including name and configuration overrides) without
going back through the development role.

To do that, you can use:

```
plugins.repackage {name_of_the_installed_plugin}
```

And you will get a fresh new `.plugin` file.

## Plugin reference

### dev commands


{{ "cat docs/_plugin_ref_dev_commands.md"|shell() }}


### interesting files inside the plugin directory


{{ "cat docs/_plugin_ref_interesting_files.md"|shell() }}


### management commands


{{ "cat docs/_plugin_ref_management_commands.md"|shell() }}

