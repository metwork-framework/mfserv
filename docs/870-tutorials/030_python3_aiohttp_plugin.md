# Python3_aiohttp plugin tutorial

Let's create a plugin based on the [python3_aiohttp plugin template](../../850-reference/plugin_templates/python3_aiohttp/100-intro/). We will called it **foo_nodejs**.

First, **bootstrap** the plugin with the command :
```bash
bootstrap_plugin.py create --template=python3_aiohttp foo_aiohttp
```

Once you have entered this command, you will be asked to fill in some fields to configure and customize your plugin: for now, press `[ENTER]` to set the default values. The plugin is created in the current directory, inside the directory named `foo_aiohttp`.

Check this directory, it contains few files, including:

- **main** directory: the Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it. This directory contains:
    - **application.py**: An entry-point for WSGI-compatible web servers to serve your project.

Let's now **build** the plugin by entering the command from the `foo_aiohttp` plugin directory:

```bash
make develop
```

Now, you can check your application works by invoking the following URL: http://localhost:18868/foo_aiohttp (you may replace localhost by your remote host if needed). A HTML page must display `Hello World from aiohttp app`.

!!! hint "Set the `debug` parameter to 1 (instead of 0) in the `[app_...]` section of the plugin `config.ini` file, in order to get an **interactive debugger** in your browser: check [Interactive debugger](../../../../360-mfserv_debug_plugin/#3-interactive-debugger)."

Check the `foo_aiohttp/application.py` script. It is a basic [aiohttp](https://docs.aiohttp.org/en/stable) application (app) which create, start the application. It routes all incoming HTTP GET requests to a unique handler which return an "Hello World" HTTP response.

You will also see some calls to start and stop functions and callbacks from `metwork_tools` module to neatly start and stop the application:
When creating the application, you will see [MetWork middlewares](https://github.com/metwork-framework/aiohttp_metwork_middlewares/) are passed to the `middlewares` parameter:

```python

def get_app(timeout=int(os.environ['MFSERV_NGINX_TIMEOUT']) - 2):
    app = web.Application(middlewares=[timeout_middleware_factory(timeout),
                                       mflog_middleware])
    app.router.add_get('/{tail:.*}', handle)
    return app
```

!!! info "You can disable some (or all) middlewares by changing (omitting) the `middlewares` parameter. See [aiohttp API](https://docs.aiohttp.org/en/stable/web_reference.html#application)"

We will extend our "Hello World!" application to handle more types of HTTP requests. Edit the the `foo_aiohttp/application.py` script as below:
```python
import sys
import os
from aiohttp import web
from aiohttp_metwork_middlewares import mflog_middleware
from aiohttp_metwork_middlewares import timeout_middleware_factory

app_name = os.environ.get('MFSERV_CURRENT_PLUGIN_NAME', "unknown")

def get_url_prefix():
    return '/{}'.format(app_name)

async def home_get(request):
    log = request['mflog_logger']
    log.info("this is an info message from home_get")
    return web.Response(text="Hello World from a GET request")


async def home_post(request):
    log = request['mflog_logger']
    log.info("this is an info message from home_post")
    return web.Response(text="Hello World from a POST request")

async def pattern(request):
    log = request['mflog_logger']
    log.info("this is an info message from pattern")
    return web.Response(text="Hello World from a Pattern Match")


def get_app(timeout=int(os.environ['MFSERV_NGINX_TIMEOUT']) - 2):
    app = web.Application(middlewares=[timeout_middleware_factory(timeout),
                                       mflog_middleware])
    app.router.add_get(get_url_prefix(), home_get)
    # This responds a POST request for the home url
    app.router.add_post(get_url_prefix(), home_post)
    # This responds a GET request for wxy, waxy, w1234bxy, and so on...
    app.router.add_get(get_url_prefix() + '/{tail:w.*xy}', pattern)
    return app


if __name__ == '__main__':
    if len(sys.argv) == 3:
        web.run_app(get_app(int(sys.argv[2])), path=sys.argv[1])
    elif len(sys.argv) == 2:
        web.run_app(get_app(), path=sys.argv[1])
    else:
        web.run_app(get_app())

```

Build the plugin with `make develop` command.

Check your application works by invoking the relevant URLs you added.

You may also doing the same with decorators:

```python
import sys
import os
from aiohttp import web
from aiohttp_metwork_middlewares import mflog_middleware
from aiohttp_metwork_middlewares import timeout_middleware_factory

routes = web.RouteTableDef()
app_name = os.environ.get('MFSERV_CURRENT_PLUGIN_NAME', "unknown")


def get_url_prefix():
    return '/{}'.format(app_name)

@routes.get(get_url_prefix())
async def home_get(request):
    log = request['mflog_logger']
    log.info("this is an info message from home_get")
    return web.Response(text="Hello World from a GET request")

@routes.post(get_url_prefix())
async def home_post(request):
    log = request['mflog_logger']
    log.info("this is an info message from home_post")
    return web.Response(text="Hello World from a POST request")

@routes.get(get_url_prefix() + '/{tail:w.*xy}')
async def pattern(request):
    log = request['mflog_logger']
    log.info("this is an info message from pattern")
    return web.Response(text="Hello World from a Pattern Match")


def get_app(timeout=int(os.environ['MFSERV_NGINX_TIMEOUT']) - 2):
    app = web.Application(middlewares=[timeout_middleware_factory(timeout),
                                       mflog_middleware])
    app.add_routes(routes)
    return app


if __name__ == '__main__':
    if len(sys.argv) == 3:
        web.run_app(get_app(int(sys.argv[2])), path=sys.argv[1])
    elif len(sys.argv) == 2:
        web.run_app(get_app(), path=sys.argv[1])
    else:
        web.run_app(get_app())

```

!!! info "See also  :"
    - [Official aiohttp documentation](http://docs.aiohttp.org/en/stable/)
    - [Configure a Metwork module](../../300-configuration_guide/#2-how-to-configure-a-metwork-module)



<!--
Intentional comment to prevent m2r from generating bad rst statements when the file ends with a block .. xxx ::
-->
