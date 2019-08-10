#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


"""
保存一段视频
"""


import cv2


cap = cv2.VideoCapture(0)

# 指定编码格式
# In Fedora: DIVX, XVID, MJPG, X264, WMV1, WMV2. (XVID is more preferable. MJPG results in high size video. X264 gives very small size video)
# In Windows: DIVX (More to be tested and added)
# In OSX : (I don’t have access to OSX. Can some one fill this?)
fourcc = cv2.VideoWriter_fourcc(*"DIVX")

out = cv2.VideoWriter("../videos/output1.avi", fourcc, 20.0, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()

    # 如果摄像头捕获到了才处理
    if ret == True:
        # 翻转每一帧
        # frame = cv2.flip(frame, 0)

        # 将帧写入到输出文件
        out.write(frame)

        # 展示
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break


cap.release()
out.release()
cv2.destroyAllWindows()
