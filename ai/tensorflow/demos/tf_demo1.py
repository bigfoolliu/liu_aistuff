#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


import tensorflow as tf


hello = tf.constant("hello, tensorflow")

# Session类用来执行tf的操作
sess = tf.Session()
ret = sess.run(hello)  # 执行
print("ret:{}".format(ret.decode("utf-8")))
sess.close()  # 关闭
