#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""

Python中的垃圾回收是以引用计数为主，分代收集为辅。

1、导致引用计数+1的情况
    对象被创建，例如a=23
    对象被引用，例如b=a
    对象被作为参数，传入到一个函数中，例如func(a)
    对象作为一个元素，存储在容器中，例如list1=[a,a]
2、导致引用计数-1的情况
    对象的别名被显式销毁，例如del a
    对象的别名被赋予新的对象，例如a=24
    一个对象离开它的作用域，例如f函数执行完毕时，func函数中的局部变量（全局变量不会）
    对象所在的容器被销毁，或从容器中删除对象

gc模块示例

- python gc模块介绍: https://blog.csdn.net/qq_38260497/article/details/87879064
- gc模块提供一个接口给开发者设置垃圾回收的选项

gc.enable()
gc.disable()
gc.isebabled()
gc.collect([generation])
gc.set_debug(flags)
gc.get_debug()
gc.get_objects()

gc.is_tracked(obj)
gc.get_count()
gc.get_threadshold()
"""

import gc
import sys


def get_ref_times():
    """
    查看对象被应用的次数
    """
    a = 'what the hell'
    print(sys.getrefcount(a))
    del a
    # print(sys.getrefcount(a))


class A(object):

    pass


def basic_demo():
    a1 = A()
    a2 = A()

    a1.a = a2  # 循环引用，会导致内存泄漏
    a2.a = a1

    del a1
    del a2

    print(gc.garbage)  # 显示垃圾
    print('*' * 100)
    gc.collect()  # 显式的执行垃圾回收
    print('*' * 100)
    print(gc.garbage)



def collect_demo():
    """
    显式进行垃圾回收的示例
    """
    pass


if __name__ == "__main__":
    # TODO:
    # get_ref_times()


    gc.set_debug(gc.DEBUG_LEAK)  # 设置gc的模块的日志,进行内存泄漏的检查
    basic_demo()

