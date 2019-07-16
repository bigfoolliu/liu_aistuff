#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


import tornado.web
import tornado.ioloop


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("hello, tornado")
        self.set_status(200)
        self.finish()


if __name__ == "__main__":
    app = tornado.web.Application([
        (r"/", IndexHandler),
    ])
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
