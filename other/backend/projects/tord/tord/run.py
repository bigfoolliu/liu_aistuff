#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

define("port", type=int, default=8000, help="server port")


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("hello, tornado")
        self.set_status(200)
        self.finish()


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [(r"/", IndexHandler),],
        )

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
