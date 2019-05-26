#!/usr/bin/env python3
#!coding:utf-8


'''
sklearn标准化API：sklearn.preprocessing.StandardScaler
    StandardScaler.fit_transform(x)
        x：numpy array格式数据[n_samples,n_features]
        返回值：转换后的形式相同的array
    StandardScaler.mean_
        原始数据(训练集)中每列特征的平均值
    StandardScaler.var_
        原始数据每列特征的方差
'''

from sklearn.preprocessing import StandardScaler


def ss():
    """
    标准化
    :return:None
    """
    std = StandardScaler()
    data = std.fit_transform([[2, 3, 5, 7],[1, 8, 2, 9],[3, 4, 6, 5]])
    print(std.mean_, '\n')
    print(std.var_, '\n')
    print(data)
    return None


if __name__ == "__main__":
    ss()