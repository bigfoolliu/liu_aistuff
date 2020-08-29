#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
pika模块

python操作RabbitMQ详解：https://www.cnblogs.com/shenh/p/10497244.html
python操作RabbitMQ：https://segmentfault.com/a/1190000017277218

- producer产生消息
"""

import json
import pika

# mq的用户名和密码
credential = pika.PlainCredentials("admin", "123456")

# 设置连接
host = "localhost"
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=host, port=5672, virtual_host="/", credentials=credential))

# 声明消息队列，消息将在这个队列中传递，如果不存在将创建
channel = connection.channel()
result = channel.queue_declare(queue="python_test")

# 想队列中插入数值,routing_key是对列名字
for i in range(10):
    message = json.dumps({"OrderId": "1000%s" % i})
    channel.basic_publish(exchange="", routing_key="python_test", body=message)
    print(message)
connection.close()
