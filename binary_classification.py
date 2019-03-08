#!/usr/bin/env python
#!coding:utf-8


"""
训练神经网络解决最基本的二分类问题
即: yes or no问题
"""

import tensorflow as tf
import numpy as np
from numpy.random import RandomState


# 定义训练数据集批次的大小
BATCH_SIZE = 8

# 定义神经网络的参数(编造的,参考forward_propagation.py)
w1 = tf.Variable(tf.random_normal([2, 3], stddev=2, seed=1))
w1 = tf.Variable(tf.random_normal([3, 1], stddev=2, seed=1))

# TODO
