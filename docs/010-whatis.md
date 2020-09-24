# What is it?

This in the **M**etwork **F**ramework "**SERV**ices" module. This module is a kind of private [PAAS](https://en.wikipedia.org/wiki/Platform_as_a_service) which help to develop, run and manage
webservices applications.

With this module, you can easily implement robust webservices with:

- synchronous Python3 (WSGI) (with a custom virtualenv including the framework you want like Django, Flask...)
- synchronous Python2 (WSGI) (with a custom virtualenv including the framework you want like Django, Flask...)
- asynchronous Python3 (with [aiohttp](https://aiohttp.readthedocs.io/) and your custom virtualenv)
- asynchronous Python3 (with [tornado](https://www.tornadoweb.org/) and your custom virtualenv)
- asynchronous Python3 [ASGI](https://asgi.readthedocs.io/) (with [Uvicorn](https://www.uvicorn.org/) server and your custom virtualenv including your favorite async framework like [FastAPI](https://fastapi.tiangolo.com/), [Starlette](https://github.com/encode/starlette)...)
- nodejs (and your custom `node_modules`)
- [OpenResty](https://openresty.org/en/) (lua + nginx)

All these technologies are managed in a "production ready" with:

- a dynamically configured `nginx` webserver in front
- some multiple workers in back
- memory limits
- autorestart features
- logs and metrics

They are optimized a lot to get huge performances. Have a look to [this blog post](https://medium.com/metwork-framework/a-new-way-to-serve-python-web-apps-d5662ab69dc0) for details.
