| Command | Description |
| --- | --- |
| `plugins.list` | list installed plugins |
| `plugins.install {/full/path/file.plugin}` | install the given plugin file |
| `plugins.uninstall {plugin_name}` | uninstall the given plugin name (the "plugin name" is given in the first column of the `plugins.list` output) |
| `plugins.info {plugin_name}` | get some informations about the given plugin name (must be installed) |
| `plugins.info {/full/path/file.plugin}` | get some informations about the given plugin file (does not need to be installed) |
| `plugin_env {plugin_name}` | enter (interactively) in the given plugin environment |
| `plugin_wrapper {plugin_name} {YOUR_COMMAND}` | execute the given command in the given plugin environment (without changing anything to your current environment), useful for cron jobs |
