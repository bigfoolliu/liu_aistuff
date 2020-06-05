#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
训练神经网络解决最基本的二分类问题
即: yes or no问题
"""

import tensorflow as tf
import numpy as np
# RandomState是numpy的一个伪随机数生成器
from numpy.random import RandomState

# 定义训练数据集批次的大小，即每批数据量的大小
BATCH_SIZE = 8

# 定义神经网络的参数(编造的,参考forward_propagation.py)
w1 = tf.Variable(tf.random_normal([2, 3], stddev=1))
w2 = tf.Variable(tf.random_normal([3, 1], stddev=1))
print("[INFO]w1, w2 define complete.")

# placeholder作为存放数据的地方,在shape的一个维度上使用None可以方便使用不大的batch大小，训练时需要将数据分成较小的batch．数据集小时可方便测试，数据集大时将大量数据放入一个batch可能导致内存溢出
x = tf.placeholder(tf.float32, shape=(None, 2), name="x-input")
y_ = tf.placeholder(tf.float32, shape=(None, 1), name="y-input")

print("[INFO]shape x:{} w1:{} w2:{}".format(x.shape, w1.shape, w1.shape))

# 定义神经网络前向传播的过程
a = tf.matmul(x, w1)
y = tf.matmul(a, w2)
print("[INFO]calculate complete.")

# 定义损失函数和反向传播的算法
cross_entropy = -tf.reduce_mean(y_ * tf.log(tf.clip_by_value(y, 1e-10, 1.0)))
train_step = tf.train.AdamOptimizer(0.001).minimize(cross_entropy)

# 通过随机数生成一个模拟数据集
rdm = RandomState(1)
dataset_size = 128
X = rdm.rand(dataset_size, 2)  # X: 128 * 2 ndarray
# 定义规则来给出样本的标签，比如 x1+x2<1的为正样本，其余为负样本
Y = [[int(x1 + x2 < 1)] for (x1, x2) in X]
# 创建会话来运行
with tf.Session() as sess:
    init_op = tf.initialize_all_variables()
    print("[INFO]init_op:\n", sess.run(init_op))
    print("[INFO]w1:\n", sess.run(w1))
    print("[INFO]w2:\n", sess.run(w2))

    # 设定训练的轮数
    STEPS = 5000
    for i in range(STEPS):
        # 每次选取BATCH_SIZE个样本进行训练
        start = (i * BATCH_SIZE) % dataset_size
        end = min(start + BATCH_SIZE, dataset_size)
        # 通过选取的样本训练神经网络参数并更新参数
        sess.run(train_step, feed_dict={x: X[start:end], y_: Y[start:end]})
        if i % 1000 == 0:
            # 每次隔一段时间计算在所有数据上的交叉熵并输出
            total_cross_entropy = sess.run(cross_entropy, feed_dict={x: X, y_: Y})
            print("[INFO]after {} training steps(s), cross_entropy on all data is {}".format(i, total_cross_entropy))

    print("[INFO]after {} times trained, w1:\n{}.".format(STEPS, sess.run(w1)))
    print("[INFO]after {} times trained, w2:\n{}.".format(STEPS, sess.run(w2)))
