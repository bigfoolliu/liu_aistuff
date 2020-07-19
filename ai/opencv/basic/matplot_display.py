#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
使用matplotlib来展示图片
"""

import cv2
import matplotlib.pyplot as plt


img = cv2.imread("../images/person.jpeg", 1)

plt.imshow(img)
# plt.imshow(img, cmap="gray", interpolation="bicubic")

# 隐藏坐标轴
plt.xticks([])
plt.yticks([])

plt.show()
