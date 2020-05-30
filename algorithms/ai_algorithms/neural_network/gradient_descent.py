#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
梯度下降算法:
- 类比一个下山的过程
- 下山的人就是反向传播算法
- 下山的路径就是代表这算法中一直在寻找的参数
- 山上当前点最陡峭的方向实际上就是代价函数在这一点的梯度方向
- 观测最陡峭方向所用的工具就是微分

梯度:
- 梯度为对每个变量进行微分，然后用逗号隔开
- 单变量函数中梯度就是函数的微分
- 多变量函数中梯度是一个向量，梯度的方向指出了函数在给定点上升最快的方向(因此下降最快要加负号)


此处实现一个简单的梯度下降算法，场景为线性回归，用梯度下降法来拟合一条直线
代价函数使用'均方误差代价函数'
"""
import numpy as np
import matplotlib.pyplot as plt

m = 20
X0 = np.ones((m, 1))
X1 = np.arange(1, m + 1).reshape(m, 1)

# x
X = np.hstack((X0, X1))
# y
y = np.array([
    3, 4, 5, 5, 2, 4, 7, 8, 11, 8, 12,
    11, 13, 13, 16, 17, 18, 17, 19, 21
]).reshape(m, 1)

alpha = 0.01  # 学习率


# print("m: {}\nalpha: {}\nX0: {}\nX1: {}\nX: {}\ny: {}".format(m, alpha, X0, X1, X, y))


def error_func(theta, X, y):
    """误差函数J，返回均方误差"""
    diff = np.dot(X, theta) - y
    return (1. / 2 * m) * np.dot(np.transpose(diff), diff)


def gradient_func(theta, X, y):
    """J函数的梯度"""
    diff = np.dot(X, theta) - y
    return (1. / m) * np.dot(np.transpose(X), diff)


def gradient_descent(X, y, alpha, error=1e-5):
    """
    应用梯度下降
    :param error: 误差
    """
    theta = np.array([1, 1]).reshape(2, 1)
    gradient = gradient_func(theta, X, y)
    # 当误差在1e-5之内结束梯度下降过程
    while not np.all(np.absolute(gradient) <= error):
        theta = theta - alpha * gradient
        gradient = gradient_func(theta, X, y)
    return theta


# 计算
optimal = gradient_descent(X, y, alpha, error=1000)
print("[INFO]optimal: {}".format(optimal))
print("[INFO]error func: {}".format(error_func(optimal, X, y)[0, 0]))

# 图形化展示
fig = plt.figure()
plt.scatter(X1, y)

x1 = np.linspace(0, 20, num=200)
theta0 = optimal[0][0]
theta1 = optimal[1][0]
y1 = theta0 + theta1 * x1
plt.scatter(x1, y1, linewidths=0.2)

plt.title("gradient descent algorithm for liner-regression")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
