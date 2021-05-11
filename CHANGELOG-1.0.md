# release_1.0 CHANGELOG

## v1.0.14 (2021-05-10)

### Bug Fixes

- fix a plugin context issue (backport #495) (#496)

## v1.0.13 (2021-04-28)

### Bug Fixes

- fix nginx root usage in some CI corner cases (backport #484) (#486)

## v1.0.12 (2021-02-11)

### Bug Fixes

- fix some stop/start issues (bp #475) (#479)

## v1.0.11 (2021-01-29)

### Bug Fixes

- fix concurrency issue about max_age (and max_age=0 now by default) (bp #477) (#478)

## v1.0.10 (2021-01-26)

- No interesting change

## v1.0.9 (2021-01-08)

### Bug Fixes

- fix error message in nginx error log (bp #473) (#474)

## v1.0.8 (2020-12-02)

### Bug Fixes

- fix potential lua collisions between mutiple openresty plugins (bp #451) (#458)

## v1.0.7 (2020-12-01)

- No interesting change

## v1.0.6 (2020-11-30)

### Bug Fixes

- fix virtualhosting usage (bp #456) (#457)

## v1.0.5 (2020-11-28)

### Bug Fixes

- avoid lua collisions with multiple openresty plugins (bp #447) (#448)
- fix static files routing with virtualhost (bp #452) (#453)

## v1.0.4 (2020-11-03)

### Bug Fixes

- fix bad comment in boostrapped config.ini for plugins (bp #435) (#437)

## v1.0.3 (2020-10-28)

### Bug Fixes

- don't prevent nginx to bind <1024 port (with setcap) (bp #411) (#413)
- bug with static files when extra_route is set to / (bp #424) (#428)

## v1.0.2 (2020-09-26)

### New Features

- load the pythonX_scientific_core layer by default in plugins (if the layer is installed) (bp #389) (#390)
- add a configuration option to open the endpoint /uuid to other … (bp #393) (#395)

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

## v1.0.1 (2020-09-19)

- No interesting change


