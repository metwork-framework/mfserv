# release_1.1 CHANGELOG

## v1.1.3 (2021-07-20)

### Bug Fixes

- allow jinja2 include tag in plugin extra nginx conf (backport #505) (#507)

## v1.1.2 (2021-05-13)

### Bug Fixes

- we can use from_json jinja2 extension in nginx configuration files (backport #499) (#501)

## v1.1.1 (2021-05-10)

### Bug Fixes

- fix a plugin context issue (backport #495) (#497)

## v1.1.0 (2021-05-01)

### New Features

- load the pythonX_scientific_core layer by default in plugins (if the layer is installed) (#389)
- add a configuration option to open the endpoint /uuid to other … (#393)

### Bug Fixes

- don't prevent nginx to bind <1024 port (with setcap) (#411)
- bug with static files when extra_route is set to / (#424)
- fix bad comment in boostrapped config.ini for plugins (#435)
- avoid lua collisions with multiple openresty plugins (#447)
- fix static files routing with virtualhost (#452)
- fix virtualhosting usage (#456)
- fix potential lua collisions between mutiple openresty plugins (#451)
- fix error message in nginx error log (#473)
- fix concurrency issue about max_age (and max_age=0 now by default) (#477)
- fix some stop/start issues (#475)
- fix nginx root usage in some CI corner cases (#484)


