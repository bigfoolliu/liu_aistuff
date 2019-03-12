#!/usr/bin/env python
#!coding:utf-8


import tensorflow as tf
from utils import input_data

# 使用google提供的程序下载mnist数据集
# mnist = input_data.read_data_sets("dataset/mnist_data/", one_hot=True)


"""
mnist数据集中的图片为28*28的像素，
训练数据集有60000张图片，将其当作[60000, 784]的张量，前一个维度数字索引，第二个维度数字用来索引每张图片中的像素点，
在该张量中的每一个元素，都表示某张图片里的某个像素的强度值，介于0-1之间

此处使用标签数据为'one-hot vector',用来表示是哪个数字，如标签0为([1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
因此mnist.train_labels是一个[60000, 10]的数字矩阵


使用softmax回归模型来给不同的对象分配概率：
1. 对图片的像素值进行加权求和，不属于该类则权值为负数，属于则为整数
2. 加入一个额外的偏置量(bias)

softmax可以看作为一个激励函数(activation)或者链接(link)函数
"""


