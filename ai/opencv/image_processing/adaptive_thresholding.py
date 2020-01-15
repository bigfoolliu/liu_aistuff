#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


"""
图片的自适应阈值

计算图像的小区域额阈值，为同一图像的不同区域计算不同的阈值
可以得到不同明亮度的图像提供更好的结果

cv2.ADAPTIVE_THRESH_MEAN_C：阈值是邻域的平均值。 
cv2.ADAPTIVE_THRESH_GAUSSIAN_C：阈值是邻域值的加权和，其中权重是高斯窗口。
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread("../images/chess.jpg", 0)
img = cv2.medianBlur(img, 5)

ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

titles = ["original image", "global thresholding(v=127)", "adaptive mean thresholding", "adaptive gaussian thresholding"]
images = [img, th1, th2, th3]


for i in range(4):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i], "gray")
    plt.title(titles[i])
    plt.xticks([])
    plt.yticks([])


plt.show()
