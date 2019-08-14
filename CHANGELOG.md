# release_0.8 CHANGELOG


## [Unreleased]

### New Features
- add plugin dir as valid path for lua files (for openresty)
- plugins.hotswap feature!
- add proxy_ignore_client_abort option
- add some smart start/stop options and features
- add a healthcheck endpoint
- debug circus and nginx configuration generation
- rename circus watcher names (step => app)
- add template "flask"
- add a new configuration key (for extending nginx conf)
- allow / to be used as extra_route
- move plugin extra_nginx_general_conf to server section.
- use envtpl new option --reduce-multi-blank-lines (#183)


### Bug Fixes
- more precise condition to delete python-requirement
- typo with virtualdomain based routing
- issues in flask plugin.
- add the missing line for numprocesses
- remove debug message in nginx conf
- fix extra daemon feature and add test





