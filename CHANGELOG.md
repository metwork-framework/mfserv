<a name="unreleased"></a>
## [Unreleased]

### Feat
- first version of inotify powered conf_monitor
- provide a way for plugins to launch their own daemons

### Fix
- fix the node plugin template

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

