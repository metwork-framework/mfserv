# Release and Deploy a plugin
.. index:: release a plugin
## Release a plugin

Releasing a plugin consists in keeping all the plugin related files together in one `.plugin`file and makes the plugin production-ready, ready to be deployed.

In order to release a plugin, go to the plugin directory and enter the run the following command from the root directory of the plugin:
```bash
make release
```

Then a `{plugin name}-{version}-1.metwork.mfserv.plugin` file is created, where:

- {plugin name} is the name of the plugin
- `{version}` is the value of the `version` parameter defined in the plugin `config.ini` file you enter when you create the plugin (default value is `${MFMODULE_VERSION}`)
 

You can change the `version` in  plugin `config.ini` file:
```cfg
# Version of the plugin (X.Y.Z)
# If the value is [MFMODULE_VERSION],
# the current module version is used
version=1.0.0
```

.. index:: deploy a plugin
## Deploy a plugin in a production environment

In order to deploy a plugin in a production environment:

- Metwork have to be installed on this environment (at least MFSERV and its dependencies MFEXT).
- the plugin you want to deploy have to be 'released' in a `.plugin` file (refer to [Release a plugin](#release-a-plugin))

### The 'basic' way

**You be logged in as** `{METWORK_MODULE}` **user, e.g.** `mfserv` **user.**

In order to deploy the plugin on a production environment,  put down the `.plugin` file in a directory on this target environment, e.g. `~/released_plugins`


Then, install the plugin by entering:

```bash
plugins.install ~/released_plugins/{your_plugin_released}.plugin
```
Then, check the plugin is installed, enter:

```bash
plugins.list
```

In practice, the plugins are installed in the `~/var/plugins` directory.


### The 'well-done' way

** This is the recommended way to deploy a plugin in a production environment**

**You be logged in as** `root` **user.**

In order to deploy the plugin on a production environment,  put down the `.plugin` file  into `/etc/metwork.config.d/mfserv/external_plugins` directory.

Then to install the plugin, you just restart the `{METWORK MODULE}` service by entering `service metwork restart {METWORK MODULE}` command, e.g.  `service metwork restart mfserv`.

```
Then, check the plugin is installed, enter the command `su --command="plugins.list" - {METWORK MODULE}`, e.g.:

```bash
su --command="plugins.list" - mfserv
```
## Override a plugin configuration

Refer to :ref:`configure_a_metwork_package:How to configure plugins during production deployment process ?` section.
