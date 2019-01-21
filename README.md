# mfserv

[//]: # (automatically generated from https://github.com/metwork-framework/resources/blob/master/cookiecutter/%7B%7Bcookiecutter.repo%7D%7D/README.md)

## Status (master branch)
[![Drone CI](http://metwork-framework.org:8000/api/badges/metwork-framework/mfserv/status.svg)](http://metwork-framework.org:8000/metwork-framework/mfserv)
[![Maintenance](https://github.com/metwork-framework/resources/blob/master/badges/maintained.svg)]()
[![License](https://github.com/metwork-framework/resources/blob/master/badges/bsd.svg)]()

## What is it ?

This in the **M**etwork **F**ramework "**SERV**ices" module. This module is a kind of private [PAAS](https://en.wikipedia.org/wiki/Platform_as_a_service) which help to develop, run and manage
webservices applications.

With this module, you can easily implement robust webservices with:

- synchronous Python3 (with a custom virtualenv including the framework you want like Django, Flask...)
- synchronous Python2 (with a custom virtualenv including the framework you want like Django, Flask...)
- asynchronous Python3 (with [aiohttp](https://aiohttp.readthedocs.io/) and your custom virtualenv)
- nodejs (and your custom `node_modules`)

All these technologies are managed in a "production ready" with:

- a dynamically configured `nginx` webserver in front
- some multiple workers in back
- memory limits
- autorestart features
- logs and metrics



## Installation guide

See [this document](.metwork-framework/install_a_metwork_package.md).

## Configuration guide

See [this document](.metwork-framework/configure_a_metwork_package.md).


## Contributing guide

See [CONTRIBUTING.md](CONTRIBUTING.md) file.



## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) file.


