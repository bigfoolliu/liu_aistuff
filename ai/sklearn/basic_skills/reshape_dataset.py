#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
sklearn处理二维数组，当不是这种的时候需要reshape
"""


from sklearn import datasets


digits = datasets.load_digits()
# print(digits["images"].shape)  # (1797, 8, 8)


# 显示图像
# plt.imshow(digits["images"][0], cmap=plt.cm.gray_r)  # 显示灰度图
# plt.imshow(digits["images"][0])  # 默认显示彩色图
# plt.show()


# 将8x8的图像转换为长度为64的数组
data = digits["images"].reshape((digits["images"].shape[0], -1))
print("new shape: ", data.shape)
