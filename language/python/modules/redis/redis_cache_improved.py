#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu



"""
对网页部分的数据进行缓存，比如电商页面，全页缓存可能导致用户看到错误的商品数量

做法：
整个页面需要更新的只是商品信息，可以只对数据行进行缓存（商品在数据库对应的一行）。

1. 编写应该持续运行的守护进程函数，让这个函数将将指定的数据行缓存到redis中，并不定期的对这些缓存数据进行更新
2. 缓存数据编码为json字典存储到redis字符串中，数据列的名字被映射为json字典的键，数据行的值被映射为json字典的值
3. 通过ajax技术将缓存异步刷新
"""


import time
import json


def schedule_row_cache(conn, row_id, delay):
    # 两个有序集合
    # 存储对应id数据的缓存时间
    conn.zadd('delay:', row_id,delay)
    # 存储对应id数据下次更新时间
    conn.zadd('schedule:', row_id, time.time())


def cache_rows(conn):
    while True:
        # zrange返回有序集 key 中，指定区间内的成员。
        # 其中成员的位置按 score 值递增(从小到大)来排序。
        # 这里一直获取第一个成员
        # 返回一个或者零个元组的列表
        next = conn.zrange('schedule:', 0, 0, withscores=True)
        now = time.time()
        # 小于则需要缓存，大于则不需要
        if not next or next[0][1] > now:
            time.sleep(.05)
        # 获取对应id
        row_id = next[0][0]
        # 根据id获取缓存的时间
        delay = conn.zscore('delay:', row_id)
        if delay <= 0:
            conn.zrem('delay:', row_id)
            conn.zrem('delay:', row_id)
            conn.delete('inv:' + row_id)
            continue
        # 从数据库获取对应id下的数据
        row = get(row_id)
        # 更新
        conn.zadd('schedule:', row_id,now +  delay)
        # 更新缓存
        conn.set('inv:' + row_id, json.dumps(row.to_dict()))


def get(id):
    pass

