| Relative path<img width="550"/> | Description |
| --- | --- |
| **`config.ini`** | main plugin configuration file |
| **`Makefile`** | build configuration file (you probably don't need to touch this unless you have specific build directives to add to the `custom::` target) |
| `local/` | local subdirectory (it mainly holds the python virtualenv), never touch this it's automatically generated) |
| `bin/` | if you put an executable in this directory, it will be available in `PATH` (in your plugin environment) |
| `lib/` | this library directory will be available in `LD_LIBRARY_PATH` and in `PYTHONPATH` (in your plugin environment), so you can put here shared libraries or python files you want to include easily |
| `postinstall` | if this executable file is present during plugin installation, it will be automatically executed in the plugin environment just after the installation |
| `python3_virtualenv_sources/`<br>`requirements-to-freeze.txt` | main requirements file for python3 plugins (you shouldn't freeze versions here), replace `3` by `2` for python2 plugins. |
| `python3_virtualenv_sources/`<br>`requirements3.txt` | frozen requirements file for python3 plugins (generated from `requirements-to-freeze.txt` file, deleted by `make superclean`, commit this file to your VCS to freeze your dependencies), replace `3` by `2` for python2 plugins. |
| `python3_virtualenv_sources/`<br>`allow_binary_packages` | file to delete if you don't want `pip` to use binary packages (it will try to compile them during install) |
| **`.layerapi2_label`** | layerapi2 file to hold the plugin name as `plugin_{plugin name}@module_in_lowercase` |
| **`.layerapi2_dependencies`** | layerapi2 file to hold the layers to load when entering the plugin environment (you can also put some plugins with the syntax `plugin_{other plugin name}@module_in_lowercase` to inherit from another plugin |
| `.layerapi2_extra_env` | can be used to define extra environment variables in your plugin environment (see layerapi2 documentation) |
| `.autorestart_includes` | file patterns (`gitignore` syntax) scanned for changes to trigger a plugin autorestart |
| `.autorestart_excludes` | file patterns (`gitignore` syntax) to exclude for scanning (see above) |
| **`.plugin_format_version`** | version of the framework used to bootstrap the plugin (don't change this, this is used for backward compatibility) |
| `.releaseignore` | file patterns (`gitignore` syntax) to ignore in the release `.plugin` file |

> Note: mandatory files are in **bold**, all these files are not created by default (it mainly depends on the template you used) but you can create them afterwards.
