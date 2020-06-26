#!/usr/bin/env python3
# -*- coding:utf-8  -*-
# author: bigfoolliu


"""
sys模块
"""

import sys


def basic_demo():
    # 获取对象的引用计数
    a = "hahaha"
    print(sys.getrefcount(a))


def args_demo():
    """sys模块常用的一些变量"""
    print(f"sys.abiflags: {sys.abiflags}")
    print(f"sys.argv: {sys.argv}")  # 返回传给python解释器的参数列表

    print(f"sys.base_exec_prefix: {sys.base_exec_prefix}")
    print(f"sys.base_prefix: {sys.base_prefix}")

    print(f"sys.byteorder: {sys.byteorder}")
    # print(f"sys.builtin_module_names: {sys.builtin_module_names}")

    # print(f"sys.copyright: {sys.copyright}")  # 获取python解释器的版本信息
    print(f"sys.executable: {sys.executable}")  # 获取python解释器的执行位置
    print(f"sys.path: {sys.path}")  # 获取python解释器查找模块的路径列表

    """
    系统              平台值
    AIX              'aix'
    Linux            'linux'
    Windows          'win32'
    Windows/Cygwin   'cygwin'
    macOS            'darwin'
    """
    print(f"sys.platform: {sys.platform}")  # 获取系统平台信息，可以根据不同的运行平台来使用不同的代码

    print(f"sys.maxsize: {sys.maxsize}")  # 获取系统的最大整数


def func_demo():
    """sys模块使用函数"""
    print(f"sys.getsizeof([1, 2, 3]): {sys.getsizeof([1, 2, 3])}")  # 获取一个对象占用空间的比特数



if __name__ == "__main__":
    # basic_demo()
    args_demo()
    # func_demo()

