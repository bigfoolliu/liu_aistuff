#!/usr/bin/env python
#!coding:utf-8


"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

    string convert(string s, int numRows);
    Example 1:

    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"
    Example 2:

    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:

    P     I    N
    A   L S  I G
    Y A   H R
    P     I
"""


def convert(s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    # 如果输入的行数为１或者超过字符串长度，直接输出原始字符串
    if numRows == 1 or numRows >= len(s):
        return s

    ret = [""] * numRows
    #　idx为下标，step为单次前进的步数
    idx, step = 0, 1
    for i in s:
        ret[idx] += i
        # 如果为第一行则向下增加
        if idx == 0:
            step = 1
        # 如果到了最后一行，则往回
        elif idx == numRows - 1:
            step = -1
        idx += step
    return ''.join(ret)


while True:
    s = input("输入测试字符串(quit结束):")
    if s == "quit":
        break
    numRows = int(input("请输入行数:"))
    ret = convert(s, numRows)
    print("[RESULT]:{}".format(ret))
    print("\n")
