#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import time
import asyncio
import threading


class DA(threading.Thread):

    def __init__(self):
        super().__init__()
        self.stopped = threading.Event()
    
    @asyncio.coroutine
    def say_after(self, delay, what):
        r = yield from asyncio.sleep(delay)
        print(what)

    # async def tasks(self):
    #     print(f"started at {time.strftime('%X')}")

    #     tasks = []
    #     for i in range(10):
    #         task = asyncio.create_task(self.say_after(i+1, "ha {}".format(i)))
    #         tasks.append(task)
        
    #     for task in tasks:
    #         await task

    #     print(f"finished at {time.strftime('%X')}")
    
    def run(self):
        while not self.stopped.wait(5):
            print(f"start time at {time.strftime('%X')}")
            loop = asyncio.get_event_loop()
            try:
                tasks = [self.say_after(1, "hello"), self.say_after(2, "world")]
                loop.run_until_complete(asyncio.wait(tasks))
                
            except Exception as e:
                print(e)
            # loop.close()
            print(f"end time at {time.strftime('%X')}")
    
    def stop(self):
        self.stopped.set()


DA().run()