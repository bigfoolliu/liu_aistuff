#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.


找到卖出股票的最佳时机
"""


def best_time_to_sell_stock(prices):
    """
    :param prices: list
    :return: int
    """
    if not prices:
        return 0

    ret_index = 0  # 结果的索引
    min_item = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        min_item = min(prices[i], min_item)
        if prices[i] - min_item > max_profit:
            ret_index = i
            max_profit = max(max_profit, prices[i] - min_item)

    return ret_index + 1  # 天数从1开始


if __name__ == "__main__":
    prices = [7, 1, 5, 300, 6, 4]
    # prices = [7, 1, 5, 3, 6, 4]
    print(best_time_to_sell_stock(prices))
