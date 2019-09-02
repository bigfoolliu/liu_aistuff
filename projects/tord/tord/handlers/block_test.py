#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 阻塞的接口，调用之后，其他的接口将不能访问

import time

from tord.handlers.base import BaseHandler


class BlockHandler(BaseHandler):
    
    def get(self):
        time.sleep(10)
        self.write_success_json("block test")
