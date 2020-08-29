#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
redis queue输入
"""

import time

from redis_queue import RedisQueue


# 新建队列名字为rq
q = RedisQueue("rq")

for i in range(5):
    q.put(i)
    print("input key: {} enqueue: {}".format(i, time.strftime("%c")))
    time.sleep(0.5)
