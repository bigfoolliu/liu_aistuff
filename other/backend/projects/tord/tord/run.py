#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

define("port", type=int, default=8000, help="server port")


class BaseHandler(tornado.web.RequestHandler):

    def get(self):
        raise NotImplementedError
    
    def post(self):
        raise NotImplementedError
    
    def write_success(self, reason=None):
        self.set_status(200, reason=reason)
        self.finish()


class IndexHandler(BaseHandler):

    def get(self):
        self.write("hello, tornado")
        self.write_success()


class BooksHandler(BaseHandler):

    def get(self, data):
        self.write(data)
        self.write_success(reason="return ok")


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [(r"/", IndexHandler),
        (r"/books/(\w+)", BooksHandler),],)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
