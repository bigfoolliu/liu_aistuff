#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
实现恶意登录保护的简单示例
一小时内每个用户最多登录5次
"""


import sys
import time

import redis


r = redis.Redis(host="127.0.0.1", port=6379, db=0)

try:
    user_id = sys.argv[1]
except Exception:
    print("input user_id error")
    sys.exit(0)

if r.llen(user_id) >= 5 and time.time() - float(r.lindex(user_id, 4)) <= 3600:
    print("you are forbidden to login")
else:
    print("you are allowed to login")
    r.lpush(user_id, time.time())
    # login()
