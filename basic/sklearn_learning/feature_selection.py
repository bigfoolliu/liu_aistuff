#!/usr/bin/env python3
#!coding:utf-8


'''
sklearn特征选择API：sklearn.feature_selection.VarianceThreshold()
    VarianceThreshold(threshold=0.0)
        删除所有低方差特征
    Variance.fit_transform(x)
        x:numpy array格式的数据[n_samples, n_features]
        返回值：训练集中差异低于threshold的特征将被删除
        默认值为保留所有非零方差的特征，即删除所有样本中具有相同值的特征
'''
from sklearn.feature_selection import VarianceThreshold


def var():
    """
    特征选择，删除低方差的特征
    :return:None
    """
    var = VarianceThreshold()
    data = var.fit_transform([[1, 2, 3 , 4],[0, 2, 5, 4],[8, 2, 6, 7]])

    print(data)
    return None


if __name__ == "__main__":
    var()