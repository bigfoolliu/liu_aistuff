#!/usr/bin/env python3
# -*-  coding:utf-8 -*-
# author: bigfoolliu


"""
Implement atoi which converts a string to an integer.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Note:

    Only the space character ' ' is considered as whitespace character.
    Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
    Example 1:

    Input: "42"
    Output: 42

    Example 2:

    Input: "   -42"
    Output: -42
    Explanation: The first non-whitespace character is '-', which is the minus sign.
                 Then take as many numerical digits as possible, which gets 42.
    Example 3:

    Input: "4193 with words"
    Output: 4193
    Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
    
    Example 4:

    Input: "words and 987"
    Output: 0
    Explanation: The first non-whitespace character is 'w', which is not a numerical 
                 digit or a +/- sign. Therefore no valid conversion could be performed.
    Example 5:

    Input: "-91283472332"
    Output: -2147483648
    Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
                 Thefore INT_MIN (−231) is returned.


字符串转换为整数
1. 输入的空格要去掉
2. 要考虑正负号
3. 还要考虑空字符串则返回0
4. 转换数字时候，只要遇到首个非数字则停止
5. 结果不能溢出，为32-bit,大于0x7fffffff - 1,返回0x7fffffff - 1,小于-0x7fffffff，则返回 -0x7fffffff
"""


def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    str = str.strip()  # 去除字符串左右的空格
    ret = 0
    if len(str) == 0:
        return ret

    # 判断截取到的是否有正负号
    positive_flag = True
    if str[0] == "+" or str[0] == "-":
        if str[0] == "-":
            positive_flag = False
        # 截取正负号之后的数字
        str = str[1:]

    for char in str:
        if "9" >= char >= "0":  # 根据ascii码的区间来判断
            ret = ret * 10 + int(char)
        elif char < "0" or char > "9":
            break

    # 根据提取的数字确定输出结果
    if ret > 2147483647:
        if positive_flag:
            ret = 2147483647
        else:
            ret = -2147483648
    else:
        if not positive_flag:
            ret = 0 - ret

    return ret


if __name__ == "__main__":
    str_input = input("input str:")
    ret = myAtoi(str_input)
    print(ret)
