import django
import redis
import os

REDIS_SOCKET_UNIX_SOCKET_PATH = os.environ['REDIS_SOCKET_UNIX_SOCKET_PATH']


def application(environ, start_response):
    x = redis.Redis(unix_socket_path=REDIS_SOCKET_UNIX_SOCKET_PATH)
    x.ping()
    status = '200 OK'
    output = b'Hello World!'
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
