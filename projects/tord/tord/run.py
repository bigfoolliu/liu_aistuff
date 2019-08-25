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

from tord.settings import settings
from tord.urls import url_patterns

define("port", type=int, default=8000, help="server port")


def main():
    tornado.options.parse_command_line()
    app = tornado.web.Application(url_patterns)

    try:
        app.listen(options.port)
        logging.info("listening on port {}".format(options.port))
        tornado.ioloop.IOLoop.instance().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.instance().stop()
