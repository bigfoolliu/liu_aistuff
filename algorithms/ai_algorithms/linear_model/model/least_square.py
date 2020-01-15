#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
线性模型

最小二乘法
"""
from sklearn import datasets
from sklearn import linear_model
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt


# load the inside diabetes dataset
diabetes = datasets.load_diabetes()
# use the second feature only
diabetes_X = diabetes.data[:, np.newaxis, 2]

diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]

diabetes_y_train = diabetes.target[:-20]
diabetes_y_test =diabetes.target[-20:]

# construct a liner model
regr = linear_model.LinearRegression()

# train the model
regr.fit(diabetes_X_train, diabetes_y_train)

# test the model
diabetes_y_pred =  regr.predict(diabetes_X_test)

print("coeffients: {}".format(regr.coef_))  # 模型的系数
print("intercept: {}".format(regr.intercept_))  # 模型的截距
print("mean squared error: %.2f"%mean_squared_error(diabetes_y_test, diabetes_y_pred))  # 均方误差回归损失
print("variance score: %.2f"%r2_score(diabetes_y_test, diabetes_y_pred))  # 方差

plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, diabetes_y_pred, color='blue', linewidth=3)

# plt.xticks([0, 0.5])
# plt.yticks([0, 400])

plt.show()