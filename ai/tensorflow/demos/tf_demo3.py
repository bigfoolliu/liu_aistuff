#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


import tensorflow as tf


# 张量可以被简单理解为多维数组，张量并不真正保存数字，保存的是如何得到这些数字的计算过程
a = tf.constant([1, 2, 3], name="a")
b = tf.constant([4, 5, 6], name="b")

# 运行之后得到的不是加法的结果，而是对结果的一个引用
ret = tf.add(a, b, name="ret")
print("ret:", ret)

# 结果与上面相同
ret2 = a - b
print("ret2:", ret2)
