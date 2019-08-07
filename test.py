#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import time
import asyncio
import threading
import os

# class DA(threading.Thread):

#     def __init__(self):
#         super().__init__()
#         self.stopped = threading.Event()

#     async def say_after(self, delay, what):
#         await asyncio.sleep(delay)
#         print(what)

#     async def tasks(self):
#         print(f"started at {time.strftime('%X')}")

#         tasks = []
#         for i in range(10):
#             task = asyncio.create_task(self.say_after(i+1, "ha {}".format(i)))
#             tasks.append(task)
        
#         for task in tasks:
#             await task

#         print(f"finished at {time.strftime('%X')}")
    
#     def run(self):
#         while not self.stopped.wait(5):
#             try:
#                 asyncio.run(self.tasks())
#                 # asyncio.get_event_loop().run_until_complete(asyncio.gather(self.tasks))
#             except Exception as e:
#                 print(e)
    
#     def stop(self):
#         self.stopped.set()


# DA().run()

path = os.path.dirname(os.path.abspath(__file__))
print(path)

print(os.path.join(path, "templates/404.html"))