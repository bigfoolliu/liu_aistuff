#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


import tensorflow as tf


a = tf.constant(10)
b = tf.constant(20)

# 使用with可以自动关闭Session()
with tf.Session() as sess:
    ret = sess.run(a + b)
    print("ret:", ret)
