#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


"""
边缘检测
"""
import cv2
from matplotlib import pyplot as plt


img = cv2.imread("../images/person.jpeg")

# 检测边缘之后的图像
edge_img = cv2.Canny(img, 100, 200)
edge_img1 = cv2.Canny(img, 100, 100)
edge_img2 = cv2.Canny(img, 200, 200)

images = [img, edge_img, edge_img1, edge_img2]


for i in range(len(images)):
    plt.subplot(2, 2, i+1)
    plt.imshow(images[i])


plt.show()
