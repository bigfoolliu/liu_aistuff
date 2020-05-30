#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
把n个骰子扔在地上, 所有骰子朝上一面的点数和为s。
输入n, 打印出s的所有可能的值出现的概率
"""

import matplotlib.pyplot as plt


# TODO:UNKNOWN
# 基于循环求点数, 时间性能好


def print_probability(number):
    if number < 1:
        return
    max_val = 6
    # 构造两个数组来存储骰子点数的每一个总数出现的次数
    # 在一次循环中, 第一个数组中的第n个数字表示骰子和为n出现的次数(从0开始)
    # 在下次循环中, 另一个数组的第n个数字设为前一个数组对应的第n-1、n-2、n-3、n-4、n-5、n-6之和
    prob_storage = [[], []]
    prob_storage[0] = [0] * (max_val * number + 1)
    flag = 0
    for i in range(1, max_val + 1):
        prob_storage[flag][i] = 1
    print(prob_storage)

    for time in range(2, number + 1):
        prob_storage[1 - flag] = [0] * (max_val * number + 1)
        for pCur in range(time, max_val * time + 1):
            diceNum = 1
            while diceNum < pCur and diceNum <= max_val:
                prob_storage[1 - flag][pCur] += prob_storage[flag][pCur - diceNum]
                diceNum += 1
        flag = 1 - flag
    print(prob_storage)

    total = max_val ** number  # 总的可能组合数
    ret_x, ret_y = [], []
    for i in range(number, max_val * number + 1):
        ratio = prob_storage[flag][i] / float(total)
        print("{}: {:e}".format(i, ratio))
        ret_x.append(i)
        ret_y.append(ratio)

    return ret_x, ret_y


_x, _y = print_probability(5)
print(_x)
print(_y)

# plt.plot(_x, _y)
plt.bar(_x, _y)
plt.show()
