#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
学习和预测
"""


from sklearn import svm
from sklearn import datasets

digits = datasets.load_digits()

clf = svm.SVC(C=100, gamma=0.001)

clf.fit(digits["data"][:-1], digits["target"][:-1])
print("clf: ", clf)

pre_digit = clf.predict(digits["data"][-1:])
print("pre_digit: ", pre_digit)

print("pre_target: ", digits["target"][-1])
if pre_digit == digits["target"][-1]:
    print("predict true")
