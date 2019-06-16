#!/usr/bin/env python3
#!coding:utf-8


'''
PCA(n_components=None)
    将数据分解为较低的维数空间
    n_components:为小数时，表示保留0-100%的信息，基本取90-95%的数据信息最好；为整数时，表示减少到的特征数量，使用较少
    PCA.fit_transform(x)
        x:numpy array格式的数据[n_samples, n_features]
        返回值：转换后指定维度的array
'''
from sklearn.decomposition import PCA


def pca():
    """
    主成分分析
    :return:None
    """
    pca = PCA(n_components=0.92)

    data = pca.fit_transform([[2, 0, 2, 34], [23, 3, 43, 5], [12, 3, 54, 6], [23, 45, 5, 67]])
    print(data)
    return None


if __name__ == "__main__":
    pca()