#!/usr/bin/env python
#!coding:utf-8


import tensorflow as tf


a = tf.constant(10)
b = tf.constant(20)

# 使用with可以自动关闭Session()
with tf.Session() as sess:
    ret = sess.run(a + b)
    print("ret:", ret)
