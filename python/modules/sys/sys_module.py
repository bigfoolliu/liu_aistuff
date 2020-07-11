#!/usr/bin/env python3
# -*- coding:utf-8  -*-
# author: bigfoolliu


"""
sys模块
"""

import sys


def basic_demo():
    # 获取对象的引用计数
    a = "hello"
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


def exit_demo():
    """
    sys.exit()通过引发SystemExit异常，如果没有捕获该异常将会退出，捕获了可以继续执行
    os._exit()会直接将python程序终止，之后的所有代码都不会继续执行
    一般情况下使用sys.exit()即可，一般在fork出来的子进程中使用os._exit()
    一般来说os._exit() 用于在线程中退出
    sys.exit() 用于在主线程中退出。
    """
    print("start")
    sys.exit(0)  # 0表示成功
    # sys.exit(1)  # 1或其他数字表示失败


def stdin_demo():
    """
    https://www.cnblogs.com/keye/p/7859181.html
    """
    iowrapper = sys.stdin  # 得到_io.TextIOWrapper对象
    print(iowrapper, type(iowrapper))

    fd = iowrapper.fileno()
    print(fd, type(fd))

    try:
        while True:
            a = sys.stdin.readline()
            print(f"your input is {a}")  # 此时的a会自带换行符\n
    except KeyboardInterrupt:  # 需要在终端中来捕获，pycharm中失败
        print("exit")


if __name__ == "__main__":
    # basic_demo()
    # args_demo()
    # func_demo()
    # exit_demo()
    stdin_demo()
