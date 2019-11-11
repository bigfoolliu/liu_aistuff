#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
redis构建任务队列
"""


import redis


class RedisQueue(object):

    """自定义一个redis队列"""

    def __init__(self, name, namespace="queue", **redis_kwargs):
        """redis默认参数，host="localhost", port=6375, db=0"""
        self.__db = redis.Redis(**redis_kwargs)
        self.key = "%s:%s" % (namespace, name)  # 注意此为队列的名字
    
    def qsize(self):
        """返回队列里面的任务的数量"""
        return self.__db.llen(self.key)
    
    def put(self, item):
        """将新的任务添加到队列末端"""
        self.__db.rpush(self.key, item)
    
    def get_wait(self, timeout=None):
        """返回队列的第一个元素，如果为空则等待直至有元素被加入队列，超时时间为None则一直等待"""
        item = self.__db.blpop(self.key, timeout=timeout)
    
    def get_nowait(self):
        """直接返回队列首个元素，如果队列为空则返回空"""
        item = self.__db.lpop(self.key)
        return item
