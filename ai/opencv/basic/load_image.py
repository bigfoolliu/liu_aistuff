#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


import numpy as np
import cv2


"""
加载图片

cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

使用 -1, 0, 1来代替
"""


# 使用灰度图的方式加载图片
img = cv2.imread("../images/person.jpeg", 0)
print("img: {}\ntype: {}".format(img, type(img)))
