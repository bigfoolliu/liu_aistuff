#!/usr/bin/env python
#!coding:utf-8


"""
使用face_recognition库定位明星的脸部
"""
import face_recognition as face_r
from PIL import Image


FILE_PATH = "./known_images/tongliya.jpeg"

# 加载图片
image = face_r.load_image_file(FILE_PATH)

# 定位脸部的位置，返回的是一个4维数组，分别表示脸部像素的上，右，下，左的像素点坐标
face_locations = face_r.face_locations(image)

print("[INFO]There are {} face(s) in image {}".format(len(face_locations), FILE_PATH))

for face_location in face_locations:
    top, right, bottom, left = face_location
    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.show()

