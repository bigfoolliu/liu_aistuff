#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
加载数据集基本技能
"""


from sklearn import datasets
# import os


# 鸢尾花数据集（一般用于分类问题）
iris = datasets.load_iris()
# 数字图像数据集（一般用于分类问题）
digits = datasets.load_digits()

# print("iris: ", iris)
# print("digits: ", digits)


# 数字的样本特征和目标值
# print("digits data:", digits["data"])
# print("digits target", digits["target"])


# 数字的图像
print("digits 0: {} shape: {}".format(digits["images"][0], digits["images"][0].shape))
