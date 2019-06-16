#!/bin/env python3
#!coding:utf-8


"""
线性回归模型实践
"""


from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np


class Boston():

    def __init__(self):
        self.lr = None  # linear regression model

    def load_dataset(self, test_size=0.1):
        """load the dataset"""
        print("load the dataset boston")
        ld = load_boston()
        x_train, x_test, y_train, y_test = train_test_split(ld["data"], ld["target"], test_size=test_size)
        return x_train, x_test, y_train, y_test
    
    def standardlize(self, x_train, x_test, y_train, y_test):
        """
        standardlize preprocessing
        标准化数据，保证每个维度的特征数据方差为1，均值为0，使预测结果不会被某些维度过大的特征值主导
        """
        print("standardlize the dataset")
        try:
            std_x = StandardScaler()
            x_train = std_x.fit_transform(x_train)  # fit(拟合) then transform(转化为标准形式)
            x_test = std_x.transform(x_test)

            std_y = StandardScaler()
            y_train = y_train.reshape(-1, 1)
            y_test = y_test.reshape(-1, 1)
            y_train = std_y.fit_transform(y_train)
            y_test = std_y.transform(y_test)
        except:
            raise Exception("standardlize failed")

        return x_train, x_test, y_train, y_test
    
    def train_model(self, x_train, y_train):
        """
        use the standardlized tain dataset to train the model
        return: trained LinearRegression
        """
        print("train the model")
        self.lr = LinearRegression()
        self.lr.fit(x_train, y_train)
    
    def predict(self, x_test, y_test, std_y):
        """use the test dataset to test the model"""
        print("predict the price with the test data")
        y_lr_predict = self.lr.predict(x_test)
        y_lr_predict = std_y.inverse_transform(y_lr_predict)
    
    def run(self):
        x_train, x_test, y_train, y_test = self.load_dataset()
        x_train, x_test, y_train, y_test = self.standardlize(x_train, x_test, y_train, y_test)
        self.train_model(x_train, y_train)


def main():
    boston = Boston()
    boston.run()
    print("trained model: {}".format(boston.lr))
    print("model coef_: {}".format(boston.lr.coef_))  # 一次项系数
    print("model intercept_: {}".format(boston.lr.intercept_))  # 位置系数


if __name__ == '__main__':
    main()
