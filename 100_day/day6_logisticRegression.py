#!/usr/bin/env python
# --*- coding:utf-8 -*-


"""
logistic回归
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix


# step1:数据预处理
dataset = pd.read_csv("./datasets/Social_Network_Ads.csv")
X = dataset.iloc[:, [2, 3]].values
Y = dataset.iloc[:, 4].values

# 数据分割
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)

# 特征提取
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.fit_transform(X_test)


# step2:构造logistic回归模型
classifier = LogisticRegression()
classifier.fit(X_train, Y_train)


# step3:预测
Y_pred = classifier.predict(X_test)


# step4:评估预测结果
cm = confusion_matrix(Y_test, Y_pred)
