#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
pillow库

全局概览：
1.图像存储：用于图像归档和图像批量处理，你可以使用它建立缩略图，转换格
式，打印图片等。
2.图像显示
3.图像处理：基本的图像处理功能，包括点操作，使用内置卷积内核过滤，色彩
空间转换。

Image类
可以通过多种方法创建这个类的实例；你可以从文件加载图像，或者处理其他图
像, 或者从 scratch 创建。
"""


import os  # os库提供了使用各种操作系统功能的接口

from PIL import Image, ImageDraw, ImageFont


def display_demo():
    """
    展示图像示例
    从文件加载图像，加载成功将返回一个Image对象，不需要知道文件格式
    """
    im = Image.open("image_test.jpg")  # 从文件中加载图像
    print(im.format, im.size, im.mode)  # 查看文件的内容,格式，尺寸，模式
    im.show()


def save_demo():
    """
    使用save()方法保存文件，保存文件的时候文件名变得重要了。除非你指定格式，
    否则这个库将会以文件名的扩展名作为格式保存。
    """
    # 将文件转换为.png格式
    im = Image.open("./image_test.jpg")
    if not os.path.exists("./image_test.png"):
        im.save("image_test.png")


def create_demo():
    """创建一张图片"""
    if not os.path.exists("./create_demo.jpg"):
        im = Image.new("RGB", (200, 200), "white")  # 指定模式，大小和颜色
        im.save("create_demo.jpg")


def font_demo():
    """使用特定字体"""
    im = Image.open("./create_demo.jpg")
    font = ImageFont.truetype("./SimHei.ttf", size=20)  # 加载指定字体
    draw = ImageDraw.Draw(im)  # 将图片转换为可编辑
    draw.text((50, 30), "Test Text", font=font, fill="red")  # 输入文字
    im.save("./font_demo.jpg")
    im.show()


if __name__ == "__main__":
    # display_demo()
    # save_demo()
    # create_demo()
    font_demo()
