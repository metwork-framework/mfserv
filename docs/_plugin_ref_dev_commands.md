| Command | Description |
| --- | --- |
| `bootstrap_plugin.py list` | list available plugin templates |
| `bootstrap_plugin.py create --template={TEMPLATE} {PLUGIN_NAME}` | bootstrap a plugin directory `{PLUGIN_NAME}` from the given template  |
| `make develop`| install the current plugin in "development mode" (devlink)  |
| `make release`| release the current plugin as a `.plugin` file |
| `make`| refresh the `virtualenv` or `node_modules` from requirements file |
| `make clean` | "clean" the current plugin and keep only "non generated" files and directories (you should commit the remaining ones to your favorite version control system) ; after that, use `make` to regenerate the `virtualenv` or `node_modules` |
| `make superclean` | same as `clean` target but also drop `requirements2.txt`, `requirements3.txt` and/or `package-lock.json` which can lead to a dependencies update (they are not frozen anymore) during next `make` call |
