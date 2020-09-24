# release_1.0 CHANGELOG



## v1.0.1 (2020-09-19)

- No interesting change


## v1.0.0 (2020-09-19)

### New Features
- better default dependencies
- little improvment in socket up/down feature
- add extra nginx configuration keys for empty plugins
- add a new configuration key for plugins
- improve empty plugin template and update documentation
- adaptation to removal of layer misc@mfext (#284)
- mfserv backends refactoring
- log refactoring
- port of mflog changes about syslog to node
- remove absolute log paths from log_proxy usages (LOGPROXY_LOG_DIRECTORY env variable is used by default)
- https/ssl support for nginx in mfserv (#323)
- remove bjoern (moved to mfext and mfextaddon_python2)
- add a better documented crontab file for plugins
- new accept_incoming_request_id_header variable and x-forwarded-*
- remove all references to MFCOM or mfcom, including backward compatibility stuff
- new plugin system
- new plugin system
- allow binary packages by default (for plugins)
- remove aiohttp_metwork_middlewares (now in a dedicated repository)
- add psycopg2 usability (by loading of optional layer python3_scientific_core@mfext)
- fix details in documentation (including comment lines in config.ini files)


### Bug Fixes
- important fix about max_age feature
- fix signal_wrapper in python2
- fix a compatibility issue with old static plugins
- remove rlimit_core (because of `ulimit -c 0` in mfext)
- fix the nginx syslog configuration
- fix timeout value when <=0
- fix timeout value when <=0 (#343)
- fix graceful timeout





