#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu

import logging
import os

import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import define, options

from tord.handlers import index, upload, media

define("port", type=int, default=8000, help="server port")


def main():
    tornado.options.parse_command_line()

    app = tornado.web.Application(
        [(r"/", index.IndexHandler),
        (r"/books", upload.BooksHandler),
        (r"/images", media.ImageHandler),
        (r"/videos", media.VideoHandler),
        (r"/async/", )
        ],)  

    try:
        app.listen(options.port)
        logging.info("listening on port {}".format(options.port))
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()
