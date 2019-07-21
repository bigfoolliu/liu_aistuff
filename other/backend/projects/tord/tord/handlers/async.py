#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


import time

from tord.handlers.base import BaseHandler
from tornado import gen
from tornado.web import asynchronous


class AsyncHandler(BaseHandler):

    @asynchronous
    def get(self):
        self.write("asynchronous")
        self.finish()
    

class BlockHandler(BaseHandler):

    def get(self):
        time.sleep(10)
        self.write("block request")


class NoBlockHandler(BaseHandler):

    @gen.coroutine
    def get(self):
        yield gen.sleep(10)
        self.write("no block request")


class AsyncClientHandler(BaseHandler):

    def get(self):
        pass
