# CHANGELOG


## [Unreleased]

### New Features
- send mflog logs to mfadmin
- add plugin name in logs
- add X-Request-Id header
- introduce automatic mflog/nginx correlation for request_id
- add a mediation template


### Bug Fixes
- fix some nasty reload bugs in some corner cases





## v0.6.0 (2019-03-27)

### New Features
- nginx logs are now in JSON to prepare mfadmin#16 (#123)
- add an option to send nginx access log to mfadmin (#124)
- split multiple node workers output to multiple files
- remove "name" from the list of questions during plugin bootstrap
- remove plugins names from config.ini
- add nginx timeout configuration


### Bug Fixes
- fix makefile target name





