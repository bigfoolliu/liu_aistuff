#!/usr/bin/env python
#!coding:utf-8


import tensorflow as tf
from utils import input_data
import datetime

# 使用google提供的程序下载mnist数据集
mnist = input_data.read_data_sets("dataset/mnist_data/", one_hot=True)


"""
mnist数据集中的图片为28*28的像素，
训练数据集有60000张图片，将其当作[60000, 784]的张量，前一个维度数字索引，第二个维度数字用来索引每张图片中的像素点，
在该张量中的每一个元素，都表示某张图片里的某个像素的强度值，介于0-1之间

此处使用标签数据为'one-hot vector',用来表示是哪个数字，如标签0为([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
因此mnist.train_labels是一个[60000, 10]的数字矩阵


使用softmax回归模型来给不同的对象分配概率：
1. 对图片的像素值进行加权求和，不属于该类则权值为负数，属于则为整数
2. 加入一个额外的偏置量(bias)

softmax可以看作为一个激励函数(activation)或者链接(link)函数:
y = softmax(Wx + b)


实现回归模型
1. 从外部计算切换回python的操作是巨大的开销(若是GPU的话更甚)
2. tf将复杂的运算放在python之外，但是不单独运行，首先用图描述一系列可交互的计算操作，然后全部一起在python之外运行

"""

# x表示一个占位符，运行计算时输入这个值，None表示第一维可以是任意的长度
x = tf.placeholder("float", [None, 784])

# 一个Variable表示一个可修改的张量
W = tf.Variable(tf.zeros([784, 10]))  # 权重值
b = tf.Variable(tf.zeros([10]))  # 偏置值

# 实现最简陋的模型
y = tf.nn.softmax(tf.matmul(x, W) + b)


# 训练模型
# 定义一个指标来评估这个模型的好坏，及成本(cost)或损失(loss),并劲来嗯最小化这个指标

# 最常见的一个成本函数就是＇交叉熵＇(cross-entropy)
# H(y) = -sum(y'log(y)), y是预测的概率分布，y'是实际的分布
y_ = tf.placeholder("float", [None, 10])
cross_entropy = -tf.reduce_sum(y_ * tf.log(y))


# tf拥有一张描述你各个计算单元的图，自动使用反向传播算法来有效确定变量是如何影响想要最小化的那个成本值的，然后tf会用你选择的优化算法来修改变量以降低成本

# 此处使用梯度下降算法以0.01的学习速率最小化交叉熵,tf将每个变量一点点往成本不断降低的方向移动
"""
tf这里实际上做的是在后台给描述你的计算的图里增加一系列新的计算操作单元，用于实现反向传播算法和梯度下降算法，返回的只是一个单一的操作，当运行该操作时，tf使用梯度下降算法训练模型，微调变量，不断减少成本
"""
learning_rate = 0.01
train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)

# 初始化创建的变量
init = tf.initialize_all_variables()

# 在一个会话中启动模型
sess = tf.Session()
sess.run(init)

# 开始训练模型
"""
模型循环训练1000次
该循环中的每个步骤中随机抓取训练数据中的100个批处理数据点，用这些数据点作为参数替换之前的占位符来运行train_step
因为如果每一次的训练都使用全部的数据将会需要很大的开销，每次训练使用不同的子集可以减少开销同时最大化的学习到数据集的总体特征
"""
train_loops = 1000
for i in range(train_loops):
    print("[INFO]{}:begin test {}.".format(datetime.datetime.now().isoformat(), i))
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})


# 评估模型
# tf.argmax(y, 1)返回的是模型对于任一预测到的标签值，tf.argmax(y_, 1)返回的是正确的标签
correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))  # 返回一组布尔值

# 将布尔值转换为浮点数，然后取平均值[True, False, True, False]变为[1, 0, 1, 0],然后取平均值0.5
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))

# 计算模型在测试数据集上的正确率
print("[INFO]accuracy:{}".format(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels})))

