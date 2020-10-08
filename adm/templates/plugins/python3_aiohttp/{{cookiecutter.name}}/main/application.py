import sys
import os
from aiohttp import web
from aiohttp_metwork_middlewares import mflog_middleware
from aiohttp_metwork_middlewares import timeout_middleware_factory


async def handle(request):
    log = request['mflog_logger']
    log.info("this is an info message")
    return web.Response(text="Hello World from aiohttp app")


def get_app(timeout=int(os.environ['MFSERV_NGINX_TIMEOUT']) - 2):
    app = web.Application(middlewares=[timeout_middleware_factory(timeout),
                                       mflog_middleware])
    app.router.add_get('/{tail:.*}', handle)
    return app


if __name__ == '__main__':
    if len(sys.argv) == 3:
        web.run_app(get_app(int(sys.argv[2])), path=sys.argv[1])
    elif len(sys.argv) == 2:
        web.run_app(get_app(), path=sys.argv[1])
    else:
        web.run_app(get_app())
