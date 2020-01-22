[![logo](https://raw.githubusercontent.com/metwork-framework/resources/master/logos/metwork-white-logo-small.png)](http://www.metwork-framework.org)
# mfserv

[//]: # (automatically generated from https://github.com/metwork-framework/resources/blob/master/cookiecutter/_%7B%7Bcookiecutter.repo%7D%7D/README.md)

**Status (master branch)**



[![Drone CI](http://metwork-framework.org:8000/api/badges/metwork-framework/mfserv/status.svg)](http://metwork-framework.org:8000/metwork-framework/mfserv)
[![Maintenance](https://github.com/metwork-framework/resources/blob/master/badges/maintained.svg)]()
[![License](https://github.com/metwork-framework/resources/blob/master/badges/bsd.svg)]()
[![Gitter](https://github.com/metwork-framework/resources/blob/master/badges/community-en.svg)](https://gitter.im/metwork-framework/community-en?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)
[![Gitter](https://github.com/metwork-framework/resources/blob/master/badges/community-fr.svg)](https://gitter.im/metwork-framework/community-fr?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)


[//]: # (TABLE_OF_CONTENTS_PLACEHOLDER)

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








## Full list of components

| Name | Version | Layer |
| --- | --- | --- |
| [aiohttp](https://github.com/aio-libs/aiohttp) | 3.4.4 | python3 |
| [async-timeout](https://github.com/aio-libs/async_timeout/) | 3.0.0 | python3 |
| [attrs](https://www.attrs.org/) | 18.2.0 | python3 |
| [bjoern](https://github.com/thefab/bjoern/tree/metwork) | metwork-20190515 | python2 |
| [bjoern](https://github.com/thefab/bjoern/tree/metwork) | metwork-20190515 | python3 |
| [idna-ssl](https://github.com/aio-libs/idna-ssl) | 1.1.0 | python3 |
| [multidict](https://github.com/aio-libs/multidict) | 4.4.2 | python3 |
| [yarl](https://github.com/aio-libs/yarl/) | 1.2.6 | python3 |

*(8 components)*










## Cheatsheet

A cheatsheet for this module is available [here](.metwork-framework/cheatsheet.md)



## Reference documentation

- (for **master (development)** version), see [this dedicated site](http://metwork-framework.org/pub/metwork/continuous_integration/docs/master/mfserv/) for reference documentation.
- (for **latest released stable** version), see [this dedicated site](http://metwork-framework.org/pub/metwork/releases/docs/stable/mfserv/) for reference documentation.

For very specific use cases, you might be interested in
[reference documentation for integration branch](http://metwork-framework.org/pub/metwork/continuous_integration/docs/integration/mfserv/).

And if you are looking for an old released version, you can search [here](http://metwork-framework.org/pub/metwork/releases/docs/).



## Installation guide

See [this document](.metwork-framework/install_a_metwork_package.md).


## Configuration guide

See [this document](.metwork-framework/configure_a_metwork_package.md).





## Contributing guide

See [CONTRIBUTING.md](CONTRIBUTING.md) file.



## Code of Conduct

See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) file.



## Sponsors

*(If you are officially paid to work on MetWork Framework, please contact us to add your company logo here!)*

[![logo](https://raw.githubusercontent.com/metwork-framework/resources/master/sponsors/meteofrance-small.jpeg)](http://www.meteofrance.com)
