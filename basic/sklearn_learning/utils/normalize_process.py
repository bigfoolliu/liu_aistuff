#!/usr/bin/env python3
#!coding:utf-8


'''
sklearn归一化API：sklearn.preprocessing.MinMaxScaler
    MinMaxScaler(featrure_range(0,1),...)
        每个特征值的缩放给定范围默认为[0,1]
    MinMaxScaler.fit_transform(x)
        x：numpy array格式的数据[n_samples,n_features]
        返回值：转换后的形状相同的array

归一化步骤：
1.实例化MinMaxScaler
2.通过fit_transform()转换
'''

from sklearn.preprocessing import MinMaxScaler

def mm():
    """
    归一化处理
    :return:None
    """
    mm = MinMaxScaler()
    data = mm.fit_transform([[90,2,10,40],[60,4,15,15]])

    print(data)
    return None


if __name__ == "__main__":
    mm()