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

        # 眉毛加粗
        d.polygon(face_landmarks["left_eyebrow"], fill=(68, 54, 39, 128))
        d.polygon(face_landmarks["right_eyebrow"], fill=(68, 54, 39, 128))
        d.line(face_landmarks["left_eyebrow"], fill=(68, 54, 39, 150), width=5)
        d.line(face_landmarks["right_eyebrow"], fill=(68, 54, 39, 150), width=5)

        # 嘴唇
        d.polygon(face_landmarks["top_lip"], fill=(150, 0, 0, 128))
        d.polygon(face_landmarks["bottom_lip"], fill=(150, 0, 0, 128))
        d.line(face_landmarks["top_lip"], fill=(150, 0, 0, 64), width=8)
        d.line(face_landmarks["bottom_lip"], fill=(150, 0, 0, 64), width=8)

        # 眼睛
        d.polygon(face_landmarks["left_eye"], fill=(255, 255, 255, 30))
        d.polygon(face_landmarks["right_eye"], fill=(255, 255, 255, 30))

        # 眼线
        # d.line(face_landmarks["left_eye"] + [face_landmarks["left_eye"][0]], fill=(0, 0, 0, 110), width=6)
        # d.line(face_landmarks["right_eye"] + [face_landmarks["left_eye"][0]], fill=(0, 0, 0, 110), width=6)

        pil_image.show()


def recognize_face(known_image_path, unknown_image_path):
    """3.识别图片中的人是谁"""
    known_image = face_r.load_image_file(known_image_path)
    unknown_image = face_r.load_image_file(unknown_image_path)

    tongliya_encoding = face_r.face_encodings(known_image)[0]
    unknown_encoding = face_r.face_encodings(unknown_image)[0]

    ret = face_r.compare_faces([tongliya_encoding], unknown_encoding)
    return ret


# make_up()

ret = recognize_face("./known_images/tongliya.jpeg", "./unknown_images/tong1.jpeg")
print("[INFO]Recognize image tong1.jpeg, is tongliya, result: {}".format(ret))
