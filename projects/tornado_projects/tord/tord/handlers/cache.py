#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu

"""
使用redis实现缓存页面

python对redis的操作: https://www.cnblogs.com/guotianbao/p/8683037.html

python的redis缓存实现：https://www.lizenghai.com/archives/13655.html
"""

import tornado.web
import redis


# 创建redis的连接池并实例化redis对象
pool = redis.ConnectionPool(host="localhost", port=6379)
r = redis.Redis(connection_pool=pool)


class CacheHandler(tornado.web.RequestHandler):

    def flush(self, include_footers=False, callback=None):
        """flush会将已经write的内容先刷新到浏览器"""
        self._data_html = self._write_buffer
        super(CacheHandler, self).flush(include_footers, callback)

    def get(self, *args, **kwargs):
        # 直接从redis数据库中获取数据
        ret = r.get("index")
        print(ret)
        if ret:
            self.write(ret)
            return
        import time
        self.render("index.html", time=time.time())
        r.set("index", self._data_html[0], ex=10)  # 设置过期时间为10s
