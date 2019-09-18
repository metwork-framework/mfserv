from aiohttp import web
import os
from mflog import get_logger
from async_timeout import timeout


MFMODULE = os.environ['MFMODULE']
CURRENT_PLUGIN_NAME_ENV_VAR = "%s_CURRENT_PLUGIN_NAME" % MFMODULE
if CURRENT_PLUGIN_NAME_ENV_VAR in os.environ:
    PLUGIN = os.environ[CURRENT_PLUGIN_NAME_ENV_VAR]
else:
    PLUGIN = None


def timeout_middleware_factory(seconds):
    @web.middleware
    async def timeout_middleware(request, handler):
        async with timeout(seconds):
            return await handler(request)
    return timeout_middleware


@web.middleware
async def mflog_middleware(request, handler):
    request_id = request.headers.get("X-Request-Id", None)
    if PLUGIN:
        log = get_logger("%s.aiohttp" % PLUGIN)
    else:
        log = get_logger("aiohttp")
    if request_id:
        log = log.bind(request_id=request_id)
    request['mflog_logger'] = log
    try:
        return await handler(request)
    except web.HTTPException:
        raise
    except Exception:
        log.exception("exception catched")
        return web.Response(text="HTTP/500", status=500)
