#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


import tornado.web


class BaseHandler(tornado.web.RequestHandler):
    
    def get(self):
        raise NotImplementedError
    
    def post(self):
        raise NotImplementedError
    
    def write_success(self, reason=None):
        self.set_status(200, reason=reason)
        self.finish()
