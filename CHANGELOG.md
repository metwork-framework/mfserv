# CHANGELOG


## [Unreleased]

### New Features
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
- fix the nginx syslog configuration
- remove rlimit_core (because of `ulimit -c 0` in mfext)
- fix a compatibility issue with old static plugins
- fix signal_wrapper in python2
- important fix about max_age feature





