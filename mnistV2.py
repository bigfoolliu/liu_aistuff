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
W_conv2 = weight_variable([5, 5, 32, 64])
b_conv2 = bias_variable([64])

h_conv2 = tf.nn.relu(conv2d(h_pool1, W_conv2) + b_conv2)
h_pool2 = max_pool_2x2(h_conv2)


"""
密集连接层
"""
W_fc1 = weight_variable([7 * 7 * 64, 1024])
b_fc1 = bias_variable([1024])

h_pool2_flat = tf.reshape(h_pool2, [-1, 7 * 7 *64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat, W_fc1) + b_fc1)


"""
Dropout
"""
keep_prob = tf.placeholder("float")
h_fc1_drop = tf.nn.dropout(h_fc1, keep_prob)


"""
输出层
"""
W_fc2 = weight_variable([1024, 10])
b_fc2 = bias_variable([10])
y_conv = tf.nn.softmax(tf.matmul(h_fc1_drop, W_fc2) + b_fc2)


"""
训练和评估模型
"""
cross_entropy = -tf.reduce_sum(y_ * tf.log(y_conv))
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
correct_prediction = tf.equal(tf.argmax(y_conv, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

sess.run(tf.initialize_all_variables())

for i in range(200):
    print("[INFO]{}:begin test {}".format(datetime.datetime.now().isoformat(), i))

    batch = mnist.train.next_batch(50)
    if i % 100 == 0:
        train_accuracy = accuracy.eval(feed_dict={x: batch[0], y_:batch[1], keep_prob: 1.0})
        print("[INFO]train {}, training accuracy {}".format(i, train_accuracy))

    train_step.run(feed_dict={x: batch[0], y_: batch[1], keep_prob: 0.5})

print("[INFO]test accuracy {}".format(accuracy.eval(feed_dict={x: mnist.test.images, y_: mnist.test.labels, keep_prob: 1.0})))

