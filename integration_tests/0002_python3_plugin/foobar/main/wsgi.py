
def application(environ, start_response):
    status = b'200 OK'
    output = b'Hello World!'
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]

