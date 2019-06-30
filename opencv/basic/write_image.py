#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


import cv2


img = cv2.imread("../images/person.jpeg", 0)

# 写入图像，将图像改变格式为png
cv2.imwrite("../images/person_reformat.png", img)
