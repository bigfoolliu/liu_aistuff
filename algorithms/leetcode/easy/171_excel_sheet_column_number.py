#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701

给定一个Excel表格中的列名称，返回其相应的列序号。
"""


def excel_sheet_column_number(s):
    """
    :param s: str
    :return: int
    """
    ret = 0
    s = s[::-1]
    counter = 0
    for i in s:
        ret += (ord(i) - 64) * (26 ** counter)
        counter += 1
    return ret


if __name__ == "__main__":
    print(excel_sheet_column_number("A"))
    print(excel_sheet_column_number("AB"))
    print(excel_sheet_column_number("ZY"))
