#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
traceback模块使用

用来跟踪异常返回信息

format_exc() 返回字符串
print_exc() 直接给打印出来
故 traceback.print_exc() 与 print (traceback.format_exc()) 显示效果是一样的，
但print_exc()还可以接受file参数直接写入到一个文件中。
"""


import traceback
import sys


try:
    a = 1 / 0
except ZeroDivisionError:
    traceback.print_exc()  # 直接输出错误堆栈
    # traceback.format_exc()
    # traceback.print_exc(file=open('log.log', mode='a', encoding='utf-8'))  # 将错误输出到文件

    exc_type, exc_value, exc_traceback = sys.exc_info()  # 精确定位错误到哪一行
    print("*** tb_lineno:", exc_traceback.tb_lineno)
