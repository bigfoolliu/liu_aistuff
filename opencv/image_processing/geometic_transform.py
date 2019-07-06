#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


"""
图像的几何转换

旋转，镜像，缩放等
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt



img = cv2.imread("../images/person_reformat.png")


# 图片缩小或放大
scaling_img = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)


# 图像翻转
flip_img = cv2.flip(img, 0)  # 0：垂直翻转，1：水平翻转，-1：水平垂直同时翻转


# 图像平移，旋转，仿射
# 平移
rows, cols = img.shape[:2]
M = np.float32([[1, 0, 100], [0, 1, 50]])  # 平移(100, 50)
translation_img = cv2.warpAffine(img, M, (cols, rows), borderValue=(155, 150, 200))
# 旋转
M1 = cv2.getRotationMatrix2D((cols/2, rows/2), 60, 1)
translation_img1 = cv2.warpAffine(img, M1, (cols, rows))

M2 = cv2.getRotationMatrix2D((cols/2, rows/2), 180, 1)
translation_img2 = cv2.warpAffine(img, M2, (cols, rows))



images = [img, scaling_img, flip_img, translation_img, translation_img1, translation_img2]
titles = ["original img", "scaling img(x2)", "flip img",
"translation img", "translation img1(60)", "translation img2(180)"]


for i in range(len(images)):
    plt.subplot(int(len(images)/3) + 1, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])


plt.show()