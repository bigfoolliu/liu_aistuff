#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
redis queue输出
"""
import time

from redis_queue import RedisQueue


q = RedisQueue("rq")

while True:
    ret = q.get_nowait()
    if not ret:
        break
    print("data {} out of queue {}".format(ret, time.strftime("%c")))
    time.sleep(2)
