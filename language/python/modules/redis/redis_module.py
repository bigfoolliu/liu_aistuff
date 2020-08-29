#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
redis模块简单使用
"""

import redis


def basic_set_get(r):
    """基础的设置和获取键值对"""
    # 设置键值对
    ret = r.set("key1", "value1")
    print("[INFO]set key result: {}".format(ret))
    # 获取键值对并将结果返回
    key1 = r.get("key1")
    print("[INFO]key1: {}".format(key1))
    # 删除键值对
    ret = r.delete("key1")
    print("[INFO]delete key result: {}".format(ret))
    print("[INFO]key1: {}".format(r.get("key1")))


def pipeline_command(r):
    """使用pipeline管道缓冲多条命令执行"""
    # 创建一个管道，transaction为默认为True保证各命令原子执行
    pipe = r.pipeline(transaction=False)
    pipe.set("key_pipeline", "vlaue_pipeline")
    pipe.get("key_pipeline")
    ret = pipe.execute()  # 执行管道内的一系列命令
    print("[INFO]pipeline result: {}".format(ret))


def pubsub_sub_command(r):
    """订阅频道以及接受新消息的pubsub对象"""
    # 创建一个pubsub对象
    p = r.pubsub()
    # 订阅频道(2个)
    p.subscribe("channel1", "channel2")
    p.subscribe("my-*")  # 遵守正则表达式的法式
    msg = p.get_message()
    print("[INFO]msg from channels: {}".format(msg))


def pubsub_pub_command(r):
    """发布频道"""
    r.publish("my-first-channel", "my-first-channel-data")  # 使用redis实例发布


if __name__ == "__main__":
    pool = redis.ConnectionPool(host="localhost", port=6379, db=0)
    r = redis.Redis(connection_pool=pool)

    # basic_set_get(r)
    # pipeline_command(r)

    pubsub_sub_command(r)
    pubsub_pub_command(r)
