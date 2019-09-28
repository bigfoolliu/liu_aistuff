#!/usr/bin/env python3
#!coding:utf-8


"""
knn算法(k近邻算法):
- 如果一个待分类样本在特征空间中的k个最相似，则该样本也属于这个类别

使用:
import knn
knn.classify(xxx)

要素:
- 数据集
- 样本的向量表示
- 样本间距离的计算方法
- K值的选取

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

k近邻算法的一般流程：

1.收集数据
2.准备数据：计算需要的数据，最好是结构化的数据格式
3.分析数据
4.训练算法：不适用于k-近邻算法
5.测试算法：计算错误率
6.使用算法：输入样本数据和结构化的输出结果，然后用K-近邻判定输入数据分别属于哪个分类，最后应用对计算出的分类执行后续处理

对未知类别属性的数据集中的每个点依次执行以下操作：
1.计算已知类别数据集中的点与当前点的距离
2.按照距离递增排序
3.选取与当前点距离最小的k个点
4.确定前k个点所在类别出现的频率
5.将k个点中出现频率最高的分类作为当前点的预测分类
"""

import numpy as np
from numpy import tile
import operator


def createDateSet():
    """
    构建最简单的数据集
    """
    group = np.array([[1, 1.1], [1, 1], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify(inX, data_set, labels, k):
    """
    构造了一个简单的分类器

    inX: 用于分类的输入向量
    dataSet: 输入的训练样本集
    labels: 标签向量
    k: 用于选择的最近邻居的数目
    eg:
        knn.classify([0, 0], [[0, 1], [1, 1], [1, 2]], ['a', 'a', 'b'], 3)
    """
    data_set_size = data_set.shape[0]  # 获取输入的数据集样本个数

    if k > data_set_size:
        raise Exception("k is supposed to smaller than the dataSet size!")

    diff_mat = tile(inX, (data_set_size, 1)) - data_set  # 计算输入数据与训练数据集每个数据的横纵坐标的差值
    sq_diff_mat = diff_mat ** 2  # 计算每一个差值的算术平方
    sq_distance = sq_diff_mat.sum(axis=1)  # 将各自的横纵坐标的差值的平方相加
    distances = sq_distance ** 0.5  # 开根号
    sorted_distance_indicies = distances.argsort()  # 将元素从小到大排列，取得其下标
    class_count = {}

    # 将前k个距离最小的点的标签进行统计
    for i in range(k):
        vote_label = labels[sorted_distance_indicies[i]]
        class_count[vote_label] = class_count.get(vote_label, 0) + 1

    # 将统计好的标签进行倒序排列
    sorted_class_count = sorted(class_count.items(), key=operator.itemgetter(1), reverse=True)

    return sorted_class_count[0][0]
