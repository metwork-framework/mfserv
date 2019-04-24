from aiohttp import web
from aiohttp_metwork_middlewares import mflog_middleware


async def handle(request):
    log = request['mflog_logger']
    log.info("this is an info message")
    return web.Response(text="Hello World")

app = web.Application(middlewares=[mflog_middleware])
app.router.add_get('/{tail:.*}', handle)
