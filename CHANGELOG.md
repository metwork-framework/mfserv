<a name="unreleased"></a>
## [Unreleased]

### Feat
- Changes in management of layer dependencies and metapackage names (only minimal and full) Associated with changes in mfext _metwork.spec, this reduces the number of layers installed by default when installing mfserv (only necessary mfext layers are installed) Metapackage metwork-mfserv-minimal only installs the necessary layers for mfserv to work properly Metapackage metwork-mfserv or metwork-mfserv-full installs all mfserv layers
- add a plugin template for Django
- autorestart feature is configurable
- execute integration tests directly from mfserv module and lauch them on a pull request on the module
- first version of inotify powered conf_monitor
- provide a way for plugins to launch their own daemons
- provide an easy way for a plugin to listen to an extra route
- we can deactivate the nginx startup

### Fix
- fix some nginx location conflicts when used with multiple apps
- fix the node plugin template
- more reliable nginx reload in conf_monitor
- upgrade django to version 2.1.5 to fix security vulnerability

### Perf
- increate stats sending delay

<a name="v0.4.1"></a>
## [v0.4.1] - 2019-01-09

<a name="v0.4.0"></a>
## [v0.4.0] - 2019-01-08
### Feat
- Add static plugin type and corresponding template
- add a redis_service option
- add an internal welcome plugin
- add plugin app directory into lua_package_path
- aiohttp upgrade (now 3.4.4)
- better plugin crontab example
- change default configuration
- delete "blank only" files during bootstrap
- filter gunicorn messages in stdout/stderr depending on their level
- introduce an empty plugin type
- provide a better plugin crontab bootstrap
- publish MFSERV environment variables into nginx environment
- remove crontab support useless choice while bootstrapping static plugin

### Fix
- add missing file for node plugin template
- better plugin routing
- don't start plugins during installation or uninstallation
- fix lua lib paths
- fix timeout issues around conf_monitor restarts
- handle NOTSET logging level value in nginx configuration

### BREAKING CHANGE

no admin module configured by default

