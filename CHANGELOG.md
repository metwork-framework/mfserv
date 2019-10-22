# release_0.9 CHANGELOG


## [Unreleased]

### New Features
- add a warning if nginx/port is < 1024
- add an option for x_forwarded headers
- infinite max_retry for circus (#258)
- add nodejs mflog lib
- build mfserv without mfcom (mfcom layers are now included in mfext) (#254)
- add nginx/server_tokens option in config
- load resty.core in nginx conf
- add an option to configure the nginx real_ip feature
- replace MODULE* environment variables names by MFMODULE* (MODULE_HOME becomes MFMODULE_HOME and so on)
- introduce MFSERV_CURRENT_PLUGIN_* variables
- introduce $extra_log_format nginx var


### Bug Fixes
- fix circus generation test
- fix security issue by updating django to latest 2.2 serie





