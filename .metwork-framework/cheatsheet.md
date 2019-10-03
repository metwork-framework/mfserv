# MetWork/mfserv cheatsheet

## `root` service commands

As `root` unix user:

| Command | Description |
| --- | --- |
| `service metwork start` | start all installed metwork services |
| `service metwork stop` | stop all installed metwork services |
| `service metwork status` | check all installed metwork services |

| `service metwork start mfserv` | start mfserv metwork services |
| `service metwork stop mfserv` | stop mfserv metwork services |
| `service metwork status mfserv` | check mfserv metwork services |


> Note: if you don't have `service` command on your Linux distribution, you can use `/etc/rc.d/init.d/metwork` instead of `service metwork`. For example: `/etc/rc.d/init.d/metwork start` instead of `service metwork start`. If your Linux distribution uses `systemd`component, you can also start metwork services with classic `systemctl` commands.


## root files or directories

| Path | Description |
| --- | --- |
| `/etc/metwork.config.d/mfserv/config.ini` | override the `mfdata` module configuration at system level |
| `/etc/metwork.config.d/mfserv/external_plugins/` | put some `.plugin` files here and they will be installed during `mfserv` service startup |




## module commands

As `mfserv` user:

| Command | Description |
| --- | --- |

| `mfserv.start` | start mfserv services |
| `mfserv.stop` | stop mfserv services |
| `mfserv.status` | check mfserv services |

| `layers`| FIXME |
| `components` | FIXME | 


## plugins management commands

As `mfserv` unix user:

| Command | Description |
| --- | --- |
| `plugins.list` | list installed plugins |
| `plugins.install /full/path/file.plugin` | install the given plugin file |
| `plugins.uninstall {plugin_name}` | uninstall the given plugin name |
| `plugins.info {plugin_name}` | get some informations about the given plugin name (must be installed) |
| `plugins.info /full/path/file.plugin` | get some informations about the given plugin file (does not need to be installed) |
| `plugin_env {plugin_name}` | enter (interactively) in the given plugin environment |
| `plugin_wrapper {plugin_name} {YOUR_COMMAND}` | execute the given command in the given plugin environment (without changing anything to your current environment) |



## plugins development commands

As `mfserv` unix user:

| Command | Description |
| --- | --- |
| `bootstrap_plugin.py list` | list available plugin templates |
| `bootstrap_plugin.py create --template={TEMPLATE} {PLUGIN_NAME}` | bootstrap a plugin directory `{PLUGIN_NAME}` from the given template  |

As `mfserv` unix user, inside a plugin directory (you must have a `Makefile` and `config.ini` files inside the current working directory):

| Command | Description |
| --- | --- |
| `make develop`| FIXME |
| `make release`| FIXME |
| `make`| FIXME |




FIXME:

- layer_load
- layer_unload
