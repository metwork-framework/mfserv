# release_2.1 CHANGELOG

## [Unreleased]

### New Features

- replace deprecated template python3_django (django 2) by template python3_django3 (django 3) (#529)
- remove all references to python2 (#551)
- add override for template plugins and upgrade uvicorn for template python3_raw_asgi (#554)
- use flask>2 for plugin template python3_flask (#556)
- switch from python 3.9 to python 3.10 (#558)

### Bug Fixes

- fix layerapi2 dependency for plugin nodejs (thanks to ne0t3ric) (#542)
- fix package-lock.json with nodejs 16 (#553)


