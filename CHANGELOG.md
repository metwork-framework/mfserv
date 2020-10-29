# CHANGELOG


## [Unreleased]

### New Features
- add a configuration option to open the endpoint /uuid to other … (#393)
- load the pythonX_scientific_core layer by default in plugins (if the layer is installed) (#389)
- fix details in documentation (including comment lines in config.ini files)
- add psycopg2 usability (by loading of optional layer python3_scientific_core@mfext)
- remove aiohttp_metwork_middlewares (now in a dedicated repository)
- allow binary packages by default (for plugins)
- new plugin system
- new plugin system
- remove all references to MFCOM or mfcom, including backward compatibility stuff
- new accept_incoming_request_id_header variable and x-forwarded-*
- add a better documented crontab file for plugins
- remove bjoern (moved to mfext and mfextaddon_python2)
- https/ssl support for nginx in mfserv (#323)
- remove absolute log paths from log_proxy usages (LOGPROXY_LOG_DIRECTORY env variable is used by default)
- port of mflog changes about syslog to node
- log refactoring
- mfserv backends refactoring
- adaptation to removal of layer misc@mfext (#284)
- improve empty plugin template and update documentation
- add a new configuration key for plugins
- add extra nginx configuration keys for empty plugins
- little improvment in socket up/down feature
- better default dependencies


### Bug Fixes
- bug with static files when extra_route is set to / (#424)
- don't prevent nginx to bind <1024 port (with setcap) (#411)
- fix graceful timeout
- fix timeout value when <=0 (#343)
- fix timeout value when <=0
- fix the nginx syslog configuration
- remove rlimit_core (because of `ulimit -c 0` in mfext)
- fix a compatibility issue with old static plugins
- fix signal_wrapper in python2
- important fix about max_age feature





