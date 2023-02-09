# release_2.1 CHANGELOG

## v2.1.1 (2023-01-04)

### New Features

- add release in plugins config.ini files (backport #564) (#565)

### Bug Fixes

- template Django 3 - metwork 2.1 - GDAL lib issue ... (#563) (backport #567) (#568)

## v2.1.0 (2022-12-08)

### New Features

- replace deprecated template python3_django (django 2) by template python3_django3 (django 3) (#529)
- remove all references to python2 (#551)
- add override for template plugins and upgrade uvicorn for template python3_raw_asgi (#554)
- use flask>2 for plugin template python3_flask (#556)
- switch from python 3.9 to python 3.10 (#558)

### Bug Fixes

- fix layerapi2 dependency for plugin nodejs (thanks to ne0t3ric) (#542)
- fix package-lock.json with nodejs 16 (#553)
- regex grouping in nginx location / (#560) (backport #561) (#562)

