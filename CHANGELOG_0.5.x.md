# release_0.5 branch CHANGELOG



## v0.5.8 (2019-04-01)

### New Features
- remove "name" from the list of questions during plugin bootstrap






## v0.5.7 (2019-03-16)

- No interesting change


## v0.5.6 (2019-02-16)

- No interesting change


## v0.5.5 (2019-02-09)

- No interesting change


## v0.5.4 (2019-02-06)

- No interesting change


## v0.5.3 (2019-01-31)

- No interesting change


## v0.5.2 (2019-01-31)

- No interesting change


## v0.5.1 (2019-01-29)

- No interesting change


## v0.5.0 (2019-01-29)

### New Features
- first version of inotify powered conf_monitor
- provide a way for plugins to launch their own daemons
- add a plugin template for Django
- autorestart feature is configurable
- Changes in management of layer dependencies and metapackage names
- we can deactivate the nginx startup
- provide an easy way for a plugin to listen to an extra route
- execute integration tests directly from mfserv module


### Bug Fixes
- fix the node plugin template
- fix some nginx location conflicts when used with multiple apps
- more reliable nginx reload in conf_monitor
- upgrade django to version 2.1.5 to fix security vulnerability


### Performance Enhancements
- increate stats sending delay




