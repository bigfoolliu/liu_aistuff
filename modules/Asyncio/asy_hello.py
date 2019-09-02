#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import asyncio

@asyncio.coroutine
def hello():
    print("hello")
    # 异步调用asyncio.sleep()
    r = yield from asyncio.sleep(2)
    print("hello again")


# 获取事件循环
loop = asyncio.get_event_loop()
loop.run_until_complete(hello())
loop.close()
