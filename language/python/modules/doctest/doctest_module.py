#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
doctest模块使用

- 用于测试
- 扫描模块并根据程序中内嵌的文档字符串执行测试

如果代码中没有doctest.testmod()，可以执行 python -m doctest -v doctest_module.py , 可以加-v参数来查看测试细节
"""


import doctest


def average(values):
  """Computes the arithmetic mean of a list of numbers. 注意下面一行是空行

  >>> print(average([20, 30, 70]))
  40.0
  """
  return sum(values) / len(values)



if __name__ == '__main__':
    # doctest.testmod是测试模块，verbose默认是False,意思是出错才用提示；True，对错都有执行结果
    doctest.testmod(verbose=True)

