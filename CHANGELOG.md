# release_0.9 CHANGELOG

## [Unreleased]

### Bug Fixes

- fix nginx root usage in some CI corner cases (backport #484) (#485)
- fix a complex issue about nginx var caching (#487)

## v0.9.13 (2020-11-02)

### Bug Fixes

- fix some rare https configuration issues (#436)

## v0.9.12 (2020-10-28)

### Bug Fixes

- bug with static files when extra_route is set to / (#425)

## v0.9.11 (2020-10-27)

### New Features

- backport of https support and <1024 port binding (from 1.0 branch) (#418)

## v0.9.10 (2020-09-25)

### New Features

- add a configuration option to open the endpoint /uuid to other … (bp #393) (#394)

## v0.9.9 (2020-01-29)

- No interesting change

## v0.9.8 (2020-01-27)

- No interesting change

## v0.9.7 (2020-01-09)

### Bug Fixes

- fix signal_wrapper in python2

## v0.9.6 (2020-01-02)

### Bug Fixes

- change the stop signal with autorestart dev feature

## v0.9.5 (2019-12-26)

- No interesting change

## v0.9.4 (2019-12-12)

- No interesting change

## v0.9.3 (2019-12-11)

### New Features

- add extra nginx configuration keys for empty plugins
- add a new configuration key for plugins

### Bug Fixes

- important fix about max_age feature

## v0.9.2 (2019-10-31)

### New Features

- little improvment in socket up/down feature

## v0.9.1 (2019-10-23)

- No interesting change

## v0.9.0 (2019-10-22)

### New Features

- introduce $extra_log_format nginx var
- introduce MFSERV_CURRENT_PLUGIN_* variables
- replace MODULE* environment variables names by MFMODULE* (MODULE_HOME becomes MFMODULE_HOME and so on)
- add an option to configure the nginx real_ip feature
- load resty.core in nginx conf
- add nginx/server_tokens option in config
- build mfserv without mfcom (mfcom layers are now included in mfext) (#254)
- add nodejs mflog lib
- infinite max_retry for circus (#258)
- add an option for x_forwarded headers
- add a warning if nginx/port is < 1024

### Bug Fixes

- fix security issue by updating django to latest 2.2 serie
- fix circus generation test


