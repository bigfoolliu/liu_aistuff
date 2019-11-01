"""
pillow库

全局概览：
1.图像存储：用于图像归档和图像批量处理，你可以使用它建立缩略图，转换格
式，打印图片等。
2.图像显示
3.图像处理：基本的图像处理功能，包括点操作，使用内置卷积内核过滤，色彩
空间转换。

"""
from __future__ import print_function
import os  # os库提供了使用各种操作系统功能的接口

from PIL import Image  # 从库中导入该类
import sys  # sys库提供了许多函数和变量来处理 Python 运行时环境的不同部分。

from matplotlib import pyplot

import csv  # csv模块可以加载.csv文件

import numpy

# Image类
# 可以通过多种方法创建这个类的实例；你可以从文件加载图像，或者处理其他图
# 像, 或者从 scratch 创建。


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

# 将文件转换为.png格式
im.save('../res/image_test.png')


"""
本段代码不懂:http://pillow-cn.readthedocs.io/zh_CN/latest/handbook/tutorial.html
"""

# 创建.jpeg缩略图
size = (128, 128)

for infile in sys.argv[1:]:
    outfile = os.path.splitext(infile)[0] + '.thumbnail'
    if infile != outfile:
        try:
            im = Image.open(infile)
            im.thumbnail(size)
            im.save(outfile, 'JPEG')
        except IOError:
            print('cannot create thumbnail for', infile)

im.save('C:/Users/tonyl/Documents/GitHub/ModuleLearning/image_test.thumbnail')


"""
没反应！
从图像中获取一个矩形选区
4元元组分别代表左，上，右，下的坐标，以左上角为坐标原点，单位为px
"""
box = (100, 100, 200, 200)  # 因此为100x100 pixels的矩形选区
region = im.crop(box)

region = region.transpose(Image.ROTATE_180)
im.paste(region, box)


"""
matplotlib

通过matplotlib库中的方法来绘制图像
"""
pyplot.figure('YellowMan')  # 图像的标题

pyplot.subplot(2, 3, 1)  # 选中1x2的图中的子图1
pyplot.title('origin')  # 该子图的标题为origin
pyplot.imshow(im)

gray = im.convert('1')
pyplot.subplot(2, 3, 2)
pyplot.title('1-bit pixel')
pyplot.imshow(gray)

gray1 = im.convert('F')
pyplot.subplot(2, 3, 3)
pyplot.title('32-bit floating \npoint pixels')
pyplot.imshow(gray1)

gray2 = im.convert('P')
pyplot.subplot(2, 3, 4)
pyplot.title('8-bit pixels')
pyplot.imshow(gray2)

gray3 = im.convert('CMYK')
pyplot.subplot(2, 3, 5)
pyplot.title('4x8-bit pixels\ncolour separation')
pyplot.imshow(gray3)

pyplot.show()
