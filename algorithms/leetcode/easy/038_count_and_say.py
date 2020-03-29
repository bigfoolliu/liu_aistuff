#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string.

 

Example 1:

Input: 1
Output: "1"
Example 2:

Input: 4
Output: "1211"

固定的数组的生成:
- 第一个数字固定为1
- 后面的数字依次为上一个数字序列的读法

思路：
"""


def count_and_say(n):
    """
    :param n: int
    :return str
    """
    s = "1"
    # 第一次遍历一次次的生成
    for j in range(1, n):
        t = s[0]
        tmp = ""
        count = 0  # 统计重复出现的数字的个数
        # 用来遍历每一次的数字，统计其读法
        for i in range(0, len(s), 1):
            if t == s[i]:
                count += 1
            else:
                tmp = tmp + str(count) + t
                t = s[i]
                count = 1
            if i == len(s) - 1:
                tmp = tmp + str(count) + t  # 将结果合并
        s = tmp
    return s


if __name__ == "__main__":
    print(count_and_say(1))
    print(count_and_say(2))
    print(count_and_say(3))
    print(count_and_say(4))
    print(count_and_say(5))
    print(count_and_say(6))
    print(count_and_say(7))
    print(count_and_say(8))
    print(count_and_say(9))
    print(count_and_say(10))
