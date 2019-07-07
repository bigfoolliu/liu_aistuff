#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


"""
轮廓检测基础
"""
import cv2
from matplotlib import pyplot as plt


img = cv2.imread("../images/blue_flower.jpeg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray_img, 127, 255, 0)

# thresh是轮廓源图，cv2.RETR_TREE是轮廓检测模型，cv2.CHAIN_APPROX_SIMPLE是轮廓近似函数
# 输出图像，轮廓和等级
contour_img, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# 轮廓展示效果图
contour_effect_img1 = cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
contour_effect_img2 = cv2.drawContours(img, contours, 3, (0, 255, 0), 3)

images = [img, gray_img, contour_img, contour_effect_img1, contour_effect_img2]
titles = ["original img", "gray img", "contour img", "contour effect img1", "contour effect img2"]

for i in range(len(images)):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])


plt.show()
