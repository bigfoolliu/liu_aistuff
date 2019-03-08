#!/usr/bin/env python
#!coding:utf-8


"""
展示神经网络实现输出结果的前向传播算法
"""


import tensorflow as tf


# 声明两个变量,元素为均值为1，标准差为1的随机数
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1, seed=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1, seed=1))

# 暂时将输入的特征向量设为常量
x = tf.constant([[0.7, 0.9]])

# 计算,矩阵乘法
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)

# 定义会话运算
sess = tf.Session()

# 初始化变量方式1
#sess.run(w1.initializer)
#sess.run(w2.initializer)

# 初始化变量方式2
init_op = tf.initialize_all_variables()
sess.run(init_op)

ret = sess.run(y)
print("[INFO]ret:{} shape:{}".format(ret, ret.shape))
sess.close()

