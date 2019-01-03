{% if cookiecutter.type != "gunicorn3_asyncio" %}
def application(environ, start_response):
    status = '200 OK'
    output = b'Hello World!'
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
{% endif %}
