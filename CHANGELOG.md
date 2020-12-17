# release_0.8 CHANGELOG

## v0.8.4 (2019-10-15)

### New Features

- add nodejs mflog lib
- add an option for x_forwarded headers

## v0.8.3 (2019-09-30)

### New Features

- add nginx/server_tokens option in config
- load resty.core in nginx conf

### Bug Fixes

- fix extra_nginx_server_conf_filename usage

## v0.8.2 (2019-09-25)

### New Features

- add an option to configure the nginx real_ip feature

### Bug Fixes

- fix security issue by updating django to latest 2.2 serie

## v0.8.1 (2019-09-16)

### New Features

- introduce $extra_log_format nginx var
- introduce MFSERV_CURRENT_PLUGIN_* variables

## v0.8.0 (2019-08-14)

### New Features

- use envtpl new option --reduce-multi-blank-lines (#183)
- move plugin extra_nginx_general_conf to server section.
- allow / to be used as extra_route
- add a new configuration key (for extending nginx conf)
- add template "flask"
- rename circus watcher names (step => app)
- debug circus and nginx configuration generation
- add a healthcheck endpoint
- add some smart start/stop options and features
- add proxy_ignore_client_abort option
- plugins.hotswap feature!
- add plugin dir as valid path for lua files (for openresty)

### Bug Fixes

- fix extra daemon feature and add test
- remove debug message in nginx conf
- add the missing line for numprocesses
- issues in flask plugin.
- typo with virtualdomain based routing
- more precise condition to delete python-requirement


