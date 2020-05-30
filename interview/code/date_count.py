#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
输入年月日，计算是改年的第几天
"""
from datetime import datetime


def day_count(year, month, day):
    return (datetime(year, month, day) - datetime(year, 1, 1)).days + 1


print(day_count(2019, 1, 1))
print(day_count(2019, 2, 1))
print(day_count(2019, 2, 28))
