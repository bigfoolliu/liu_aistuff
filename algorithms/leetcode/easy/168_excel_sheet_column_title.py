#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given a positive integer, return its corresponding column title as appear in an Excel sheet.

For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 
    ...
Example 1:

Input: 1
Output: "A"
Example 2:

Input: 28
Output: "AB"
Example 3:

Input: 701
Output: "ZY"

给定一个正整数，返回它在 Excel 表中相对应的列名称。
"""


def excel_sheet_column_from_title(n):
    """
    :param n: int
    :return: str
    """
    if (n - 1) // 26 == 0:
        return chr(65 + (n - 1) % 26)
    else:
        return excel_sheet_column_from_title((n - 1) // 26) + chr(65 + (n - 1) % 26)


if __name__ == "__main__":
    print(excel_sheet_column_from_title(1))
    print(excel_sheet_column_from_title(28))
    print(excel_sheet_column_from_title(701))
