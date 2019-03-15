#!/usr/bin/env python
#!coding:utf-8


"""
将fer2013数据集中的csv文件还原为图片,格式为jpg

- 每张图片大小为固定的48*48
- 7种表情对应数字0-6(
    0: anger生气，
    1: disgust厌恶
    2: fear恐惧
    3: happy开心
    4: sad伤心
    5: surprised惊讶
    6: normal中性
    )
- 对应格式为:
    emotion, pixels, Usage
    0        ...     Training
"""
import pandas as pd
import numpy as np
import os
import scipy.misc as sm
import datetime


# csv数据集位置
FILE_PATH = "../dataset/fer2013/fer2013.csv"

emotions = {
        "0": "anger",
        "1": "disgust",
        "2": "fear",
        "3": "happy",
        "4": "sad",
        "5": "surprised",
        "6": "normal"
        }


def show_time():
    """显示当前时间"""
    return datetime.datetime.now().isoformat()


def create_folder(dir):
    """创建文件夹"""
    if os.path.exists(dir) is False:
        os.makedirs(dir)


def csv_to_img(file):
    """将fer2013的csv文件转换为图片"""
    # 读取文件
    face_data = pd.read_csv(file)

    # 遍历csv文件内容并将图片数据分类保存
    for index in range(len(face_data)):
        print("[INFO]{}:Begin to save data {}".format(show_time(), index))

        # 将csv数据列分类
        emotion_data = face_data.loc[index][0]
        img_data = face_data.loc[index][1]
        usage_data = face_data.loc[index][2]

        # 将图片转换为48*48格式
        data_array = list(map(float, img_data.split()))  # 将数据转换为float然后转换为list
        data_array = np.array(data_array)
        img = data_array.reshape(48, 48)

        # 选择分类并创建文件名
        dir_name = usage_data
        emotion_name = emotions[str(emotion_data)]

        # 图片要保存的文件夹
        img_path = os.path.join(dir_name, emotion_name)

        # 创建"用于文件夹"和"表情文件夹"
        create_folder(dir_name)
        create_folder(img_path)

        # 图片文件名
        img_name = os.path.join(img_path, str(index) + ".jpg")

        # 转换并存储
        sm.toimage(img).save(img_name)  # 将nparray数组转换为图片并保存


csv_to_img(FILE_PATH)

