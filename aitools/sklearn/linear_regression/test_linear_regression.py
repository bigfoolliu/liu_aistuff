
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


import numpy as np
import unittest
from linear_model import LinearRegressionModel


class TestLinearRegressionModel(unittest.TestCase):

    """测试用例必须以Test开头"""

    def setUp(self):
        """每个测试用例执行前做的环境配置"""
        self.x_train = np.array([1, 2, 3])
        self.y_train = np.array([4, 5, 6])
        self.lr_test = LinearRegressionModel(self.x_train, self.y_train)
    
    def tearDown(self):
        """每个测试用例执行结束之后做的环境清理"""
        pass
    
    def test_linear_regression_model(self):
        """测试方法以test开头"""
        self.lr_test.run()
        print(self.lr_test.lr.coef_)
        assert self.lr_test.lr.coef_ == 1
        print(self.lr_test.lr.intercept_)
        assert self.lr_test.lr.intercept_ == 3


if __name__ == '__main__':
    unittest.main()
    