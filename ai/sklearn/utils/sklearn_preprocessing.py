#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


from sklearn.feature_extraction import DictVectorizer
from sklearn.feature_selection import VarianceThreshold
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler


class SklearnPreprocessing(object):

    def dectvec(self):
        """
        字典数据抽取函数
        字典特征提取:
        把字典中一些类型数据分别转换成特征，数值特征（int, float等）不必要转换
        """
        # 实例化
        dict = DictVectorizer()
        # 调用fit_transform
        data = dict.fit_transform([{'city': '北京', 'temperature': '100'},
                                   {'city': '上海', 'temperature': '90'},
                                   {'city': '深圳', 'temperature': '70'},
                                   {'city': '广州', 'temperature': '80'}])
        print(dict.get_feature_names())
        print(data)
        return None

    def var(self):
        """
        sklearn特征选择API：sklearn.feature_selection.VarianceThreshold()
        VarianceThreshold(threshold=0.0)
            删除所有低方差特征
        Variance.fit_transform(x)
            x:numpy array格式的数据[n_samples, n_features]
            返回值：训练集中差异低于threshold的特征将被删除
            默认值为保留所有非零方差的特征，即删除所有样本中具有相同值的特征
        
        特征选择，删除低方差的特征
        :return:None
        """
        var = VarianceThreshold()
        data = var.fit_transform([[1, 2, 3, 4], [0, 2, 5, 4], [8, 2, 6, 7]])

        print(data)
        return None

    def pca(self):
        """
        PCA(n_components=None)
        将数据分解为较低的维数空间
        n_components:为小数时，表示保留0-100%的信息，基本取90-95%的数据信息最好；为整数时，表示减少到的特征数量，使用较少
        PCA.fit_transform(x)
            x:numpy array格式的数据[n_samples, n_features]
            返回值：转换后指定维度的array
        
        主成分分析
        :return:None
        """
        pca = PCA(n_components=0.92)

        data = pca.fit_transform([[2, 0, 2, 34], [23, 3, 43, 5], [12, 3, 54, 6], [23, 45, 5, 67]])
        print(data)
        return None

    def ss(self):
        """
        sklearn标准化API：sklearn.preprocessing.StandardScaler
        StandardScaler.fit_transform(x)
            x：numpy array格式数据[n_samples,n_features]
            返回值：转换后的形式相同的array
        StandardScaler.mean_
            原始数据(训练集)中每列特征的平均值
        StandardScaler.var_
            原始数据每列特征的方差
        
        标准化
        :return:None
        """
        std = StandardScaler()
        data = std.fit_transform([[2, 3, 5, 7], [1, 8, 2, 9], [3, 4, 6, 5]])
        print(std.mean_, '\n')
        print(std.var_, '\n')
        print(data)
        return None

    def mm(self):
        """
        sklearn归一化API：sklearn.preprocessing.MinMaxScaler
        MinMaxScaler(featrure_range(0,1),...)
            每个特征值的缩放给定范围默认为[0,1]
        MinMaxScaler.fit_transform(x)
            x：numpy array格式的数据[n_samples,n_features]
            返回值：转换后的形状相同的array

        归一化步骤：
        1.实例化MinMaxScaler
        2.通过fit_transform()转换

        归一化处理
        :return:None
        """
        mm = MinMaxScaler()
        data = mm.fit_transform([[90, 2, 10, 40], [60, 4, 15, 15]])

        print(data)
        return None


def main():
    sp = SklearnPreprocessing()
    sp.dectvec()
    sp.var()
    sp.pca()
    sp.mm()


if __name__ == "__main__":
    main()
