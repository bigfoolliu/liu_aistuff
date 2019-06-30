#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


import numpy as np
import cv2


img = cv2.imread("../images/person.jpeg", 1)

cv2.imshow("window-name", img)  # 前面是窗口的名字


# 1.基础使用方法
# cv2.waitKey(0)  # 0的时候等待按键停止，其他的数字表示为毫秒数
# cv2.waitKey(2000)
# cv2.destroyWinsows()


# 2.等待用户触发事件，等待时间为1000ms，
# 如果在这个时间段内, 用户按下ESC(ASCII码为27),
# 则跳出循环,否则,则跳出循环
while True:
    if cv2.waitKey(1000) == 27:
        break
