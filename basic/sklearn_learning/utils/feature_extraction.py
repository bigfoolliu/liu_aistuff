#!/usr/bin/env python3
#!coding:utf-8

"""
字典特征提取:
把字典中一些类型数据分别转换成特征，数值特征（int, float等）不必要转换
"""

from sklearn.feature_extraction import DictVectorizer


def dectvec():
    """
    字典数据抽取函数
    """
    # 实例化
    dict = DictVectorizer()
    # 调用fit_transform
    data = dict.fit_transform([{'city':'北京','temperature':'100'},
                                {'city':'上海','temperature':'90'},
                                {'city':'深圳','temperature':'70'},
                                {'city':'广州','temperature':'80'}])
    print(dict.get_feature_names())
    print(data)
    return None


if __name__ == "__main__":
    dectvec()