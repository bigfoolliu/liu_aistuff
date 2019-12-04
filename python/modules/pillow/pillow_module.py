"""
pillow库

全局概览：
1.图像存储：用于图像归档和图像批量处理，你可以使用它建立缩略图，转换格
式，打印图片等。
2.图像显示
3.图像处理：基本的图像处理功能，包括点操作，使用内置卷积内核过滤，色彩
空间转换。

"""
import csv  # csv模块可以加载.csv文件
import os  # os库提供了使用各种操作系统功能的接口
import sys  # sys库提供了许多函数和变量来处理 Python 运行时环境的不同部分。

import numpy
from matplotlib import pyplot
from PIL import Image  # 从库中导入该类


"""
Image类
可以通过多种方法创建这个类的实例；你可以从文件加载图像，或者处理其他图
像, 或者从 scratch 创建。
"""


def display_demo():
    """展示图像示例"""
    # 从文件加载图像，加载成功将返回一个Image对象，不需要知道文件格式
    im = Image.open('../res/image_test.jpg')  # 从文件中加载图像

    # 通过示例属性查看文件的内容
    print(im.format, im.size, im.mode)

    # 通过show()函数就可以显示图像，但效率不高
    im.show()


"""
读写图像
使用save()方法保存文件，保存文件的时候文件名变得重要了。除非你指定格式，
否则这个库将会以文件名的扩展名作为格式保存。
"""


def save_demo():
    """保存图像示例"""
    # 将文件转换为.png格式
    im.save('../res/image_test.png')


if __name__ == "__main__":
    display_demo()
