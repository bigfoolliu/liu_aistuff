#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu

"""
线性回归模型实践
"""


from sklearn.linear_model import LinearRegression, SGDRegressor, Ridge
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def load_boston_dataset(test_size=0.1):
    """load the inside boston dataset"""
    print("load the dataset boston")
    ld = load_boston()
    x_train, x_test, y_train, y_test = train_test_split(ld["data"], ld["target"], test_size=test_size)
    return x_train, x_test, y_train, y_test


class LinearRegressionModel():

    """
    when training model with LinearRegression algorithms, you can be the subclass
    """

    def __init__(self, x_train, y_train, x_test=None, y_test=None):
        """
        :param x_train: [n_samples, n_features] np.ndarray
        :param y_train: [n_samples, ] np.ndarray
        :param x_test: [n_samples, n_features] np.ndarray
        :param y_test: [n_samples,] np.ndarray"""
        self.lr = None  # linear regression model
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
    
    def preprocess_dataset(self):
        print(self.y_train, self.y_train.shape)
        if len(self.y_train.shape) == 1:
            self.y_train = self.y_train.reshape(-1, 1)
        
        if self.y_test is not None and len(self.y_test.shape) == 1:
            self.y_test = self.y_test.reshape(-1, 1)
    
    def standardlize(self):
        """
        standardlize preprocessing
        标准化数据，保证每个维度的特征数据方差为1，均值为0，使预测结果不会被某些维度过大的特征值主导
        """
        print("standardlize the dataset")
        std_x = StandardScaler()
        std_y = StandardScaler()

        self.x_train = std_x.fit_transform(self.x_train)  # fit(拟合) then transform(转化为标准形式)        
        self.y_train = std_y.fit_transform(self.y_train)

        if self.x_test is not None:
            self.x_test = std_x.transform(self.x_test)
        if self.y_test is not None:
            self.y_test = std_y.transform(self.y_test)

    def train_model(self):
        """
        use the standardlized tain dataset to train the model
        return: trained LinearRegression
        """
        print("train the model")
        self.lr = LinearRegression()
        self.lr.fit(self.x_train, self.y_train)
    
    def predict(self, x_test, y_test, std_y):
        """use the test dataset to test the model"""
        print("predict the price with the test data")
        y_lr_predict = self.lr.predict(x_test)
        y_lr_predict = std_y.inverse_transform(y_lr_predict)
    
    def run(self):
        self.preprocess_dataset()
        self.standardlize()
        self.train_model()


def main():
    x_train, x_test, y_train, y_test = load_boston_dataset()

    lr_boston = LinearRegressionModel(x_train, y_train)
    lr_boston.run()

    print("trained model: {}".format(lr_boston.lr))
    print("model coef_: {}".format(lr_boston.lr.coef_))  # 一次项系数
    print("model intercept_: {}".format(lr_boston.lr.intercept_))  # 位置系数


if __name__ == '__main__':
    main()
