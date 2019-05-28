import redis
import os


def application(environ, start_response):
    status = '200 OK'
    output = b'Hello World!'
    r = redis.Redis(
        unix_socket_path=os.environ['REDIS_SOCKET_UNIX_SOCKET_PATH'])
    r.ping()
    response_headers = [('Content-Type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)
    return [output]
