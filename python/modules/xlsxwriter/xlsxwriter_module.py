#!/usr/bin/env python3
# -*- coding:utf-8  -*-
# author: bigfoolliu


"""
xlsxwriter模块的使用

- xlsxwriter使用(简书): https://www.jianshu.com/p/187e6b86e1d9
- xlsxwriter使用(blog): https://www.cnblogs.com/brightbrother/p/8671077.html
- 目前只能创建,不能读取excel文件
"""


import xlsxwriter



def basic_demo():
    # 新建excel表
    workbook = xlsxwriter.Workbook("./xlsx_test.xlsx")
    worksheet = workbook.add_worksheet("sheet1")

    # 增加工作样式
    bold = workbook.add_format(dict(bold=True, border=1))

    # 写入单个单元格数据
    worksheet.write(0, 0, "row1,column1", bold)

    # 写入行数据
    worksheet.write_row("A1", ["a", "b", "c"])

    # 写入列数据
    worksheet.write_column("B2", [10, 20, 30])

    # 操作完成一定要关闭
    workbook.close()


if __name__ == "__main__":
    basic_demo()

