#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
数据类型转换
sklearn默认将数据类型是float64
"""


import numpy as np
from sklearn import random_projection

# 伪随机数生成器
rng = np.random.RandomState(0)
# print("rng: ", rng)


X = rng.rand(50, 2000)
X = np.array(X, dtype="float32")
print("X: {} type: {}".format(X, X.dtype))


transformer = random_projection.GaussianRandomProjection()
X_new = transformer.fit_transform(X)
print("X_new: {} type: {}".format(X, X.dtype))
