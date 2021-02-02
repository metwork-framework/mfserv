# CHANGELOG

## [Unreleased]

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


