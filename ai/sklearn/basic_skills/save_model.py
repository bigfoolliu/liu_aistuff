#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
将训练完成的模型保存
"""


import pickle
from sklearn import svm
from sklearn import datasets

clf = svm.SVC(gamma="scale")
digits = datasets.load_digits()

X, y = digits["data"], digits["target"]

clf.fit(X, y)

# 将模型保存并写入文件
s = pickle.dumps(clf)
with open("./clf_model.bin", "wb") as f:
    f.write(s)

# 读取文件中的模型并预测
with open("./clf_model.bin", "rb") as f:
    s = f.read()
clf = pickle.loads(s)

pre_digit = clf.predict(digits["data"][-1:])
print("pre_digit: ", pre_digit)
