#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
tornado同步阻塞的示例

1. 访问 http://127.0.0.1:8888/index 得到结果
2. 访问 http://127.0.0.1:8888/blocking 会阻塞（标签一直转圈）
3. 立即接着 访问 http://127.0.0.1:8888/index 也会阻塞
"""


import time
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('index')


def doing():
    time.sleep(10)
    return 'Blocking'


class BlockingHandler(tornado.web.RequestHandler):
    
    def get(self):
        result = doing()
        self.write(result)


application = tornado.web.Application([
    (r"/index", IndexHandler),
    (r"/blocking", BlockingHandler),
])


if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
