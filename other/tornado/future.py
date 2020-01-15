#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
使用future来解决异步问题 
"""


import tornado.web
from tornado import gen
from tornado.concurrent import Future


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.write('index')


def doing():
    future = Future()
    # here doing some things ...
    future.set_result('Non-Blocking')
    return future


class NonBlockingHandler(tornado.web.RequestHandler):

    @gen.coroutine
    def get(self):
        result = yield doing()
        self.write(result)


application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/nonblocking", NonBlockingHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
