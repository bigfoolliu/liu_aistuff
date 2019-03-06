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


# 直接从tensorflow访问该数据集(一般的需要自己下载到本地)
#fashion_mnist = keras.datasets.fashion_mnist
#(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()  # 加载查看该数据集的基本信息


# 下载到本地进行访问(借助官方提供的一个函数)
from utils import mnist_reader
x_train, y_train = mnist_reader.load_mnist("dataset", kind="train")
x_test, y_test = mnist_reader.load_mnist("dataset", kind="t10k")

print("加载数据集完成.")
