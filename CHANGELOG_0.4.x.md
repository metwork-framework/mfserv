# release_0.4 branch CHANGELOG



## v0.4.1 (2019-01-09)

- No interesting change


## v0.4.0 (2019-01-08)

### New Features
- change default configuration
- add a redis_service option
- add plugin app directory into lua_package_path
- delete "blank only" files during bootstrap
- introduce an empty plugin type
- provide a better plugin crontab bootstrap
- better plugin crontab example
- aiohttp upgrade (now 3.4.4)
- Add static plugin type and corresponding template
- filter gunicorn messages in stdout/stderr depending on their level
- add an internal welcome plugin
- remove crontab support useless choice
- publish MFSERV environment variables into nginx environment


### Bug Fixes
- better plugin routing
- fix lua lib paths
- fix timeout issues around conf_monitor restarts
- handle NOTSET logging level value in nginx configuration
- add missing file for node plugin template
- don't start plugins during installation or uninstallation





