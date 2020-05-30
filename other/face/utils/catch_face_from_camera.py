#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
实时从摄像头中捕捉人脸
"""
import face_recognition as face_r
import cv2
from PIL import Image, ImageFont, ImageDraw
import numpy as np
import time
import os

FILE_PATH = "./known_images"
name_list = []
face_encoding_list = []
face_locations = []
process_this_frame = True


def get_known_images(file_path):
    """返回文件夹中的所有图片的名称列表"""
    global name_list, face_encoding_list
    if file_path:
        for image_name in os.listdir(file_path):
            # 将图片的名称和后缀分开
            name, extension = os.path.splitext(image_name)
            # 加载图片以及将面部编码
            image = face_r.load_image_file(os.path.join(file_path, image_name))
            face_encoding = face_r.face_encodings(image)[0]
            # 将所有图片信息添加进列表
            name_list.append(name)
            face_encoding_list.append(face_encoding)

    print("name_list:", name_list)
    print("face_encoding_list:", face_encoding_list)
    return


def run():
    global face_locations, process_this_frame
    print("[INFO]Begin to capture video")
    # 使用摄像头(注意虚拟机的话需要打开摄像头设备)
    video_capture = cv2.VideoCapture(0)
    print("[INFO]video_capture: {}".format(video_capture))
    while True:
        # 从摄像头抓取单帧并处理
        ret, frame = video_capture.read()
        print("[INFO]ret: {}, frame: {}".format(ret, frame))
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)  # 图片缩小
        rgb_small_frame = small_frame[:, :, ::-1]  # 将图片从BGR颜色(opencv使用)转换为rgb颜色(face_recognition使用)
        # 处理部分帧以节约时间
        if process_this_frame:
            face_locations = face_r.face_locations(rgb_small_frame)
            face_encodings = face_r.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # 判断是否匹配已知的面部
                matches = face_r.compare_faces(face_encoding_list, face_encoding)
                name = "Unknown"

                # 如果有一个匹配,则使用第一个匹配的
                if True in matches:
                    first_match_index = matches.index(True)
                    name = name_list[first_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # 展示结果
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # 在发现的面部画个方框
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # 放置一个面部的名字
            # cv2.rectangle(frame, (left, bottom-100), (right, bottom), (0, 0, 255), 2)
            # 为了显示cv2能显示中文，将frame(cv2的编码格式)转换为pillow格式，加上汉字，再转换为cv2格式
            font = ImageFont.truetype("./fonts/SimHei.ttf", 20, encoding="utf-8")
            pil_img = Image.fromarray(frame)
            draw = ImageDraw.Draw(pil_img)
            draw.text((left + 6, bottom - 25), name, font=font, fill=(0, 255, 0, 0))
            frame = np.array(pil_img)
            cv2.putText(frame, "", (left + 6, bottom - 25), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 1)
        # 展示图片结果
        cv2.imshow("Video", frame)

        # 按q键来退出
        if cv2.waitKey(1) & 0xff == ord("q"):
            break

        time.sleep(0.1)

    # 释放摄像头
    video_capture.release()
    cv2.destroyAllWindows()


get_known_images(FILE_PATH)
run()
