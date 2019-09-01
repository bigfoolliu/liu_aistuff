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
# size = (128, 128)
#
# for infile in sys.argv[1:]:
#     outfile = os.path.splitext(infile)[0] + '.thumbnail'
#     if infile != outfile:
#         try:
#             im = Image.open(infile)
#             im.thumbnail(size)
#             im.save(outfile, 'JPEG')
#         except IOError:
#             print('cannot create thumbnail for', infile)
#
# im.save('C:/Users/tonyl/Documents/GitHub/ModuleLearning/image_test.thumbnail')


"""
没反应！
从图像中获取一个矩形选区
4元元组分别代表左，上，右，下的坐标，以左上角为坐标原点，单位为px
"""
# box = (100, 100, 200, 200)  # 因此为100x100 pixels的矩形选区
# region = im.crop(box)
#
# region = region.transpose(Image.ROTATE_180)
# im.paste(region, box)


"""
matplotlib

通过matplotlib库中的方法来绘制图像
"""
# pyplot.figure('YellowMan')  # 图像的标题
#
# pyplot.subplot(2, 3, 1)  # 选中1x2的图中的子图1
# pyplot.title('origin')  # 该子图的标题为origin
# pyplot.imshow(im)
#
# gray = im.convert('1')
# pyplot.subplot(2, 3, 2)
# pyplot.title('1-bit pixel')
# pyplot.imshow(gray)
#
# gray1 = im.convert('F')
# pyplot.subplot(2, 3, 3)
# pyplot.title('32-bit floating \npoint pixels')
# pyplot.imshow(gray1)
#
# gray2 = im.convert('P')
# pyplot.subplot(2, 3, 4)
# pyplot.title('8-bit pixels')
# pyplot.imshow(gray2)
#
# gray3 = im.convert('CMYK')
# pyplot.subplot(2, 3, 5)
# pyplot.title('4x8-bit pixels\ncolour separation')
# pyplot.imshow(gray3)
#
# pyplot.show()


"""
图例，标题和标签
"""
# pyplot.figure('Line')
#
# x1 = [1, 2, 3]
# y1 = [4, 5, 6]
#
# x2 = [3, 6, 9]
# y2 = [12, 3, 5]
#
# pyplot.plot(x1, y1, label='line 1')
# pyplot.plot(x2, y2, label='line 2')
#
# pyplot.xlabel('plot number')  # 生成X轴标签
# pyplot.ylabel('Important var')  # 生成Y轴标签
#
# pyplot.title('Plot Graph')
# pyplot.legend()  # 生成图例
# pyplot.show()


"""
条形图和直方图
"""
# pyplot.figure('Bar And Hist')
#
# pyplot.subplot(1, 2, 1)
#
# x1 = ([1, 3, 5, 7, 9], [2, 3, 5, 6, 7])
# x2 = ([2, 4, 6, 8, 10], [8, 6, 3, 6, 4])
#
# pyplot.bar(x1[0], x1[1], label='bar 1', color='g')  # 创建直方图，同样需要两组数据，颜色为g(reen)
# pyplot.bar(x2[0], x2[1], label='bar 2', color='r')
#
# pyplot.xlabel('bar number')
# pyplot.ylabel('bar height')
#
# pyplot.title('Bar Graph')
# pyplot.legend()
#
# pyplot.subplot(1, 2, 2)
#
# population_ages = [23, 35, 45, 56, 65, 78, 85]
# bins = [0, 10, 20, 30, 40, 50, 60]
#
# pyplot.hist(population_ages, bins, histtype='bar', rwidth=0.8)
#
# pyplot.xlabel('population_ages')
# pyplot.ylabel('bins')
# pyplot.title('Hist Graph')
# # pyplot.legend()
#
# pyplot.show()


"""
散点图
"""
# pyplot.figure('Scatter')
#
# x = [1, 2, 3, 4, 5, 6]
# y = [2, 3, 6, 2, 7, 9]
# z = [3, 4, 8, 3, 5, 1]
#
# pyplot.subplot(1, 2, 1)
#
# pyplot.scatter(x, y)
#
# pyplot.xlabel('x')
# pyplot.ylabel('y')
# pyplot.title('2-D')
# # pyplot.legend()
#
# pyplot.subplot(1, 2, 2)
#
# pyplot.scatter(x, y, z)
#
# pyplot.xlabel('x')
# pyplot.ylabel('y')
# # pyplot.zlabel('z')，本行错误，三维散点图不能表示
# pyplot.title('3-D')
# # pyplot.legend()
#
# pyplot.show()


"""
堆叠图
"""
# pyplot.figure('Stackplot Graph')
#
# days = [1, 2, 3, 4, 5]
#
# sleeping = [7, 8, 9, 6, 10]
# eating = [1, 3, 2, 4, 2]
# working = [8, 7, 9, 8, 10]
# playing = [5, 8, 7, 10, 12]


"""
以下的代码段是为了给数据添加标签
在任何不止是线条，带有像这样的填充或堆叠图的地方，我们不能以固有方式标记出特定的部分。
均可使用下面的方式
"""
# pyplot.plot([], [], color='m', label='sleeping', linewidth=5)
# pyplot.plot([], [], color='c', label='eating', linewidth=5)
# pyplot.plot([], [], color='k', label='working', linewidth=5)
# pyplot.plot([], [], color='r', label='playing', linewidth=5)
#
# pyplot.stackplot(days, sleeping, eating, working, playing, colors=['m', 'k', 'c', 'r'])
#
# pyplot.xlabel('x')
# pyplot.ylabel('y')
# pyplot.title('Time Spending')
# pyplot.legend()  # 此行不出现将没有图例
#
# pyplot.show()
#
# # 饼图
# pyplot.figure('Pie Graph')
#
# slices = [7, 1, 3, 10]
# activities = ['sleeping', 'eating', 'working', 'playing']
# cols = ['k', 'b', 'm', 'r']
#
# pyplot.pie(slices,
# 		   labels=activities,
# 		   colors=cols,
# 		   startangle=90,
# 		   shadow=True,
# 		   explode=(0, 0.1, 0, 0),
# 		   autopct='%1.1f%%')
#
# pyplot.title('Time Spending Proportion')
# pyplot.show()


"""
从文件加载数据
使用内置csv模块加载csv文件
"""
# pyplot.figure('Load-File Graph')
#
# pyplot.subplot(1, 2, 1)
#
# x = []
# y = []
#
# with open('csv_test.txt', 'r') as csvfile:
# 	plots = csv.reader(csvfile, delimiter=',')  # 读取点集，delimiter表示分隔符，为,(逗号)
# 	for row in plots:
# 		x.append(int(row[0]))  # 将索引为0的元素整数化存储到x列表
# 		y.append(int(row[1]))  # 将索引为1的元素整数化存储到y列表
#
# pyplot.plot(x, y, label='Loaded from csv_test')
# pyplot.xlabel('x')
# pyplot.ylabel('y')
# pyplot.title('csv plot')
# pyplot.legend()
#
# # 使用numpy模块加载文件和数据
# pyplot.subplot(1, 2, 2)
#
# x, y = numpy.loadtxt('numpy_test.txt', delimiter=',', unpack=True)
# pyplot.plot(x, y, label='Loaded from numpy_test', color='r')
#
# pyplot.xlabel('x')
# pyplot.ylabel('y')
# pyplot.title('numpy plot')
# pyplot.legend()
#
# pyplot.show()


"""
有问题！
从网络加载数据
通过简单的拆分来分离数据
"""
# import urllib  # 该库提供一系列用于操作url的功能
#
# from matplotlib import dates  # dates对于将日期戳转换为 matplotlib 可以理解的日期很有用
#
#
# # 定义
# def bytespdata2num(fmt, encoding='utf-8'):
# 	strconverter = dates.strpdate2num(fmt)
#
# 	def bytesconverter(b):
# 		s = b.decode(encoding)
# 		return strconverter(s)
#
# 	return bytesconverter
#
#
# def graph_data(stock):
# 	stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/' + stock + '/chartdata;type=quote;range=10y/csv'
# 	source_code = urllib.request.urlopen(stock_price_url).read().decode()
# 	stock_data = []
# 	split_source = source_code.split('\n')
#
# 	for line in split_source:
# 		split_line = line.split(',')
# 		if len(split_line) == 6:
# 			if 'values' not in line and 'labels' not in line:
# 				stock_data.append(line)
#
# 	date, closep, highp, lowp, openp, volume = numpy.loadtxt(stock_data,
# 															 delimiter=',',
# 															 unpack='True',
# 															 # %Y = full year. 2015
# 															 # %y = partial year 15
# 															 # %m = number month
# 															 # %d = number day
# 															 # %H = hours
# 															 # %M = minutes
# 															 # %S = seconds
# 															 # 12-06-2014
# 															 # %m-%d-%Y
# 															 converters={0: bytespdata2num('%Y%m%d')})
#
# 	pyplot.plot_date(date, closep, '-', label='Price')
#
# 	pyplot.xlabel('Date')
# 	pyplot.ylabel('Prices')
# 	pyplot.title('Stock Price')
# 	pyplot.legend()
# 	pyplot.show()
#
#
# graph_data('TSLA')


"""
matplot，3D绘图
axes3d，不需要不同种类的轴域，便于绘制
"""
from mpl_toolkits.mplot3d import axes3d
from matplotlib import style

style.use('fivethirtyeight')

fig = pyplot.figure('3D Scatter Plots')
ax1 = fig.add_subplot(1, 2, 1, projection='3d')

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [5, 6, 7, 8, 2, 5, 6, 3, 7, 2]
z = [1, 2, 6, 3, 2, 7, 3, 3, 7, 2]

ax1.scatter(x, y, z)  # 绘制散点图

ax1.set_xlabel('x axis')
ax1.set_ylabel('y axis')
ax1.set_zlabel('z axis')


"""
绘制空间曲面

z = x ^ 2 + y ^ 2 
"""
import numpy

ax2 = fig.add_subplot(1, 2, 2, projection='3d')

x = numpy.linspace(-10, 10, 50)
y = x
x, y = numpy.meshgrid(x, y)

z = x ** 2 + y ** 2

ax2.plot_wireframe(x, y, z)

ax2.set_xlabel('x axis')
ax2.set_ylabel('y axis')
ax2.set_zlabel('z axis')

pyplot.show()
