#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
基础介绍
生成一些三维数据，然后用一个平面来拟合
"""
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# 生成假数据
x_data = np.float32(np.random.rand(2, 100))  # 2*100的矩阵
y_data = np.dot([0.100, 0.200], x_data) + 0.300  # y_data = [0.1, 0.2] * x_data + 0.3

# 构造一个线性模型
b = tf.Variable(tf.zeros([1]))
w = tf.Variable(tf.random_uniform([1, 2], -1.0, 1.0))  # 均匀分布
y = tf.matmul(w, x_data) + b

# 最小化方差
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)

# c初始化变量
init = tf.initialize_all_variables()

# 启动图
sess = tf.Session()
sess.run(init)

# 拟合平面
for step in range(200):
    sess.run(train)
    if step % 20 == 0:
        print("[INFO]step:{} w:{} b:{}".format(step, sess.run(w), sess.run(b)))

# 三维图像展示
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(x_data[0], x_data[1], y_data)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()
