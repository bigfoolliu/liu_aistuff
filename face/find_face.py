#!/usr/bin/env python
#!coding:utf-8


"""
使用face_recognition库定位明星的脸部
"""
import face_recognition as face_r
from PIL import Image, ImageDraw


FILE_PATH = "./known_images/tongliya.jpeg"

# 加载图片
IMAGE_TONG = face_r.load_image_file(FILE_PATH)


def cut_face():
    """1.定位面部并将其切割出来显示"""
    # 定位脸部的位置，返回的是一个4维数组，分别表示脸部像素的上，右，下，左的像素点标
    face_locations = face_r.face_locations(IMAGE_TONG)
    print("[INFO]There are {} face(s) in image {}".format(len(face_locations), FILE_PATH))
    for face_location in face_locations:
        top, right, bottom, left = face_location
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show()


def make_up():
    """2.识别人脸关键点,对人脸进行化妆"""
    face_landmarks_list = face_r.face_landmarks(IMAGE_TONG)
    for face_landmarks in face_landmarks_list:
        pil_image = Image.fromarray(IMAGE_TONG)
        d = ImageDraw.Draw(pil_image, "RGBA")

        # 眉毛
        d.polygon(face_landmarks["left_eyebrow"], fill=(68, 54, 39, 128))
        d.polygon(face_landmarks["right_eyebrow"], fill=(68, 54, 39, 128))
        d.line(face_landmarks["left_eyebrow"], fill=(68, 54, 39, 150), width=5)
        d.line(face_landmarks["right_eyebrow"], fill=(68, 54, 39, 150), width=5)

        pil_image.show()


make_up()

