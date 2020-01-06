# release_0.9 CHANGELOG



## v0.9.6 (2020-01-02)

### New Features


### Bug Fixes
- change the stop signal with autorestart dev feature





## v0.9.5 (2019-12-26)

- No interesting change


## v0.9.4 (2019-12-12)

- No interesting change


## v0.9.3 (2019-12-11)

### New Features
- add a new configuration key for plugins
- add extra nginx configuration keys for empty plugins


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





