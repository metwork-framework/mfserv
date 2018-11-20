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
