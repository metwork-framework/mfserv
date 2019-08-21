# release_0.8 CHANGELOG



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





