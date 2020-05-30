#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
图像梯度
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("../images/chess.jpg", 0)

# 拉普拉斯衍生
laplacian_img = cv2.Laplacian(img, cv2.CV_64F)

sobelx_img = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobely_img = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

images = [img, laplacian_img, sobelx_img, sobely_img]

for i in range(len(images)):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], "gray")


plt.show()
