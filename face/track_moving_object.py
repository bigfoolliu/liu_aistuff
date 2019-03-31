#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
追踪视频或者摄像头中的移动物体
参考: https://blog.csdn.net/weixin_38907560/article/details/82292091
"""
import cv2
import imutils
from imutils.video import VideoStream, FPS
import time
import argparse


# step1:目标是根据输入的参数来指定追踪方式
parser = argparse.ArgumentParser()
parser.add_argument(
    "-v", "--video", type=str, help="path of the video file"
    )  # 视频地址
parser.add_argument(
    "-t", "--tracker", type=str, help="track type the opencv use"
    )  # 追踪方式
args = vars(parser.parse_args())  # 将参数转换为字典格式,object.__dict__


# step2:根据opencv的版本处理追踪器的类别
(major, minor) = cv2.__version__.split(".")[:2]
if int(minor) < 3:  # 低于3.3版本
    tracker = cv2.Tracker_create(args["tracker"].upper())
else:  # 高于3.3版本
    OPENCV_OBJECT_TRACKERS = {
        "csrt": cv2.TrackerCSRT_create,
        "kcf": cv2.TrackerKCF_create,
        "boosting": cv2.TrackerBoosting_create,
        "mil": cv2.TrackerMIL_create,
        "tld": cv2.TrackerTLD_create,
        "medianflow": cv2.TrackerMedianFlow_create,
        "mosses": cv2.TrackerMOSSE_create
    }

tracker = OPENCV_OBJECT_TRACKERS[args["tracker"]]()


# step3:初始化边界
init_bounding_box = None
# 如果没有指定视频则启用摄像头录制视频
if not args.get("video", False):
    print("[INFO]starting video stream...")
    video_stream = VideoStram(src=0).start()
    time.sleep(1.0)
else:
    # 指定了视频流则从视频文件对视频流初始化
    video_stream = cv2.VideoCapture(args["video"])

fps = None


# step4:迭代视频流中的视频帧
while True:
    # 根据是视频还是摄像头来处理帧
    frame = video_stream.read()
    frame = frame[1] if args.get("video", False) else frame

    if frame is None:
        break
    # 调整帧的大小以便处理的更快，并获取帧的维度
    frame = imutils.resize(frame, width=500)
    (H, W) = frame.shape[:2]

    if init_bounding_box is not None:
        (success, box) = tracker.update(frame)
        if success:
            (x, y, w, h) = [int(v) for v in box]
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        fps.update()
        fps.stop()

        # 需要输出的信息
        info = [
            ("Tracker", args["tracker"]),
            ("Success", "Yes" if success else "No"),
            ("FPS", "{:.2f}".format(fps.fps())),
        ]

        for (i, (k, v)) in enumerate(info):
            text = "{}: {}".format(k, v)
            cv2.putText(
                frame, text, (10, H-((i*20)+20)),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2
                )

    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF

    if key == ord("s"):
        init_bounding_box = cv2.selectROI(
            "Frame", frame, fromCenter=False, showCrosshair=True
            )
        tracker.init(frame, init_bounding_box)
        fps = FPS().start()

    elif key == ord("q"):
        break


if not args.get("video", False):
    video_stream.stop()
else:
    video_stream.release()

cv2.destroyAllWindows()
