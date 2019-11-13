#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
pika模块

python操作RabbitMQ详解：https://www.cnblogs.com/shenh/p/10497244.html
python操作RabbitMQ：https://segmentfault.com/a/1190000017277218

- consumer处理消息
"""


import pika


# mq的用户名和密码
credential = pika.PlainCredentials("admin", "123456")

# 设置连接
host = ""
connection = pika.BlockingConnection(pika.ConnectionParameters(host=host, port=5672, virtual_host="/", credentials=credential))

channel = connection.channel()
channel.queue_declare(queue="python_test", durable=False)


def call_back(ch, method, properties, body):
    """
    定义一个回调函数来处理消息队列中的消息，此处的处理方式是打印出来
    注意：此回调函数固定要四个参数
    """
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print(body.decode())


# 将消息队列中的数据取出来回调给回调函数
channel.basic_consume(call_back, queue="python_test")
channel.start_consuming()
