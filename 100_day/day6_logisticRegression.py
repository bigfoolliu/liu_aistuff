#!/usr/bin/env python
# --*- coding:utf-8 -*-


"""
logistic回归
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix


# step1:数据预处理
dataset = pd.read_csv("./datasets/Social_Network_Ads.csv")
X = dataset.iloc[:, [2, 3]].values  # Age和EstimatedSalary
Y = dataset.iloc[:, 4].values  # Purchased
print("X: {}\nY: {}".format(X, Y))
print("X type: {} and len: {}\nY type: {} and len: {}".format(type(X), len(X), type(Y), len(Y)))

# 数据分割
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.25, random_state=0)
print("X_train: {}\nX_test: {}\n,Y_train: {}\n,Y_test: {}".format(X_train, X_test, Y_train, Y_test))

plt.figure(figsize=(15, 8))
plt.subplot(2, 2, 1)
plt.scatter(X_train[:, 0], X_train[:,1], color="red")
plt.title("Logistic Regression(Training Set)")
plt.xlabel("Age")
plt.ylabel("EstimatedSalary")

plt.subplot(2, 2, 2)
plt.scatter(X_test[:, 0], X_test[:,1], color="red")
plt.title("Logistic Regression(Test Set)")
plt.xlabel("Age")
plt.ylabel("EstimatedSalary")

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


# step5:可视化结果
# plt.scatter(X_train[:, 0], X_train[:,1], color="red")
# plt.plot(X_train, classifier.predict(X_train), color="blue")

# plt.scatter(X_test, Y_test, color="green")
# plt.plot(X_test, classifier.predict(X_test), color="blue")

plt.show()