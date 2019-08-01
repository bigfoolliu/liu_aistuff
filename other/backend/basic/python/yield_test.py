#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
协程可以身处四个状态中的一个。当前状态可以使用inspect.getgeneratorstate(…) 函数确定，该函数会返回下述字符串中的一个： 

1. GEN_CREATED：等待开始执行 
2. GEN_RUNNING：解释器正在执行 
3. GEN_SUSPENED：在yield表达式处暂停 
4. GEN_CLOSED：执行结束
"""

# def averager():
#     total = 0.0
#     count = 0
#     avg = None

#     while True:
#         num = yield avg
#         total += num
#         count += 1
#         avg = total/count

# # run
# ag = averager()
# # 预激协程,协程执行到yield表达式，将yield后的结果返回
# print(next(ag))     # None

# # send激活协程，将发送的值赋给yield之前的num，print打印yield返回的值
# print(ag.send(10))  # 10
# print(ag.send(20))  # 15


import time
import random
import requests


class Worker():

    def __init__(self, name):
        self.name = name
    
    def ping(self):
        print("{} ping starts".format(self.name))
        html = yield requests.get("hhttp://www.baidu.com")
        status = html.status_code
        data = html.content
        print("{} ping ends".format(self.name))
        return status, data


workers = [Worker(i) for i in range(10)]
for worker in workers:
    print(worker)
    task = worker.ping()
    next(task)
