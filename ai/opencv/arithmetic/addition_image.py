#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


"""
图像的加法
"""


import cv2
import numpy as np


x = np.uint8([200])
y = np.uint8([200])

c = cv2.add(x, y)
print(c)  # [255]
