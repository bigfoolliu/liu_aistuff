#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
基本数据处理
"""
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer  # 新
# from sklearn.preprocessing import Imputer  # 旧
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


FILE_PATH = "datasets/Data.csv"


# step1: 获取数据
# iloc通过行号来索引行数据
dataset = pd.read_csv(FILE_PATH)
X = dataset.iloc[:, : -1].values  # 取所有的行,列取到倒数第二行(倒数第一行不取)
Y = dataset.iloc[:, 3].values

print("[INFO]The data we got is:")
print("[INFO]X: {}\nY: {}\n".format(X, Y))


# step2: 预处理数据
# 处理丢失的数据
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")  # 新
# imputer = Imputer(missing_values="NaN", strategy="mean", axis=0)  # 旧
imputer = imputer.fit(X[:, 1:3])  # 将X[:, 1:3]所有缺失值替换
X[:, 1:3] = imputer.transform(X[:, 1:3])

print("[INFO]After preprocessing:")
print("[INFO]X: {}\n".format(X))


# step3: 对明确的数据进行编码
label_encoder_X = LabelEncoder()
X[:, 0] = label_encoder_X.fit_transform(X[:, 0])

# 创建一个dummy变量
one_hot_encoder = OneHotEncoder(categorical_features=[0])
X = one_hot_encoder.fit_transform(X).toarray()
label_encoder_Y = LabelEncoder()
Y = label_encoder_Y.fit_transform(Y)

print("[INFO]After encoding:")
print("[INFO]X: {}\nY: {}\n".format(X, Y))


# step4: 将数据分割为训练数据和测试数据
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=0
    )  # test_size参数表明将所有数据的20%作为测试数据


# step5: 特征提取
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)


print("[INFO]After scaling the features:")
print("[INFO]X_train: {}\nX_test: {}\n".format(X_train, X_test))
