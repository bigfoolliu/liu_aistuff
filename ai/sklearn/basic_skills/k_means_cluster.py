#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


"""
k-means聚类展示
"""


from sklearn import cluster, datasets


iris = datasets.load_iris()

X = iris["data"]
y = iris["target"]

k_means = cluster.KMeans(n_clusters=3)
k_means.fit(X, y)

print("k_means: ", k_means)

labels = k_means.labels_[::10]
y_iris = y[::10]

print("labels: ", labels)  # 分类的情况
print("y_iris: ", y_iris)  # 实际情况
