#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


from tord.handlers.base import BaseHandler


class IndexHandler(BaseHandler):
    
    def get(self):
        self.write("hello, tornado")
        self.write_success()
