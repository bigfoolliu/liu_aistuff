#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
asyncio模块的使用

- python异步编程入门(阮一峰)：http://www.ruanyifeng.com/blog/2019/11/python-asyncio.html
- asyncio模块就只有一个线程，多任务合作
- 允许异步任务交出执行权给其他任务，等到其他任务完成，再收回执行权继续往下执行
"""


import asyncio


@asyncio.coroutine
def hello():
    """耗时任务"""
    print("hello")
    # 异步调用asyncio.sleep()
    r = yield from asyncio.sleep(5)
    print("hello again")


def coroutine_demo():
    """使用异步协程的示例"""
    # 获取事件循环
    loop = asyncio.get_event_loop()
    loop.run_until_complete(hello())
    loop.close()


if __name__ == "__main__":
    coroutine_demo()
