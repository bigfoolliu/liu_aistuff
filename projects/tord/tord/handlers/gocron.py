#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from tord.handlers import base


class TestHandler(base.BaseHandler):

    def post(self):
        data = self.request.body
        self.write(data)
        self.finish()
