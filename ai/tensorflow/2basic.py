#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
使用变量实现一个简单的计数器
"""
import tensorflow as tf


# 创建一个常量，初始化为标量0
state = tf.Variable(0, name="state")

# 创建一个op,作用是使state增加1
one = tf.constant(1)
new_value = tf.add(state, one)
update = tf.assign(state, new_value)  # 将new_value的值重新赋给state

# 启动图后，变量需要经过初始化
init_op = tf.initialize_all_variables()

# 启动图后运行op
with tf.Session() as sess:
    sess.run(init_op)
    print("[INFO]state:{}".format(sess.run(state)))

    for _ in range(3):
        sess.run(update)
        print("[INFO]new state:{}".format(sess.run(state)))
