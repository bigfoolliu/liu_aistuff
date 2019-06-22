#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


"""
设定不同的参数让模型重新训练
"""


import numpy as np
from sklearn import datasets
from sklearn.svm import SVC


digits = datasets.load_digits()
X, y = digits["data"][:-1], digits["target"][:-1]

clf = SVC()
clf.set_params(kernel="linear").fit(X, y)
print("clf: ", clf)

# 重新设置参数训练
clf.set_params(kernel="rbf", gamma="scale").fit(X, y)
print("clf new: ", clf)
