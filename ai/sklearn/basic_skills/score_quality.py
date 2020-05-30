#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
通过估计器的score来评估模型的好坏
且score的值越大越好
"""


from sklearn import datasets
from sklearn import svm
# import numpy as np


digits = datasets.load_digits()

X = digits["data"]
y = digits["target"]

svc = svm.SVC(C=1, kernel="linear")
svc.fit(X[:-100], y[:-100])

score_pre = svc.score(X[-100:], y[-100:])

print("score_pre: ", score_pre)
