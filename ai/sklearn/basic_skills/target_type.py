#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
查看目标值 y 的类型

binary                      y 包含 <=2 个的离散数值，并且是一个1d或者列向量
continuous                  y 是一个非全是整数的 array-like 的浮点数，并且是一个1d或者列向量
multiclass                  y 包含2个以上离散的数值，并且是一个1d或者列向量
multiclass-multioutput      y 是一个包含2个以上离散数值的2d的数组，并且不是一系列序列，每个维度的的size > 1
multilabel-indicator        y 是一个标签指示符矩阵，包含至少两列的两个维度的数组，最多2个唯一值
unknown
"""

import numpy as np
from sklearn.utils.multiclass import type_of_target

print(__doc__)

continuous = type_of_target([0.1, 0.6])
binary = type_of_target([1, -1, -1, 1])
mulclass = type_of_target([0, 2, 1])
muloutput = type_of_target(np.array([[1, 2], [3, 1]]))
mulindicator = type_of_target(np.array([[0, 1], [1, 1]]))

print("continuous  : ", continuous)
print("binary      : ", binary)
print("mulclass    : ", mulclass)
print("muloutput   : ", muloutput)
print("mulindicator: ", mulindicator)
