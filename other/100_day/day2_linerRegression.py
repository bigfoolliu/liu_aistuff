#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
简单的线性回归实例(一元)
"""
# import numpy as np
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# step1:获取数据
cur_dir = os.path.dirname(__file__)
file_path = os.path.join(cur_dir, "datasets/studentscores.csv")

dataset = pd.read_csv(file_path)
X = dataset.iloc[:, :1].values
Y = dataset.iloc[:, 1].values


X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

# step2:将线性回归模型应用到训练集
regressor = LinearRegression()
regressor = regressor.fit(X_train, Y_train)


# step3:预测结果
Y_pred = regressor.predict(X_test)


# step4:可视化结果
plt.scatter(X_train, Y_train, color="red")
plt.plot(X_train, regressor.predict(X_train), color="blue")

plt.scatter(X_test, Y_test, color="green")
plt.plot(X_test, regressor.predict(X_test), color="blue")

# plt.legend()
plt.show()
