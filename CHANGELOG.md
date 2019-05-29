# CHANGELOG


## [Unreleased]

### New Features
- huge refactoring (sorry about this monster commit)
- remove double access-log messages with gunicorn
- add a .gitignore file in plugin templates
- introduce template inheritance for mfserv plugins
- introduce template inheritance
- add a mediation template
- introduce automatic mflog/nginx correlation for request_id
- add X-Request-Id header
- add plugin name in logs
- send mflog logs to mfadmin
- split multiple node workers output to multiple files


### Bug Fixes
- fix extra daemon feature and add test
- fix building issues with proxy
- proxy_timeout was bypassed by gunicorn sync configurations
- django template regression when bootstrapping
- fix some nasty reload bugs in some corner cases





