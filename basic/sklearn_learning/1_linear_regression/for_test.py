#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


import numpy as np
from linear_model import LinearRegressionModel

x_train = np.array([1, 2, 3])
y_train = np.array([4, 5, 6])
lr_test = LinearRegressionModel(x_train, y_train)

lr_test.run()
print(lr_test.lr.coef_)
print(lr_test.lr.intercept_)
