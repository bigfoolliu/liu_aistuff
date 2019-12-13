#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
tornado异步非阻塞实现之 多进程
"""


import time

import tornado.web
from tornado import gen
from tornado.httpserver import HTTPServer


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("index page:{}".format(time.time()))


@gen.coroutine
def doing():
    yield gen.sleep(10)
    raise gen.Return(time.time())


class NonBlockHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        ret = yield doing()
        self.write("non block:{}".format(ret))


app = tornado.web.Application(handlers=[
    (r"/", IndexHandler),
    (r"/nonblock", NonBlockHandler),
], debug=True)


if __name__ == "__main__":
    print("listening on port: 8000")
    try:
        server = HTTPServer(app)
        server.bind(8000)
        server.start(2)  # 设置启动多少个进程
        tornado.ioloop.IOLoop.current().start()
    except Exception as e:
        print(e)
        tornado.ioloop.IOLoop.current().stop()
