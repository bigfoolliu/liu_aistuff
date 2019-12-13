#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
tornado异步非阻塞实现之 线程池
"""

import os
import time
from concurrent.futures import ThreadPoolExecutor

import tornado.web
from tornado import gen
from tornado.concurrent import run_on_executor


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("index page:{}".format(time.time()))


class NonBlockHandler(tornado.web.RequestHandler):
    # 指定线程池的数量
    executor = ThreadPoolExecutor(4)

    @gen.coroutine
    def get(self):
        ret = yield self.doing()
        self.write("non blocking {}".format(ret))
    
    @run_on_executor
    def doing(self):
        time.sleep(10)
        ret = time.time()
        return ret


app = tornado.web.Application(handlers=[
    (r"/", IndexHandler),
    (r"/nonblock", NonBlockHandler)
], debug=True)


if __name__ == "__main__":
    print("listenging on port 8000")
    try:
        app.listen(8000)
        tornado.ioloop.IOLoop.current().start()
    except Exception as e:
        print(e)
        tornado.ioloop.IOLoop.current().stop()
