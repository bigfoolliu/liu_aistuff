#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

    Example 1:

    Input: 121
    Output: true
    Example 2:

    Input: -121
    Output: false
    Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
    Example 3:

    Input: 10
    Output: false
    Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
    Follow up:

    Could you solve it without converting the integer to a string?

判断一个整数是否在不转换为字符串的情况下为为回文
"""


def isPalindrome(x):
    """
    判断输入的整数是否为回文数字
    :type x: int
    :rtype: bool
    """
    # 将该数字逆序输出和原始的对比,相同则为回文
    x_list = [i for i in str(x)]
    print("[INFO]the x_list:", x_list)

    reverse_list = []
    ret = False
    
    import copy
    x_list_copy = copy.deepcopy(x_list)
    for i in range(len(x_list)):
        reverse_list.append(x_list_copy.pop())

    print("[INFO]the reverse_list:", reverse_list)
    
    # 判断两个列表是否相等,元素的数量和位置相同
    import operator
    if operator.eq(x_list, reverse_list):
        ret = True
    
    return ret


if __name__ == "__main__":
    num = int(input("please input an integer:"))
    is_palindrome = isPalindrome(num)

    if not is_palindrome:
        print("{} is not a palindrome.".format(num))
    print("{} is a palindrome.".format(num))
