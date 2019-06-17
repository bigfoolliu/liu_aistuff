#!/usr/bin/env python3
#!coding:utf-8


"""
线性模型

岭回归
一种改良的最小二乘估计法，通过放弃最小二乘法的无偏性，以损失部分信息，降低精度为代价获得回归系数更为实际的回归方法；
对病态数据（比如某一两个数据偏离的极大）的拟合要好于最小二乘法。

https://blog.csdn.net/aoulun/article/details/78688572
"""

from sklearn import linear_model
import numpy as np
import matplotlib.pyplot as plt


# X is 10*10 Hilbert matrix
X = 1.0 / (np.arange(1, 11) + np.arange(0, 10)[:, np.newaxis])
print("X: ", X)

y = np.ones(10)

# compute paths
n_alphas = 200
alphas = np.logspace(-10, -2, n_alphas)

coefs = []
for a in alphas:
    ridge = linear_model.Ridge(alpha=a, fit_intercept=False)
    ridge.fit(X, y)
    coefs.append(ridge.coef_)

# display results
ax = plt.gca()

ax.plot(alphas, coefs)
ax.set_xscale("log")
ax.set_xlim(ax.get_xlim()[::-1])

plt.xlabel("alpha")
plt.ylabel("weights")
plt.title("Ridge coefficients as a function of the regularization")

plt.axis("tight")
plt.show()
