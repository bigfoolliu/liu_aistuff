#!/usr/bin/env python
#!coding:utf-8


"""
knn算法(k近邻算法):
- 如果一个待分类样本在特征空间中的k个最相似，则该样本也属于这个类别

要素:
- 数据集
- 样本的向量表示
- 样本间距离的计算方法
- K值的选取

基本步骤:
1. 计算待分类点与已知类别点之间的距离
2. 按照距离递增次序排序
3. 选取与待分类点距离最小的K个点
4. 确定前K个点所在类别的出现次数
5. 返回前K个点出现次数最高的类别作为待分类点的预测分类

优点:
- 简单有效
- 重新训练的代价较低
- 计算时间和空间线性相对较小
- 对于类域的交叉或重叠较多的待分样本集较为适合

缺点:
- 属于lazy learning,基本上不学习
- 类别评分不是规格化的
- 输出的解释性不强
- 样本数量不平衡时，也可能导致输入一个新的样本时，该样本的K个邻居中大容量类的样本占多数，导致会靠近大容量样本，那就需要归一化处理
- 计算量较大
"""
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

