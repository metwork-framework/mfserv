# release_0.7 CHANGELOG

## v0.7.6 (2019-08-09)

### New Features

- change default configuration
- add a redis_service option
- add plugin app directory into lua_package_path
- delete "blank only" files during bootstrap
- introduce an empty plugin type
- provide a better plugin crontab bootstrap
- better plugin crontab example
- aiohttp upgrade (now 3.4.4)
- Add static plugin type and corresponding template
- filter gunicorn messages in stdout/stderr depending on their level
- add an internal welcome plugin
- remove crontab support useless choice
- publish MFSERV environment variables into nginx environment
- first version of inotify powered conf_monitor
- provide a way for plugins to launch their own daemons
- add a plugin template for Django
- autorestart feature is configurable
- Changes in management of layer dependencies and metapackage names
- we can deactivate the nginx startup
- provide an easy way for a plugin to listen to an extra route
- execute integration tests directly from mfserv module
- nginx logs are now in JSON to prepare mfadmin#16 (#123)
- add an option to send nginx access log to mfadmin (#124)
- split multiple node workers output to multiple files
- remove "name" from the list of questions during plugin bootstrap
- remove plugins names from config.ini
- add nginx timeout configuration
- send mflog logs to mfadmin
- add plugin name in logs
- add X-Request-Id header
- introduce automatic mflog/nginx correlation for request_id
- add a mediation template
- introduce template inheritance
- introduce template inheritance for mfserv plugins
- add a .gitignore file in plugin templates
- remove double access-log messages with gunicorn
- huge refactoring (sorry about this monster commit)
- move plugin extra_nginx_general_conf to server section.
- allow / to be used as extra_route
- add a new configuration key (for extending nginx conf)
- add a healthcheck endpoint
- add some smart start/stop options and features
- add proxy_ignore_client_abort option
- add plugin dir as valid path for lua files (for openresty)

### Bug Fixes

- better plugin routing
- fix lua lib paths
- fix timeout issues around conf_monitor restarts
- handle NOTSET logging level value in nginx configuration
- add missing file for node plugin template
- don't start plugins during installation or uninstallation
- fix the node plugin template
- fix some nginx location conflicts when used with multiple apps
- more reliable nginx reload in conf_monitor
- upgrade django to version 2.1.5 to fix security vulnerability
- fix makefile target name
- fix some nasty reload bugs in some corner cases
- django template regression when bootstrapping
- proxy_timeout was bypassed by gunicorn sync configurations
- fix building issues with proxy
- fix extra daemon feature and add test
- remove debug message in nginx conf
- add the missing line for numprocesses
- typo with virtualdomain based routing

## v0.7.5 (2019-07-16)

### New Features

- change default configuration
- add a redis_service option
- add plugin app directory into lua_package_path
- delete "blank only" files during bootstrap
- introduce an empty plugin type
- provide a better plugin crontab bootstrap
- better plugin crontab example
- aiohttp upgrade (now 3.4.4)
- Add static plugin type and corresponding template
- filter gunicorn messages in stdout/stderr depending on their level
- add an internal welcome plugin
- remove crontab support useless choice
- publish MFSERV environment variables into nginx environment
- first version of inotify powered conf_monitor
- provide a way for plugins to launch their own daemons
- add a plugin template for Django
- autorestart feature is configurable
- Changes in management of layer dependencies and metapackage names
- we can deactivate the nginx startup
- provide an easy way for a plugin to listen to an extra route
- execute integration tests directly from mfserv module
- nginx logs are now in JSON to prepare mfadmin#16 (#123)
- add an option to send nginx access log to mfadmin (#124)
- split multiple node workers output to multiple files
- remove "name" from the list of questions during plugin bootstrap
- remove plugins names from config.ini
- add nginx timeout configuration
- send mflog logs to mfadmin
- add plugin name in logs
- add X-Request-Id header
- introduce automatic mflog/nginx correlation for request_id
- add a mediation template
- introduce template inheritance
- introduce template inheritance for mfserv plugins
- add a .gitignore file in plugin templates
- remove double access-log messages with gunicorn
- huge refactoring (sorry about this monster commit)
- move plugin extra_nginx_general_conf to server section.
- allow / to be used as extra_route
- add a new configuration key (for extending nginx conf)
- add a healthcheck endpoint
- add some smart start/stop options and features
- add proxy_ignore_client_abort option
- add plugin dir as valid path for lua files (for openresty)

### Bug Fixes

- better plugin routing
- fix lua lib paths
- fix timeout issues around conf_monitor restarts
- handle NOTSET logging level value in nginx configuration
- add missing file for node plugin template
- don't start plugins during installation or uninstallation
- fix the node plugin template
- fix some nginx location conflicts when used with multiple apps
- more reliable nginx reload in conf_monitor
- upgrade django to version 2.1.5 to fix security vulnerability
- fix makefile target name
- fix some nasty reload bugs in some corner cases
- django template regression when bootstrapping
- proxy_timeout was bypassed by gunicorn sync configurations
- fix building issues with proxy
- fix extra daemon feature and add test
- remove debug message in nginx conf
- add the missing line for numprocesses
- typo with virtualdomain based routing

## v0.7.4 (2019-07-15)

### New Features

- change default configuration
- add a redis_service option
- add plugin app directory into lua_package_path
- delete "blank only" files during bootstrap
- introduce an empty plugin type
- provide a better plugin crontab bootstrap
- better plugin crontab example
- aiohttp upgrade (now 3.4.4)
- Add static plugin type and corresponding template
- filter gunicorn messages in stdout/stderr depending on their level
- add an internal welcome plugin
- remove crontab support useless choice
- publish MFSERV environment variables into nginx environment
- first version of inotify powered conf_monitor
- provide a way for plugins to launch their own daemons
- add a plugin template for Django
- autorestart feature is configurable
- Changes in management of layer dependencies and metapackage names
- we can deactivate the nginx startup
- provide an easy way for a plugin to listen to an extra route
- execute integration tests directly from mfserv module
- nginx logs are now in JSON to prepare mfadmin#16 (#123)
- add an option to send nginx access log to mfadmin (#124)
- split multiple node workers output to multiple files
- remove "name" from the list of questions during plugin bootstrap
- remove plugins names from config.ini
- add nginx timeout configuration
- send mflog logs to mfadmin
- add plugin name in logs
- add X-Request-Id header
- introduce automatic mflog/nginx correlation for request_id
- add a mediation template
- introduce template inheritance
- introduce template inheritance for mfserv plugins
- add a .gitignore file in plugin templates
- remove double access-log messages with gunicorn
- huge refactoring (sorry about this monster commit)
- move plugin extra_nginx_general_conf to server section.
- allow / to be used as extra_route
- add a new configuration key (for extending nginx conf)
- add a healthcheck endpoint
- add some smart start/stop options and features
- add proxy_ignore_client_abort option
- add plugin dir as valid path for lua files (for openresty)

### Bug Fixes

- better plugin routing
- fix lua lib paths
- fix timeout issues around conf_monitor restarts
- handle NOTSET logging level value in nginx configuration
- add missing file for node plugin template
- don't start plugins during installation or uninstallation
- fix the node plugin template
- fix some nginx location conflicts when used with multiple apps
- more reliable nginx reload in conf_monitor
- upgrade django to version 2.1.5 to fix security vulnerability
- fix makefile target name
- fix some nasty reload bugs in some corner cases
- django template regression when bootstrapping
- proxy_timeout was bypassed by gunicorn sync configurations
- fix building issues with proxy
- fix extra daemon feature and add test
- remove debug message in nginx conf
- add the missing line for numprocesses
- typo with virtualdomain based routing

## v0.7.3 (2019-06-27)

### New Features

- change default configuration
- add a redis_service option
- add plugin app directory into lua_package_path
- delete "blank only" files during bootstrap
- introduce an empty plugin type
- provide a better plugin crontab bootstrap
- better plugin crontab example
- aiohttp upgrade (now 3.4.4)
- Add static plugin type and corresponding template
- filter gunicorn messages in stdout/stderr depending on their level
- add an internal welcome plugin
- remove crontab support useless choice
- publish MFSERV environment variables into nginx environment
- first version of inotify powered conf_monitor
- provide a way for plugins to launch their own daemons
- add a plugin template for Django
- autorestart feature is configurable
- Changes in management of layer dependencies and metapackage names
- we can deactivate the nginx startup
- provide an easy way for a plugin to listen to an extra route
- execute integration tests directly from mfserv module
- nginx logs are now in JSON to prepare mfadmin#16 (#123)
- add an option to send nginx access log to mfadmin (#124)
- split multiple node workers output to multiple files
- remove "name" from the list of questions during plugin bootstrap
- remove plugins names from config.ini
- add nginx timeout configuration
- send mflog logs to mfadmin
- add plugin name in logs
- add X-Request-Id header
- introduce automatic mflog/nginx correlation for request_id
- add a mediation template
- introduce template inheritance
- introduce template inheritance for mfserv plugins
- add a .gitignore file in plugin templates
- remove double access-log messages with gunicorn
- huge refactoring (sorry about this monster commit)
- move plugin extra_nginx_general_conf to server section.
- allow / to be used as extra_route
- add a new configuration key (for extending nginx conf)
- add a healthcheck endpoint
- add some smart start/stop options and features
- add proxy_ignore_client_abort option
- add plugin dir as valid path for lua files (for openresty)

### Bug Fixes

- better plugin routing
- fix lua lib paths
- fix timeout issues around conf_monitor restarts
- handle NOTSET logging level value in nginx configuration
- add missing file for node plugin template
- don't start plugins during installation or uninstallation
- fix the node plugin template
- fix some nginx location conflicts when used with multiple apps
- more reliable nginx reload in conf_monitor
- upgrade django to version 2.1.5 to fix security vulnerability
- fix makefile target name
- fix some nasty reload bugs in some corner cases
- django template regression when bootstrapping
- proxy_timeout was bypassed by gunicorn sync configurations
- fix building issues with proxy
- fix extra daemon feature and add test
- remove debug message in nginx conf
- add the missing line for numprocesses
- typo with virtualdomain based routing

## v0.7.2 (2019-06-17)

### New Features

- change default configuration
- add a redis_service option
- add plugin app directory into lua_package_path
- delete "blank only" files during bootstrap
- introduce an empty plugin type
- provide a better plugin crontab bootstrap
- better plugin crontab example
- aiohttp upgrade (now 3.4.4)
- Add static plugin type and corresponding template
- filter gunicorn messages in stdout/stderr depending on their level
- add an internal welcome plugin
- remove crontab support useless choice
- publish MFSERV environment variables into nginx environment
- first version of inotify powered conf_monitor
- provide a way for plugins to launch their own daemons
- add a plugin template for Django
- autorestart feature is configurable
- Changes in management of layer dependencies and metapackage names
- we can deactivate the nginx startup
- provide an easy way for a plugin to listen to an extra route
- execute integration tests directly from mfserv module
- nginx logs are now in JSON to prepare mfadmin#16 (#123)
- add an option to send nginx access log to mfadmin (#124)
- split multiple node workers output to multiple files
- remove "name" from the list of questions during plugin bootstrap
- remove plugins names from config.ini
- add nginx timeout configuration
- send mflog logs to mfadmin
- add plugin name in logs
- add X-Request-Id header
- introduce automatic mflog/nginx correlation for request_id
- add a mediation template
- introduce template inheritance
- introduce template inheritance for mfserv plugins
- add a .gitignore file in plugin templates
- remove double access-log messages with gunicorn
- huge refactoring (sorry about this monster commit)
- move plugin extra_nginx_general_conf to server section.
- allow / to be used as extra_route
- add a new configuration key (for extending nginx conf)
- add a healthcheck endpoint
- add some smart start/stop options and features
- add proxy_ignore_client_abort option
- add plugin dir as valid path for lua files (for openresty)

### Bug Fixes

- better plugin routing
- fix lua lib paths
- fix timeout issues around conf_monitor restarts
- handle NOTSET logging level value in nginx configuration
- add missing file for node plugin template
- don't start plugins during installation or uninstallation
- fix the node plugin template
- fix some nginx location conflicts when used with multiple apps
- more reliable nginx reload in conf_monitor
- upgrade django to version 2.1.5 to fix security vulnerability
- fix makefile target name
- fix some nasty reload bugs in some corner cases
- django template regression when bootstrapping
- proxy_timeout was bypassed by gunicorn sync configurations
- fix building issues with proxy
- fix extra daemon feature and add test
- remove debug message in nginx conf
- add the missing line for numprocesses
- typo with virtualdomain based routing

## v0.7.1 (2019-06-12)

### New Features

- change default configuration
- add a redis_service option
- add plugin app directory into lua_package_path
- delete "blank only" files during bootstrap
- introduce an empty plugin type
- provide a better plugin crontab bootstrap
- better plugin crontab example
- aiohttp upgrade (now 3.4.4)
- Add static plugin type and corresponding template
- filter gunicorn messages in stdout/stderr depending on their level
- add an internal welcome plugin
- remove crontab support useless choice
- publish MFSERV environment variables into nginx environment
- first version of inotify powered conf_monitor
- provide a way for plugins to launch their own daemons
- add a plugin template for Django
- autorestart feature is configurable
- Changes in management of layer dependencies and metapackage names
- we can deactivate the nginx startup
- provide an easy way for a plugin to listen to an extra route
- execute integration tests directly from mfserv module
- nginx logs are now in JSON to prepare mfadmin#16 (#123)
- add an option to send nginx access log to mfadmin (#124)
- split multiple node workers output to multiple files
- remove "name" from the list of questions during plugin bootstrap
- remove plugins names from config.ini
- add nginx timeout configuration
- send mflog logs to mfadmin
- add plugin name in logs
- add X-Request-Id header
- introduce automatic mflog/nginx correlation for request_id
- add a mediation template
- introduce template inheritance
- introduce template inheritance for mfserv plugins
- add a .gitignore file in plugin templates
- remove double access-log messages with gunicorn
- huge refactoring (sorry about this monster commit)
- move plugin extra_nginx_general_conf to server section.
- allow / to be used as extra_route
- add a new configuration key (for extending nginx conf)
- add a healthcheck endpoint
- add some smart start/stop options and features
- add proxy_ignore_client_abort option
- add plugin dir as valid path for lua files (for openresty)

### Bug Fixes

- better plugin routing
- fix lua lib paths
- fix timeout issues around conf_monitor restarts
- handle NOTSET logging level value in nginx configuration
- add missing file for node plugin template
- don't start plugins during installation or uninstallation
- fix the node plugin template
- fix some nginx location conflicts when used with multiple apps
- more reliable nginx reload in conf_monitor
- upgrade django to version 2.1.5 to fix security vulnerability
- fix makefile target name
- fix some nasty reload bugs in some corner cases
- django template regression when bootstrapping
- proxy_timeout was bypassed by gunicorn sync configurations
- fix building issues with proxy
- fix extra daemon feature and add test
- remove debug message in nginx conf
- add the missing line for numprocesses
- typo with virtualdomain based routing

## v0.7.0 (2019-05-29)

### New Features

- change default configuration
- add a redis_service option
- add plugin app directory into lua_package_path
- delete "blank only" files during bootstrap
- introduce an empty plugin type
- provide a better plugin crontab bootstrap
- better plugin crontab example
- aiohttp upgrade (now 3.4.4)
- Add static plugin type and corresponding template
- filter gunicorn messages in stdout/stderr depending on their level
- add an internal welcome plugin
- remove crontab support useless choice
- publish MFSERV environment variables into nginx environment
- first version of inotify powered conf_monitor
- provide a way for plugins to launch their own daemons
- add a plugin template for Django
- autorestart feature is configurable
- Changes in management of layer dependencies and metapackage names
- we can deactivate the nginx startup
- provide an easy way for a plugin to listen to an extra route
- execute integration tests directly from mfserv module
- nginx logs are now in JSON to prepare mfadmin#16 (#123)
- add an option to send nginx access log to mfadmin (#124)
- split multiple node workers output to multiple files
- remove "name" from the list of questions during plugin bootstrap
- remove plugins names from config.ini
- add nginx timeout configuration
- send mflog logs to mfadmin
- add plugin name in logs
- add X-Request-Id header
- introduce automatic mflog/nginx correlation for request_id
- add a mediation template
- introduce template inheritance
- introduce template inheritance for mfserv plugins
- add a .gitignore file in plugin templates
- remove double access-log messages with gunicorn
- huge refactoring (sorry about this monster commit)
- move plugin extra_nginx_general_conf to server section.
- allow / to be used as extra_route
- add a new configuration key (for extending nginx conf)
- add a healthcheck endpoint
- add some smart start/stop options and features
- add proxy_ignore_client_abort option
- add plugin dir as valid path for lua files (for openresty)

### Bug Fixes

- better plugin routing
- fix lua lib paths
- fix timeout issues around conf_monitor restarts
- handle NOTSET logging level value in nginx configuration
- add missing file for node plugin template
- don't start plugins during installation or uninstallation
- fix the node plugin template
- fix some nginx location conflicts when used with multiple apps
- more reliable nginx reload in conf_monitor
- upgrade django to version 2.1.5 to fix security vulnerability
- fix makefile target name
- fix some nasty reload bugs in some corner cases
- django template regression when bootstrapping
- proxy_timeout was bypassed by gunicorn sync configurations
- fix building issues with proxy
- fix extra daemon feature and add test
- remove debug message in nginx conf
- add the missing line for numprocesses
- typo with virtualdomain based routing


