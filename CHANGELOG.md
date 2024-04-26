# release_2.2 CHANGELOG

## [Unreleased]

### New Features

- add initscripts, make and crontab as dependencies (backport #628) (#629)
- add support of the nginx port_in_redirect directive (#627)

## v2.2.3 (2024-04-05)

- No interesting change

## v2.2.2 (2024-04-03)

### Bug Fixes

- stop plugins before nginx stop (#621) (#624)

## v2.2.1 (2023-12-09)

### Bug Fixes

- requires django<5 (django 5 requires sqlite >= 3.27 not availabl… (backport #614) (#615)

## v2.2.0 (2023-12-01)

### New Features

- add release in plugins config.ini files (#564)
- upgrade jquery from 3.3.1 to 3.5.1 (security update) (#584)
- use sonarcloud.io for sonarqube checks (#597)
- rename template python3_django3 in python3_django with django4 (backport #612) (#613)

### Bug Fixes

- regex grouping in nginx location / (#560) (#561)
- template Django 3 - metwork 2.1 - GDAL lib issue ... (#563) (#567)
- force django3>=3.2.17 in template plugin django3 (security fix) (#573)
- regression on static routing (#576) (#577)
- fix .releaseignore to ignore .git folder when releasing plugins (#581)
- django, duplicated logs (#579) (#580)
- force flask >= 2.2.5 for security reason (#585)
- .release_ignore instead of .releaseignore in common.mk (closes #… (#608)


