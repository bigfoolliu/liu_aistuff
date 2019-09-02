#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu

import requests
import tornado.web


class AsyncHandler(tornado.web.RequestHandler):

    @property
    def executor(self):
        return self.application.executor
    
    @tornado.gen.coroutine
    def async_worker(self, func, data):
        status, result = yield self.executor.submit(func, (data))
        if status == 200:
            self.set_status(200)
            self.write(result)
            self.finish()
        else:
            self.set_status(status)
            self.write(result)
            self.finish()


class Handler(AsyncHandler):

    def get(self, url=""):
        return self.async_worker(self.do_proxy, (requests.get, url))

    def do_proxy(self, data):
        func, url = data
        status, ret = func(url=url)
        self.set_status(status)
        self.write(ret)
        self.finish()


class LongTaskHandler(tornado.web.RequestHandler):

    @tornado.gen.Task
    def get(self):
        pass
