#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
使用摄像头拍摄一段视频
"""

import cv2
import time

# 构建一个VideoCapture对象
cap = cv2.VideoCapture(0)

while True:
    # 判断摄像头是否打开，未打开使用cap.open()来打开摄像头
    # if cap.isOpened():
    #     print("is opened")

    # 一帧一帧的捕获图像
    ret, frame = cap.read()

    print(frame)
    print(ret, type(ret))

    # 将捕获的图像转换为灰度图
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 展示灰度图
    cv2.imshow("frame", gray)
    # waitKey(1) 中的数字代表等待按键输入之前的无效时间，单位为毫秒，在这个时间段内按键 ‘q’ 不会被记录，在这之后按键才会被记录
    # 与操作是因为cv2.waitKey(1) 的返回值不止8位，但是只有后8位实际有效，为避免产干扰，通过 ‘与’ 操作将其余位置0
    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

    time.sleep(0.05)

# 展示获取的图像的宽度和高度
print("width: {}\nheight: {}".format(cap.get(3), cap.get(4)))

# 重新设置图像的宽高
# cap.set(3, 320)
# cap.set(4, 240)


# 当退出循环之后，释放对象，关闭所有窗口
cap.release()
cv2.destroyAllWindows()
