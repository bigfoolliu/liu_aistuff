#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
决策树

分类：
1. 分类树，输出是样本的类标
2. 回归树，输出是一个实数

优点：
1. 计算复杂度不高，输出结果易于理解
2. 对中间值缺失不敏感，可以处理不相关的特征数据
3. 使用数值型和标称型数据类型

缺点：
1. 可能会产生过度匹配

决策树的一般流程：
1. 收集数据
2. 准备数据，只适用标称数据，因此要将数值离散化处理
3. 分析数据，构造数完成之后，检查图形是否符合预期
4. 训练算法，即构造数的数据结构
5. 测试算法，使用经验数计算错误率
6. 使用算法
"""
from math import log


def cal_shannon_ent(data_set):
    """
    计算香农熵
    H = -sum(p(Xi)log(p(Xi)))
    """
    data_set_size = len(data_set)
    label_conunts = {}
    for feat_vec in data_set:
        current_label = feat_vec[-1]  # 数据字典，其键值为最后一列数值
        if current_label not in label_conunts.keys():
            label_conunts[current_label] = 0
            label_conunts[current_label] += 1
    shannon_ent = 0.0
    for key in label_conunts:
        prob = float(label_conunts[key]) / data_set_size
        shannon_ent -= prob * log(prob, 2)
    return shannon_ent


def main():
    data_set = [[0], [2], [3]]
    ret = cal_shannon_ent(data_set)
    print(ret)


if __name__ == '__main__':
    main()
    