# Plugins guide

[//]: # (automatically generated from https://github.com/metwork-framework/resources/blob/master/cookiecutter/_%7B%7Bcookiecutter.repo%7D%7D/.metwork-framework/plugins_guide.md)

## Plugins Configuration
A plugin has its own configuration in `config.ini` file stored in the root directory of the plugin.

This `config.ini` file is created with its requisite configuration during the `bootstrap_plugin.py create` command.

You can change some of the configuration parameters and/or add configuration specific to your plugin.

Every time you change the configuration file, you have to stop and start the Metwork module to reload the configuration, by entering the commands :

- either
```bash
{MODULE_RUNTIME_HOME}.stop
{MODULE_RUNTIME_HOME}.start
```
- or (as root user)
```bash
service metwork restart {MODULE_RUNTIME_HOME}
```

with {MODULE_RUNTIME_HOME} the Metwork module you are working with, e.g. mfdata.

The configuration parameters are described and explained in the `${MODULE_RUNTIME_HOME}/config/config.ini` file.

## Plugins Commands

This section sums up all the commands you will need to build, install a plugin.

Use `-h` or `--help` option of the command to review all available options of the command.

### `plugins.list`

List installed plugins.
```bash
plugins.list [options]
```

Note: if you have a version named `dev_link`, the plugin is installed as a symbolic link to a source directory. 
It's a kind of "development mode".


### `plugins.install`

Install a given plugin from a `.plugin` file.
```bash
plugins.install {plugin file path} [options]
```

### `plugins.uninstall`

Uninstall a given plugin **name** (not file). The name corresponds to the first column of `plugins.list` output.
```bash
plugins.uninstall {plugin name} [options]
```

### `plugins.info`

Get more infomation about a  plugin.
```bash
plugins.info {plugin_name}
```

### `plugin_env`

If you have a virtualenv in your plugin or if you want to simulate the exact environment your code will run in the context of your plugin, you can use the `plugin_env` interactive command.

If you are developping, the best way is to go in the root directory of your plugin and use `plugin_env` without argument.

If you have a "normal" installed plugin, you can use `plugin_env {PLUGIN_NAME}`.

When you are inside a plugin environment, you will find some extra environment variables:
```bash
env | grep "^${MODULE}_" | grep CURRENT
```

```
MFDATA_CURRENT_PLUGIN_NAME=my_plugin
MFDATA_CURRENT_PLUGIN_DIR=/home/mfdata/var/plugins/my_plugin
MFDATA_CURRENT_PLUGIN_LABEL=plugin_my_plugin@mfdata
```

And of course, paths of your plugin "layer" (kind of virtualenv generalization) are loaded before system paths.

### `plugin_wrapper`

This command follows the same idea than `plugin_env` but in a non-interactive way. Use it for example for `crontabs` or if you want to execute a command in a given plugin environment without changing anything to the current shell.

```bash
plugin_wrapper {PLUGIN_NAME} {COMMAND} [{COMMAND_ARG1}] [{COMMAND_ARG2}] [...]
```

Note: the plugin {PLUGIN_NAME} must be installed.

## Make Commands

### make develop

Install your plugin in "development mode" (you don't need to release and install each time you make a modification), the plugin installed through a symlink.
```bash
make develop
```

### make release

Release your plugin as a `.plugin` file.
```bash
make release
```

### make clean

Clean (before release)
```bash
make clean
```

### make superclean

Hard-clean, can be useful when you have error with your virtualenv
```bash
make superclean
```

### make

Build your virtualenv from sources
```bash
make
```
## Python virtualenv

When developing Python applications, it’s standard practice to have a `requirements.txt` file.

This file can be used in different ways, and typically takes one of these two forms:

- Simple requirements: A list of top-level dependencies a plugin has, often without versions specified.
- Exact requirements: A complete list of all dependencies a plugin has, each with exact versions specified.

### The 'Simple' requirements

A list of **top-level dependencies** a plugin has, often without versions specified.

The `requirements.txt` looks like:
```cfg
requests[security]
flask
gunicorn==19.4.5
```
When a `requirements.txt` file like above is used to deploy in production environment, unexpected consequences can occur. Effectively, because versions haven’t been pinned, running `pip install` will give you different results today than it will tomorrow.

This is rather a bad way. As different versions of sub-dependencies are released, the result of a fresh `pip install -r requirements.txt` will result in different packages being installed, and potentially, your application failing for unknown and hidden reasons.

### The 'Exact' Requirements

A complete list of **all dependencies** a plugin has, each with exact package versions specified.

The `requirements.txt` looks like:
```cfg
cffi==1.5.2
cryptography==1.2.2
enum34==1.1.2
Flask==0.10.1
gunicorn==19.4.5
idna==2.0
ipaddress==1.0.16
itsdangerous==0.24
Jinja2==2.8
MarkupSafe==0.23
ndg-httpsclient==0.4.0
pyasn1==0.1.9
pycparser==2.14
pyOpenSSL==0.15.1
requests==2.9.1
six==1.10.0
Werkzeug==0.11.4
```

This is a best-practice for deploying applications, and ensures an explicit runtime environment with deterministic builds.

All dependencies, including sub-dependencies, are listed, each with an exact version specified.

While the this method for requirements.txt is best practice, it is a bit cumbersome. Namely, if you want to upgrade some or all of the packages, it's not so easy to do.

### The 'Best' Requirements

The best an simple way is to have two requirements file instead of having one:

- requirements-to-freeze.txt
- requirements.txt


The `requirements-to-freeze.txt` uses 'simple' requirements', and is used to specify the top-level dependencies, and any explicit versions you need to specify.

the `requirements.txt` uses 'exact' requirements, and contains the output of a `pip freeze` after `pip install requirements-to-freeze.txt` has been run.

Working with Metwork plugin, you just need to fill the `requirements-to-freeze.txt` file. Then, when building/releasing the plugin, the `requirements.txt` will be generated.

Depending on which python version (python2 or python3) you are working with, the `requirements.txt` file will be named, respectively  `requirements2.txt` and `requirements3.txt`

### Python3 requirements-to-freeze.txt

If you are working with python3, an empty `requirements-to-freeze.txt` is created in the `python3_virtualenv_sources` plugin directory (during the `bootstrap_plugin.py create` command)

Add your python3 dependencies inside this file (with or without package version)


### Python2 requirements-to-freeze.txt

If you are working with python2, an empty `requirements-to-freeze.txt` is created in the `python2_virtualenv_sources` plugin directory (during the `bootstrap_plugin.py` create command)

Add your python2 dependencies inside this file (with or without package version)






