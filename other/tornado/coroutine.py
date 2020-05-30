#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
tornado异步非阻塞实现方式之一

协程 + 生成器

1. 访问 http://127.0.0.1:8888/index 得到结果
2. 访问 http://127.0.0.1:8888/nonblocking 会阻塞（标签一直转圈）
3. 立即接着 访问 http://127.0.0.1:8888/index 不会阻塞
"""


import tornado.web
from tornado import gen


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('index')


@gen.coroutine
def doing():
    """
    穿上@gen.coroutine 装饰器之后，最终结果会返回一个可以被yield 的生成器 Future 对象
    与众不同的是这个函数的返回值需要以 raise gen.Return() 这种形式返回。
    :return: Future object
    """
    # time.sleep(10)     # time.sleep() 是blocking 的，不支持异步操作，我刚开始测试tornado的时候坑了
    yield gen.sleep(10)  # 使用这个方法代替上面的方法模拟 I/O 等待的情况, 可以点进去看下这个方法的介绍
    raise gen.Return('Non-Blocking')


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
