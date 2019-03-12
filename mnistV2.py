#!/usr/bin/env python
#!coding:utf-8


import tensorflow as tf
from utils import input_data
import datetime

# 使用google提供的程序下载mnist数据集
mnist = input_data.read_data_sets("dataset/mnist_data/", one_hot=True)

# tf依赖于c++后端来进行计算，这里使用InteractiveSession类，可以更加灵活的构建你的代码，能让你在运行图的时候插入一些计算图，如果没有使用的话则需要在启动session之前构建整个计算图然后启动计算图
sess = tf.InteractiveSession()

# x表示一个占位符，运行计算时输入这个值，None表示第一维可以是任意的长度
x = tf.placeholder("float", shape=[None, 784])
y_ = tf.placeholder("float", shape=[None, 10])

# 一个Variable表示一个可修改的张量
W = tf.Variable(tf.zeros([784, 10]))  # 权重值
b = tf.Variable(tf.zeros([10]))  # 偏置值

"""
为提高准确率，构建一个多层的卷积神经网络
1. 权重初始化
2. 卷积和池化
"""
def weight_variable(shape):
    """构建权重值，避免在建立模型的时候反复初始化操作"""
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)


def bias_variable(shape):
    """构建偏置值"""
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)


def conv2d(x, W):
    """卷积"""
    return tf.nn.conv2d(x, W, strides=[1, 1, 1, 1], padding="SAME")


def max_pool_2x2(x):
    """池化"""
    return tf.nn.max_pool(x, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="SAME")


"""
第一层卷积
"""
W_conv1 = weight_variable([5, 5, 1, 32])
b_conv1 = bias_variable([32])

x_image = tf.reshape(x, [-1, 28, 28, 1])
h_conv1 = tf.nn.relu(conv2d(x_image, W_conv1) + b_conv1)
h_pool1 = max_pool_2x2(h_conv1)


"""
第二层卷积
"""
# TODO

sess.run(tf.initialize_all_variables())

# 类别预测和损失函数
y = tf.nn.softmax(tf.matmul(x, W) + b)
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))

# 训练模型
train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

for i in range(1000):
    print("[INFO]{}:begin test {}".format(datetime.datetime.now().isoformat(), i))
    batch = mnist.train.next_batch(50)
    train_step.run(feed_dict={x: batch[0], y_: batch[1]})

# 评估模型
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print("[INFO]accuracy:{}".format(accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels})))


