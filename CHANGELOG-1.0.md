# release_1.0 CHANGELOG

## v1.0.18 (2021-08-12)

### Bug Fixes

- fix missing http_host and via in logs and a minor issue with / as custom route (backport #517) (#518)

## v1.0.17 (2021-07-22)

### Bug Fixes

- fix ssl with virtualhost (backport #508) (#509)

## v1.0.16 (2021-07-20)

### Bug Fixes

- allow jinja2 include tag in plugin extra nginx conf (backport #505) (#506)

## v1.0.15 (2021-05-11)

### Bug Fixes

- we can use from_json jinja2 extension in nginx configuration files (backport #499) (#500)

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

- No interesting change

## v1.0.1 (2020-09-19)

- No interesting change


