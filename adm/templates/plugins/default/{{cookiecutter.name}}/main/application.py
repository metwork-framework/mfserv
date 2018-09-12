{% if cookiecutter.type == "gunicorn3_asyncio" %}
from aiohttp import web


async def handle(request):
    return web.Response(text="Hello World")

app = web.Application()
app.router.add_get('/{tail:.*}', handle)
{% endif %}
