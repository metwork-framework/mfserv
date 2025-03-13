# CHANGELOG

## [Unreleased]

### New Features

- rename template python3_django3 in python3_django with django4 (#612)
- authorize django >=5 (ok with built-in sqlite 3.45 in layer core) (#616)
- add support of the nginx port_in_redirect directive (#626)
- add initscripts, make and crontab as dependencies (#628)
- add plugin php (first version, from repository mfservplugin_php) (#645)
- plugin PHP template (#649)
- bump django to 5.0.13 in template django to fix CVE-2025-26699 (#650)

### Bug Fixes

- requires django<5 (django 5 requires sqlite >= 3.27 not availabl… (#614)
- stop plugins before nginx stop (#621)
- fix vulnerabilites in django (CVE-2024-45231 and CVE-2024-45230) (#634)
- enable the access log for the healthcheck endpoint (closes #1958) (#637)
- bump django5 to 5.0.11 (CVE-2024-56374) (#644)


