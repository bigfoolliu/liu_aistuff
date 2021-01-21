#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
matplotlib模块基本使用
"""


import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
from mpl_toolkits.mplot3d import axes3d


def sin_demo():
    """
    1. 画正弦图像
    """
    # 定义横坐标
    x = np.arange(-np.pi * 2, np.pi * 2, 0.02)
    # 计算得到纵坐标
    y = np.sin(x)
    # 画图
    plt.title('y=sinx')
    plt.plot(x, y)
    # 显示图像
    plt.show()


def axis_demo():
    """
    2. 坐标区间设置
    """
    x = np.arange(-np.pi * 2, np.pi * 2, 0.02)
    y = np.sin(x)

    # 定义坐标轴,横坐标为-10至10, 纵坐标为-2至2
    plt.title('y=sinx, (-10<x<10)')
    plt.axis([-10, 10, -2, 2])
    plt.plot(x, y)
    plt.show()


def grid_demo():
    """
    3. 设置网格
    """
    x = np.arange(-np.pi * 2, np.pi * 2, 0.02)
    y = np.sin(x)

    plt.title('y=sinx, grid')
    plt.axis([-10, 10, -2, 2])
    plt.plot(x, y)
    # 增加网格线
    plt.grid(True)
    plt.show()


def three_dimention_graph():
    """
    matplot，3D绘图
    axes3d，不需要不同种类的轴域，便于绘制
    """
    style.use('fivethirtyeight')
    
    fig = plt.figure('3D Scatter Plots')
    ax1 = fig.add_subplot(1, 2, 1, projection='3d')
    
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [5, 6, 7, 8, 2, 5, 6, 3, 7, 2]
    z = [1, 2, 6, 3, 2, 7, 3, 3, 7, 2]
    
    ax1.scatter(x, y, z)  # 绘制散点图
    
    ax1.set_xlabel('x axis')
    ax1.set_ylabel('y axis')
    ax1.set_zlabel('z axis')

    # 绘制空间曲面: z = x ^ 2 + y ^ 2 
    ax2 = fig.add_subplot(1, 2, 2, projection='3d')
    
    x = np.linspace(-10, 10, 50)
    y = x
    x, y = np.meshgrid(x, y)
    
    z = x ** 2 + y ** 2
    
    ax2.plot_wireframe(x, y, z)
    
    ax2.set_xlabel('x axis')
    ax2.set_ylabel('y axis')
    ax2.set_zlabel('z axis')
    
    plt.show()


def hist_demo():
    """条形图和直方图"""
    plt.figure('Bar And Hist')

    plt.subplot(1, 2, 1)

    x1 = ([1, 3, 5, 7, 9], [2, 3, 5, 6, 7])
    x2 = ([2, 4, 6, 8, 10], [8, 6, 3, 6, 4])

    plt.bar(x1[0], x1[1], label='bar 1', color='g')  # 创建直方图，同样需要两组数据，颜色为g(reen)
    plt.bar(x2[0], x2[1], label='bar 2', color='r')

    plt.xlabel('bar number')
    plt.ylabel('bar height')

    plt.title('Bar Graph')
    plt.legend()

    plt.subplot(1, 2, 2)

    population_ages = [23, 35, 45, 56, 65, 78, 85]
    bins = [0, 10, 20, 30, 40, 50, 60]

    plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

    plt.xlabel('population_ages')
    plt.ylabel('bins')
    plt.title('Hist Graph')
    # pyplot.legend()

    plt.show()


def scatter_demo():
    """
    散点图
    """
    plt.figure('Scatter')

    x = [1, 2, 3, 4, 5, 6]
    y = [2, 3, 6, 2, 7, 9]
    z = [3, 4, 8, 3, 5, 1]

    plt.subplot(1, 2, 1)

    plt.scatter(x, y)

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('2-D')
    # plt.legend()

    plt.subplot(1, 2, 2)

    plt.scatter(x, y, z)

    plt.xlabel('x')
    plt.ylabel('y')
    # plt.zlabel('z')，本行错误，三维散点图不能表示
    plt.title('3-D')
    # plt.legend()

    plt.show()


def pie_demo():
    """
    堆叠图
    """
    plt.figure('Stackplot Graph')

    days = [1, 2, 3, 4, 5]

    sleeping = [7, 8, 9, 6, 10]
    eating = [1, 3, 2, 4, 2]
    working = [8, 7, 9, 8, 10]
    playing = [5, 8, 7, 10, 12]

    # 给数据添加标签, 任何带有像这样的填充或堆叠图的地方,不能以固有方式标记出特定的部分,均可使用下面的方式
    plt.plot([], [], color='m', label='sleeping', linewidth=5)
    plt.plot([], [], color='c', label='eating', linewidth=5)
    plt.plot([], [], color='k', label='working', linewidth=5)
    plt.plot([], [], color='r', label='playing', linewidth=5)

    plt.stackplot(days, sleeping, eating, working, playing, colors=['m', 'k', 'c', 'r'])

    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Time Spending')
    plt.legend()  # 此行不出现将没有图例

    plt.show()

    # 饼图
    plt.figure('Pie Graph')

    slices = [7, 1, 3, 10]
    activities = ['sleeping', 'eating', 'working', 'playing']
    cols = ['k', 'b', 'm', 'r']

    plt.pie(slices,
            labels=activities,
            colors=cols,
            startangle=90,
            shadow=True,
            explode=(0, 0.1, 0, 0),
            autopct='%1.1f%%')

    plt.title('Time Spending Proportion')
    plt.show()


def legend_demo():
    """
    图例，标题和标签
    """
    plt.figure('Line')

    x1 = [1, 2, 3]
    y1 = [4, 5, 6]

    x2 = [3, 6, 9]
    y2 = [12, 3, 5]

    plt.plot(x1, y1, label='line 1')
    plt.plot(x2, y2, label='line 2')

    plt.xlabel('plot number')  # 生成X轴标签
    plt.ylabel('Important var')  # 生成Y轴标签

    plt.title('Plot Graph')
    plt.legend()  # 生成图例
    plt.show()


if __name__ == "__main__":
    sin_demo()
    axis_demo()
    grid_demo()
    hist_demo()
    scatter_demo()
    pie_demo()
    legend_demo()
    three_dimention_graph()
