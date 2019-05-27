from mflog import get_logger

logger = get_logger("myapp")


def application(environ, start_response):
    status = '200 OK'
    output = b'Hello World!'
    logger.info("this is a test message")
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
