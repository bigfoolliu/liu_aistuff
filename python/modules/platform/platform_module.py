#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
platform模块示例
"""

import platform


def basic_demo():
    """基础展示"""
    print("平台架构为：", platform.machine())
    print("网络名称(主机名): ", platform.node())
    print("系统版本: ", platform.platform())
    print("处理器名称: ", platform.processor())
    print("系统名称: ", platform.system())
    print("系统版本为: ", platform.version())
    print("系统位数为：", platform.architecture())

    print("汇总信息为: ", platform.uname())


def python_demo():
    """展示python相关的信息"""
    print("python build信息: ", platform.python_build())
    print("python 编译器信息：", platform.python_compiler())
    print("python 分支: ", platform.python_branch())
    print("python 执行器信息：", platform.python_implementation())
    print("python 版本：", platform.python_version())
    print("python 版本元组：", platform.python_version_tuple())
    print("python 修订版本：", platform.python_revision())


if __name__ == "__main__":
    basic_demo()
    python_demo()

