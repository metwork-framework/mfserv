# release_2.2 CHANGELOG

## v2.2.13 (2025-12-04)

### New Features

- bump django to 4.2.27 to fix CVE-2025-13372 and CVE-2025-64460 (#698)

## v2.2.12 (2025-11-07)

### New Features

- bump django >= 4.2.26 (fix CVE-2025-64458 and 64459) (#693)

## v2.2.11 (2025-10-16)

### New Features

- bump django >= 4.2.25 (fix CVE-2025-57833) (#686)

## v2.2.10 (2025-09-16)

### New Features

- force django >= 4.2.24 in plugin django (CVE-2025-57833) (#684)

## v2.2.9 (2025-09-05)

### New Features

- add comments to explain how to resolve setcap problems (backport #677) (#678)

## v2.2.8 (2025-06-11)

### New Features

- bump django to 4.2.22 to fix CVE-2025-48432 (#659)

## v2.2.7 (2025-03-13)

### New Features

- bump django to 4.2.17 (CVE-2024-53907 and CVE-2024-53908) (#643)
- add plugin php (first version, from repository mfservplugin_php) (backport #645) (#647)

### Bug Fixes

- bump django to 4.2.20 in template django to fix CVE-2025-26699 (#651)

## v2.2.6 (2024-10-26)

- No interesting change

## v2.2.5 (2024-10-25)

### Bug Fixes

- fix vulnerabilites in django (CVE-2024-45231 and CVE-2024-45230) (backport #634) (#635)
- enable the access log for the healthcheck endpoint (closes #1958) (#637) (#638)

## v2.2.4 (2024-04-26)

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


