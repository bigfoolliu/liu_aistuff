#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


FILE_PATH = "./knn_dataset/3-16.csv"


def read_file(file_path):
    """
    读取csv文件
    movie,actions,kisses,type
    :return type: DataFrame
    """
    movie_data = pd.read_csv(file_path)
    return movie_data


def draw_scatter(x, y, color="red"):
    """
    画出散点图
    """
    plt.scatter(x, y, color=color)


movie = read_file(FILE_PATH)
# 以actions的数量作为横坐标，kisses作为纵坐标
fig = plt.figure()
plt.scatter(movie["actions"], movie["kisses"])
plt.xlabel("actions")
plt.ylabel("kisses")
plt.show()
