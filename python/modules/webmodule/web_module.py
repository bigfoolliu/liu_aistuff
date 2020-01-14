#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
web模块使用

博文：简单而直接的python web框架： web.py:
https://blog.csdn.net/qq_22194315/article/details/79114533
"""


import web


urls = (
    "/", "index",
)


app = web.application(app, globals())


class index(object):
    def GET(self):
        return "index"


if __name__ == "__main__":
    app.run()
    