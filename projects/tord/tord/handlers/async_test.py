#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import time
from concurrent.futures import ThreadPoolExecutor

import requests
import tornado
import tornado.web


class Executor(ThreadPoolExecutor):
    """
    创建多线程的线程池，线程池的大小为10
    创建多线程时使用了单例模式，如果Executor的_instance实例已经被创建，
    则不再创建，单例模式的好处在此不做讲解
    """
    _instance = None
 
    def __new__(cls, *args, **kwargs):
        if not getattr(cls, '_instance', None):
            cls._instance = ThreadPoolExecutor(max_workers=10)
        return cls._instance


# 全部协程+异步线程池实现，yield在此的作用相当于回调函数
# 经过压力测试发现，此种方式的性能在并发量比较大的情况下，要远远优于纯协程实现方案
class Handler(tornado.web.RequestHandler):
    """ 获取域名所关联的IP信息 """
    # executor为RequestHandler中的一个属性，在使用run_on_executor时，必须要用，不然会报错
    # executor在此设计中为设计模式中的享元模式，所有的对象共享executor的值
    executor = Executor()
 
    @tornado.web.asynchronous  # 异步处理
    @tornado.gen.coroutine  # 使用协程调度
    def get(self):
        """ get 接口封装 """
        # 可以同时获取POST和GET请求参数
        # value = self.get_argument("value", default=None)
        # result = yield self._process(value)

        result = yield self._long_task()
        self.set_status(200)
        self.write(result)

    @tornado.concurrent.run_on_executor  # 增加并发量
    def _process(self, url):
        # 此处执行具体的任务
        try:
            resp = requests.get(url)
        except IOError as e:
            print(e)
            return 'failed'

        return 'success'

    @tornado.concurrent.run_on_executor    
    def _long_task(self):
        time.sleep(10)
        self.set_status(201)
        return "success2"
