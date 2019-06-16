
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu


import numpy as np
import unittest
from linear_model import LinearRegressionModel

lr_test.run()
print(lr_test.lr.coef_)
print(lr_test.lr.intercept_)


class TestLinearRegressionModel(unittest.TestCase):

    """测试用例必须以Test开头"""

    def setUp(self):
        """每个测试用例执行前做的环境配置"""
        x_train = np.array([1, 2, 3])
        y_train = np.array([4, 5, 6])
        lr_test = LinearRegressionModel(x_train, y_train)
    
    def tearDown(self):
        """每个测试用例执行结束之后做的环境清理"""
        pass
    
    def test_linear_regression_model(self):
        """测试方法以test开头"""