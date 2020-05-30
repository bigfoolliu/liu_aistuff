#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
色域

使用不同的色域可以做物体提取，此处是将蓝色的物体提取出来
获取到的图像中可能会有一些噪点

1. 不同色域之间转换的函数列表
eg: cv2.COLOR_BGR2GRAY, cv2.COLOR_BGR2HSV
flags = [i for i in dir(cv2) if i.startswith("COLOR_")]

2. 找到合适的HSV数值来追踪
green = np.uint8([0, 255, 0])  # 任何想要追踪的颜色
hsv_green = cv2.cvtColor(green, cv2.COLOR_BGR2HSV)
print(hsv_green)  # [[[60 255 255]]]
"""
import cv2
import numpy as np


img = cv2.imread("../images/blue_flower.jpeg")

# 将原始的BGR色域转换为HSV色域
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 定义在HSV色域中的蓝色的区间（也可以转换为其他颜色）
lower_blue = np.array([110, 50, 50])
upper_blue = np.array([130, 255, 255])

# HSV图像获取蓝色的阈值
mask = cv2.inRange(hsv, lower_blue, upper_blue)

# 将原始图像和阈值按位与只获取到蓝色的图
res = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow("img", img)
cv2.imshow("mask", mask)
cv2.imshow("res", res)

while True:
    if cv2.waitKey(1000) == 27:
        break
