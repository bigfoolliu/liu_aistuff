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

import time
import asyncio
import threading


class DA(threading.Thread):

    def __init__(self):
        super().__init__()
        self.stopped = threading.Event()

    async def say_after(self, delay, what):
        await asyncio.sleep(delay)
        print(what)

    async def tasks(self):
        print(f"started at {time.strftime('%X')}")  # 注意此处的格式

        tasks = []
        for i in range(10):
            task = asyncio.create_task(self.say_after(i+1, "ha {}".format(i)))
            tasks.append(task)
        
        for task in tasks:
            await task

        print(f"finished at {time.strftime('%X')}")

    def run(self):
        while not self.stopped.wait(5):
            try:
                asyncio.run(self.tasks())
                # asyncio.get_event_loop().run_until_complete(asyncio.gather(self.tasks))
            except Exception as e:
                print(e)

    def stop(self):
        self.stopped.set()


DA().run()
