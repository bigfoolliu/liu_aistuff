#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
k-近邻分类器demo
"""


from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


iris = datasets.load_iris()
X_train = iris["data"][:-10, :2]  # 取前两个特征进行训练
y_train = iris["target"][:-10]


n_neighbors = 10
h = 0.02

# 设置颜色
# cmap_light = ListedColormap(["#DC143C", "#0000FF", "#32CD32"])
cmap_light = ListedColormap(["#DC143C", "#0000FF", "#32CD32"])
# cmap_bold = ListedColormap(["#FF1493", "#000080", "#008000"])
cmap_bold = ListedColormap(["#FF1493", "#000080", "#008000"])


# 从不同的角度来分类
# uniform表示所有点的权重相同，点多的则取那个类
# distance表示距离近的权重高，是加权
for weight in ["uniform", "distance"]:
    clf = KNeighborsClassifier(n_neighbors=n_neighbors, weights=weight)
    clf.fit(X_train, y_train)

    x_min, x_max = X_train[:, 0].min() - 1, X_train[:, 0].max() + 1  # 坐标轴的范围
    y_min, y_max = X_train[:, 1].min() - 1, X_train[:, 1].max() + 1

    # 画分类图
    xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    Z = Z.reshape(xx.shape)

    plt.figure()
    plt.pcolormesh(xx, yy, Z, cmap=cmap_light)

    plt.scatter(X_train[:, 0], X_train[:, 1], c=y_train, cmap=cmap_bold, edgecolors='k', s=20)
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())

    plt.title("3-class classification (k={}, weight={})".format(n_neighbors, weight))

plt.show()
