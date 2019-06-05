# release_0.7 CHANGELOG



## v0.7.0 (2019-05-29)

### New Features
- split multiple node workers output to multiple files
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


### Bug Fixes
- fix some nasty reload bugs in some corner cases
- django template regression when bootstrapping
- proxy_timeout was bypassed by gunicorn sync configurations
- fix building issues with proxy
- fix extra daemon feature and add test





