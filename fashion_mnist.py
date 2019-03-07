#!/usr/bin/env python
#!coding:utf-8


"""
使用fashion mnist数据集训练一个最基础的图像分类的神经网络模型，
该数据集有60000张图像用于训练，10000张图片用于测试

图片尺寸: 28 * 28
"""

import tensorflow as tf
from tensorflow import keras  # 构建和训练模型的高阶API

import numpy as np
import matplotlib.pyplot as plt


# 数据集中的品类列表(T恤，裤子，套衫，裙子，外套，凉鞋，衬衫，运动鞋，包包，踝靴)
class_names = ["T-shirt", "Trouser", "Pullover", "Dress", "Coat", "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]


# 直接从tensorflow访问该数据集(一般的需要自己下载到本地)
#fashion_mnist = keras.datasets.fashion_mnist
#(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()  # 加载查看该数据集的基本信息


# 下载到本地使用python加载数据(借助官方提供的一个函数)
from utils import mnist_reader
x_train, y_train = mnist_reader.load_mnist("dataset", kind="train")
x_test, y_test = mnist_reader.load_mnist("dataset", kind="t10k")
# 将数据集转换:(60000, 784) ---> (60000, 28, 28)
x_train = x_train.reshape(60000, 28, 28)
x_test = x_test.reshape(10000, 28, 28)
print("x_train:\ntype:{}\nshape:{}\n".format(type(x_train), x_train.shape))
print("y_train:\ntype:{}\nshape:{}\n".format(type(y_train), y_train.shape))
print("x_test:\ntype:{}\nshape:{}\n".format(type(x_test), x_test.shape))
print("y_test:\ntype:{}\nshape:{}".format(type(y_test), y_test.shape))

# 使用tensorflow进行加载数据
#from tensorflow.examples.tutorials.mnist import input_data
#data = input_data.read_data_sets("dataset")
# data.train.next_batch(BATCH_SIZE)


# Test:检查训练集中的第一张图像
# plt.figure()
# plt.imshow(x_test[0])
# plt.colorbar()
# plt.grid(False)
# plt.show()


# 将这些值缩小到0-1之间
x_train = x_train / 255.0
x_test = x_test / 255.0

# 展示训练集中前25张图像，并在每张图像下显示类别名称
plt.figure(figsize=(10, 10))
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x_train[i], cmap=plt.cm.binary)
    plt.xlabel(class_names[y_train[i]])
plt.show()


# 1. 构建模型,首先构建模型的层，然后预编译模型
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),  # 网络第一层，将二维数组(28, 28)转换为一维数组(28 * 28 = 784)像素，该层没有要学习的参数，只改动数据的格式
    keras.layers.Dense(128, activation=tf.nn.relu),  #　网络包含两个Ｄense的序列，这些层是密集连接或全连接神经层，第一层有128节点(神经元)
    keras.layers.Dense(10, activation=tf.nn.softmax)  # 第二个Ｄense序列是有10个神经元的softmax层，该层返回一个具有10个概率得分的数组(表示为10个类别中某一个的概率)，得分总和为1
    ])
print("模型构建完成．")


# 2. 编译模型
model.compile(
        optimizer=tf.train.AdamOptimizer(),  # 优化器，根据模型看到的数据以及损失函数更新模型的方式
        loss='sparse_categorical_crossentropy',  # 损失函数，衡量模型训练期间的准确率，应该尽量小
        metrics=['accuracy']  # 指标，用于监控训练和测试步骤，此处使用准确率，即图像被正确分类的比例
        )

print("模型编译完成．")


# 3. 训练模型
model.fit(x_train, y_train, epochs=5)  # fit方法使模型和数据'拟合'
print("模型训练完成.")
