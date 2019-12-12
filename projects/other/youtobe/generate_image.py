#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu
import matplotlib.pyplot as plt
import numpy as np
import pandas


def generate_image(countries, gdps):
    """
    输入十组数据，生成柱状图
    """
    plt.rcdefaults()
    fig, ax = plt.subplots()
    y_pos = np.arange(len(countries))
    ax.barh(y_pos, gdps, align='center')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(countries)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('gdps')
    ax.set_title('gdps for each country')
    plt.show()


def generate_video():
    pass


def main():
    countries = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j")
    gdps = (100, 90, 85, 70, 50, 30, 20, 10, 2, 1)
    generate_image(countries, gdps)


if __name__ == '__main__':
    main()
