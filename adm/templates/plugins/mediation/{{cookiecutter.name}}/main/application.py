import sys
import os
from aiohttp import web, ClientSession
from aiohttp_metwork_middlewares import mflog_middleware
from aiohttp_metwork_middlewares import timeout_middleware_factory

CHUNK_SIZE = 4096 * 1024
STREAMING_MODE = True


async def handle(request):

    # Log something with context aware logger
    log = request['mflog_logger']
    http_method = request.method
    url_path_qs = request.path_qs
    log.info("got a %s call on %s" % (http_method, url_path_qs))

    # For this example, we limit the service to GET/HEAD methods
    if http_method not in ["GET", "HEAD"]:
        return web.Response(status=405)

    # Let's build the backend url
    backend_url = "http://mybackend%s" % url_path_qs

    async with ClientSession() as session:
        log.info("calling %s on %s..." % (http_method, backend_url))
        async with session.get(backend_url) as resp:

            backend_status = resp.status
            log.info("got an HTTP/%i status" % backend_status)

            if not STREAMING_MODE:
                ######################
                # NON STREAMING MODE #
                ######################

                body = await resp.read()
                response = web.Response(
                    headers={"Content-Type": resp.headers['Content-Type']},
                    body=body
                )

            else:
                ##################
                # STREAMING MODE #
                ##################

                # Let's prepare a streaming response
                response = web.StreamResponse(
                    headers={"Content-Type": resp.headers['Content-Type']}
                )
                await response.prepare(request)
                response.content_type = resp.headers['Content-Type']

                # Let's stream the response body to avoid storing it in memory
                while True:
                    chunk = await resp.content.read(CHUNK_SIZE)
                    if not chunk:
                        break
                    await response.write(chunk)
                await response.write_eof()

    return response


def get_app(timeout=int(os.environ['MFSERV_NGINX_TIMEOUT']) + 2):
    app = web.Application(middlewares=[timeout_middleware_factory(timeout),
                                       mflog_middleware])
    app.router.add_route('*', '/{tail:.*}', handle)
    return app


if __name__ == '__main__':
    if len(sys.argv) == 3:
        web.run_app(get_app(int(sys.argv[2])), path=sys.argv[1])
    elif len(sys.argv) == 2:
        web.run_app(get_app(), path=sys.argv[1])
    else:
        web.run_app(get_app())
