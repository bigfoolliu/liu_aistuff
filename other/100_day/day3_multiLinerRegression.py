#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
多元线性回归
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


# 获取数据
dataset = pd.read_csv("datasets/50_Startups.csv")
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 4].values
print("The datas we got is :\nX: {}\nY: {}".format(X, Y))

# 数据编码
label_encoder = LabelEncoder()
X[:, 3] = label_encoder.fit_transform(X[:, 3])

one_hot_encoder = OneHotEncoder(categorical_features=[3])
X = one_hot_encoder.fit_transform(X).toarray()
print("After encoding, the data X: {}".format(X))

# 防止陷入死循环
X = X[:, 1:]

# 数据集分割
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=0
    )
print("After spiliting, X_train: {}\nX_test: {}\nY_train: {}\n\
    Y_test: {}".format(X_train, X_test, Y_train, Y_test))

# 将多元线性回归模型应用到训练集
regressor = LinearRegression()
regressor.fit(X_train, Y_train)

Y_pred = regressor.predict(X_test)
print("The prediction Y_pred: {}".format(Y_pred))
