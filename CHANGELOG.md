# CHANGELOG


## [Unreleased]

### New Features
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





