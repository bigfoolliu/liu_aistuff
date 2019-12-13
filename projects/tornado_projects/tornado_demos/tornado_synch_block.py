#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu



"""
tornado同步阻塞代码示例

1.访问 / 正常
2.访问 /block 阻塞5s，这5s内访问 / 会阻塞
3.10后 /block 返回结果，访问 / 也会正常
"""


import time

import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("index page")


class BlockHandler(tornado.web.RequestHandler):
    def get(self):
        ret = time.sleep(5)
        self.write("block page {}".format(ret))


app = tornado.web.Application([
        (r"/", IndexHandler),
        (r"/block", BlockHandler),
    ], debug=True)


if __name__ == "__main__":
    print("listening on port:", 8000)
    try:
        app.listen(8000)
        tornado.ioloop.IOLoop.instance().start()
    except Exception as e:
        print(e)
        tornado.ioloop.IOLoop.instance().stop()
