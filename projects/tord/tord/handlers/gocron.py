#!/usr/bin/env python3
# -*- coding:utf-8 -*-


from tord.handlers import base


class TestHandler(base.BaseHandler):

    def post(self):
        data = self.parse_json_body()
        self.finish(data)
