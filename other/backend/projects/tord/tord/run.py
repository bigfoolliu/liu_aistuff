#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu

import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from tord.handlers.index import IndexHandler
from tord.handlers.upload import BooksHandler

define("port", type=int, default=8000, help="server port")


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        [(r"/", IndexHandler),
        (r"/books", BooksHandler),
        ],)

    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.current().start()
