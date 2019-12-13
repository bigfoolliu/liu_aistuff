#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
tornado异步非阻塞实现之 协程+生成器

- 包含了 yield 关键字的函数是一个 生成器(generator). 所有的生成器都是异步的;
- 当调用它们的时候,会返回一个生成器对象,而不是一个执行完的结果. 
- @gen.coroutine 装饰器通过 yield 表达式和生成器进行交流, 而且通过返回一个 Future 与协程的调用方进行交互. 
- 协程一般不会抛出异常: 它们抛出的任何异常将被 Future 捕获 直到它被得到. 这意味着用正确的方式调用协程是重要的, 否则你可能有被忽略的错误。
- @gen.coroutine 可以让你的函数以异步协程的形式运行，但是依赖第三方的异步库，要求你的函数本身不是blocking的。例如os.sleep() 方法是blocking 的，没办法实现异步非阻塞。
"""


import time

import tornado.web
from tornado import gen


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("index page")


@gen.coroutine
def long_time_task():
    """
    模拟长时间耗时任务
    @gen.coroutine 装饰器之后，最终结果会返回一个可以被yield 的生成器 Future 对象
    与众不同的是这个函数的返回值需要以 raise gen.Return() 这种形式返回。
    """
    # time.sleep()是阻塞的，不能起到效果
    # yield time.sleep(10)
    yield gen.sleep(10)
    raise gen.Return("non block")


class NonBlockHandler(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self):
        ret = yield long_time_task()
        self.write("{} {}".format(ret, time.time()))


app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/nonblock", NonBlockHandler)
    ], debug=True)


if __name__ == '__main__':
    print("listening on port:", 8000)
    try:
        app.listen(8000)
        tornado.ioloop.IOLoop.current().start()
    except Exception as e:
        print(e)
        tornado.ioloop.IOLoop.current().stop
