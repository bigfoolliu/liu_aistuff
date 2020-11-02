#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
importlib使用

- 博客园python importlib使用: https://www.cnblogs.com/bad-robot/p/9746870.html
- 以及导包的多种方式
"""

import importlib
import sys
import os


# 将当前路径加入导入路径
sys.path.append(os.path.abspath(__file__))
print(sys.path)


from package1.module_p1 import test_pkg1


if __name__ == "__main__":
    test_pkg1()

