#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
importlib使用

- 博客园python importlib使用: https://www.cnblogs.com/bad-robot/p/9746870.html
"""

import importlib


def basic_demo():
    _service = "importlib_test_module.TestClass".split(".")
    print(_service)
    _lib = importlib.import_module(".".join(_service[0:-1]))
    print(_lib, type(_lib))
    print(getattr(_lib, _service[-1]))


if __name__ == "__main__":
    basic_demo()
