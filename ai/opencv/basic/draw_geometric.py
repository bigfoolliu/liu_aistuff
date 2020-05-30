#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
画几何图形
"""


import cv2
import numpy as np


img = np.zeros((512, 512, 3), np.uint8)

# 画直线
img = cv2.line(img, (0, 0), (500, 500), (255, 0, 0), 5)

# 画矩形
img = cv2.rectangle(img, (0, 0), (200, 100), (0, 255, 0), 3)

# 画圆
img = cv2.circle(img, (100, 100), 50, (0, 0, 255), -1)

# 画椭圆
# img = cv2.ellipse(img, (200, 200), (100, 50), 0, 0, 180, 255, -1)  # 半个椭圆
img = cv2.ellipse(img, (200, 200), (100, 50), 0, 0, 360, 255, -1)

# 添加文字
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, "open cv ", (10, 300), font, 4, (255, 255, 255), 2, cv2.LINE_AA)

cv2.imshow("geometric", img)

while True:
    if cv2.waitKey(1000) == 27:
        break
