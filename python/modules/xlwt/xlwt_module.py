#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
xlwt模块的使用

对xls文件的操作和创建

-xlwt模块的简单操作(简书): https://www.jianshu.com/p/fc97dd7e822c
"""


import xlwt


def basic_demo():
    """最基础的使用"""

    # 创建book和sheet
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet = workbook.add_sheet("sheet1")

    # sheet写入内容
    worksheet.write(0, 0, "首行首列")
    worksheet.write(0, 1, "首行第二列")
    worksheet.write(0, 2, "first row, third column")

    # 将文件内容保存
    workbook.save("./test.xls")


if __name__ == "__main__":
    basic_demo()

