#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

找到买卖股票的最佳时机，但是可以尽量多次的买卖

一般人可能会想，怎么判断不是第三天就卖出了呢? 
这里就把问题复杂化了，根据题目的意思，当天卖出以后，当天还可以买入，
所以其实可以第三天卖出，第三天买入，第四天又卖出（（5-1）+ （6-5） === 6 - 1）。
所以算法可以直接简化为只要今天比昨天大，就卖出。
"""


def best_time_to_sell_stock(prices):
    """
    :param prices: list
    :return: int，最大的利润值
    """
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            max_profit += prices[i] - prices[i-1]
    return max_profit


if __name__ == "__main__":
    # prices = [7,1,5,3,6,4]
    # prices = [1,2,3,4,5]
    prices = [7,6,4,3,1]
    print(best_time_to_sell_stock(prices))
