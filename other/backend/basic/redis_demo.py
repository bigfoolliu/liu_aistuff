#!/usr/bin/env python
# -*- coding:utf-8 -*-


"""
redis模块使用以及操作数据库


## 1. redis的pubsub

Pub/Sub: "发布/订阅",这个功能在redis中，被设计的非常轻量级和简洁，它做到了消息的“发布”和“订阅”的基本能力，但是尚未提供JMS中关于消息的持久化/耐久性等各种企业级的特性。
一个Redis client发布消息，其他多个redis client订阅消息，发布的消息“即发即失”，redis不会持久保存发布的消息；消息订阅者也将只能得到订阅之后的消息，通道中此前的消息将无从获得。这就类似于JMS中“非持久”类型的消息。

- 消息发布者，即publish客户端，无需独占链接，你可以在publish消息的同时，使用同一个redis-client链接进行其他操作（例如：INCR等）
- 消息订阅者，即subscribe客户端，需要独占链接，即进行subscribe期间，redis-client无法穿插其他操作，此时client以阻塞的方式等待“publish端”的消息；这一点很好理解，因此subscribe端需要使用单独的链接，甚至需要在额外的线程中使用。

一旦subscribe端断开链接，将会失去部分消息，即链接失效期间的消息将会丢失。

### 如果你非常关注每个消息，那么你应该考虑使用JMS或者基于Redis做一些额外的补充工作，如果你期望订阅是持久的，那么如下的设计思路可以借鉴(如下原理基于JMS)

1. subscribe端首先向一个Set集合中增加“订阅者ID”，此Set集合保存了“活跃订阅”者，订阅者ID标记每个唯一的订阅者，例如：sub:email,sub:web。此SET称为“活跃订阅者集合”
2. subcribe端开启订阅操作，并基于Redis创建一个以“订阅者ID”为KEY的LIST数据结构，此LIST中存储了所有的尚未消费的消息。此LIST称为“订阅者消息队列”
3. publish端：每发布一条消息之后，publish端都需要遍历“活跃订阅者集合”，并依次向每个“订阅者消息队列”尾部追加此次发布的消息。
4. 到此为止，我们可以基本保证，发布的每一条消息，都会持久保存在每个“订阅者消息队列”中。
5. subscribe端，每收到一个订阅消息，在消费之后，必须删除自己的“订阅者消息队列”头部的一条记录。
6. subscribe端启动时，如果发现自己的自己的“订阅者消息队列”有残存记录，那么将会首先消费这些记录，然后再去订阅。
"""
import redis

"""
创建一个连接池管理与redis数据库的连接
默认每个redis实例会创建自己的连接池,可以用已经存在的连接池覆盖实例redis的connection_pool参数来覆盖这一行为,
可以通过这种方式实现客户端的切分或连接池的管理
"""
pool = redis.ConnectionPool(host="localhost", port=6379, db=0)
r = redis.Redis(connection_pool=pool)


"""
redis-py 没有在客户端实例中实现 SELECT 命令。
如果要在同一个应用中使用多个 Redis 数据库，应该给第一个数据库创建独立的客户端实例（可能也需要独立的连接池）。
"""


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


# basic_set_get(r)
# pipeline_command(r)

pubsub_sub_command(r)
pubsub_pub_command(r)