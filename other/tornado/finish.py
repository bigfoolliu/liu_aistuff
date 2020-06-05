#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("done")
        self.finish()
        print("after finish")


application = tornado.web.Application([
    (r"/index", IndexHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
