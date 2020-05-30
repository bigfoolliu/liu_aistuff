#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
basemap库
"""

from matplotlib import pyplot
from mpl_toolkits.basemap import Basemap


def basic_demo():
    # 画出海岸线
    pyplot.figure('Coast Line')

    m = Basemap(projection='mill')  # 以'米勒投影'的方式得到的海岸线
    m.drawcoastlines()  # 画海岸线

    pyplot.show()

    # 放大到特定区域
    pyplot.figure('Zoom Areas')

    m = Basemap(projection='mill',
                llcrnrlat=-40,  # 左下角的纬度，西经和南纬坐标为负值
                llcrnrlon=-40,  # 左下角的经度
                urcrnrlat=60,  # 右下角的纬度，东经和北纬坐标为正值
                urcrnrlon=90)  # 右下角的经度
    m.drawcoastlines()

    pyplot.show()

    # 画出国家，州
    pyplot.figure('World Map')

    pyplot.subplot(3, 2, 1)

    m = Basemap(projection='mill',
                llcrnrlat=-90,  # 左下角的纬度，西经和南纬坐标为负值
                llcrnrlon=-180,  # 左下角的经度
                urcrnrlat=90,  # 右下角的纬度，东经和北纬坐标为正值
                urcrnrlon=180)  # 右下角的经度

    m.drawcoastlines()
    m.drawcountries(linewidth=2)
    m.drawstates(color='b')
    m.drawcounties(color='darkred')
    # m.drawrivers()  # 画出河流

    pyplot.title('Version 1')

    # 调整分辨率resolution
    # c-粗糙，l-低，h-高，f-完整
    pyplot.subplot(3, 2, 2)

    m = Basemap(projection='mill',
                llcrnrlat=-90,  # 左下角的纬度，西经和南纬坐标为负值
                llcrnrlon=-180,  # 左下角的经度
                urcrnrlat=90,  # 右下角的纬度，东经和北纬坐标为正值
                resolution='l')  # 右下角的经度

    m.drawcoastlines()
    m.drawcountries(linewidth=1)
    m.drawstates(color='b')
    m.drawcounties(color='g')
    pyplot.title('Version 2')

    # 绘制地形#m.etopo()，蓝色大理石版#m.bluemarble()
    pyplot.subplot(3, 2, 3)

    m.drawcoastlines()
    m.drawcountries(linewidth=2)
    m.drawstates(color='b')
    m.drawcounties(color='g')
    m.fillcontinents()

    pyplot.title('Version 3')

    pyplot.show()


if __name__ == "__main__":
    basic_demo()
