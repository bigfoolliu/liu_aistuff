#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
python协程：https://thief.one/2017/02/20/Python%E5%8D%8F%E7%A8%8B/

python协程官方文档：
https://docs.python.org/zh-cn/3/library/asyncio-task.html

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


# import time
# import random
# import requests
# import gevent


# class Worker():

#     def __init__(self, name):
#         self.name = name
    
#     def ping(self):
#         print("{} ping starts".format(self.name))
#         html = yield requests.get("hhttp://www.baidu.com")
#         status = html.status_code
#         data = html.content
#         print("{} ping ends".format(self.name))
#         return status, data


# workers = [Worker(i) for i in range(10)]
# for worker in workers:
#     print(worker)
#     task = worker.ping()
#     next(task)


# def long_task(i):
#     print("{} starts".format(i))
#     time.sleep(random.randint(1, 6))
#     print("{} ends".format(i))


# tasks = [gevent.spawn(long_task, i) for i in range(5)]
# gevent.joinall(tasks)


# import asyncio


# async def compute(x, y):
#     print("Compute %s + %s ..." % (x, y))
#     await asyncio.sleep(1.0)
#     return x + y


# async def print_sum(x, y):
#     result = await compute(x, y)
#     print("%s + %s = %s" % (x, y, result))


# loop = asyncio.get_event_loop()
# print("start")
# loop.run_until_complete(print_sum(1, 2))
# print("end")
# loop.close()


# from tornado import gen
# import random


# def long_task(i):
#     print("start {}".format(i))
#     time.sleep(random.randint(1, 5))
#     print("end {}".format(i))
#     return(i)


# # @gen.coroutine
# def tasks():
#     for i in range(5):
#         ret = yield long_task(i)
#         print(ret)


# tasks()


import time
import asyncio


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main():
    task1 = asyncio.create_task(
        say_after(1, 'hello'))

    task2 = asyncio.create_task(
        say_after(2, 'world'))

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)
    await task1
    await task2

    print(f"finished at {time.strftime('%X')}")


asyncio.run(main())
