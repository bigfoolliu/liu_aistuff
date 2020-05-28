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


def multi_sheet_demo():
    # 新建excel表
    workbook = xlsxwriter.Workbook("./multi_sheet_xlsx_test.xlsx")

    for sheet_name in ['已签到', '未签到']:
        worksheet = workbook.add_worksheet(sheet_name)
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


def worksheet_page_demo():
    """worksheet分页示例"""
    list1 = [{'name': 'tony', 'score': 100, 'pass': True}]
    list2 = [{'name': 'jim', 'score': 50, 'pass': False}]
    workbook = xlsxwriter.Workbook('./worksheet_page_text.xlsx')

    for sheet_name in ['通过', '未通过']:
        work_sheet = workbook.add_worksheet(sheet_name)
        if sheet_name == '通过':
            data_list = list1
        else:
            data_list = list2
        for data in data_list:
            print('begin at sheet {}'.format(sheet_name))
            work_sheet.write_row(0, 0, data)
            print('end at sheet {}'.format(sheet_name))
    workbook.close()i
    del workbook


if __name__ == "__main__":
    # basic_demo()
    # multi_sheet_demo()
    worksheet_page_demo()

