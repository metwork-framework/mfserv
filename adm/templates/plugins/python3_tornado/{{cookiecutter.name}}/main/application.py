import sys
import tornado.ioloop
import tornado.web
import tornado.httpserver
import tornado.netutil


class MainHandler(tornado.web.RequestHandler):
    async def get(self):
        self.write("Hello, world")


def make_app():
    return tornado.web.Application([
        (r"/.*", MainHandler),
    ])


if __name__ == "__main__":
    app = make_app()
    if len(sys.argv) >= 2:
        server = tornado.httpserver.HTTPServer(app)
        socket = tornado.netutil.bind_unix_socket(sys.argv[1])
        server.add_socket(socket)
    else:
        app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
