#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
calendar模块

日历展示
"""

import calendar


def basic_demo():
    # year = calendar.calendar(theyear=2020)  # 日历
    year = calendar.calendar(theyear=2020, w=3, l=1, c=8)  # c：每月间隔距离 w：每日宽度间隔 l：每星期行数
    print(year)

    month = calendar.month(theyear=2020, themonth=1, w=3, l=1)  # 打印指定月份
    print(month)

    print('2020 is leap year: {}'.format(calendar.isleap(2020)))  # 判断闰年
    print(calendar.leapdays(2000, 2020))  # 判断两个年份之间有多少个闰年, 包含y1，但是不包含y2

    print(calendar.monthrange(year=2020, month=1))  # (1, 31)输出元组(a, b)，a代表该月从星期几开始；6代表星期天，取值为0-6 b代表该月总共有多少天

    print(calendar.weekday(year=2020, month=1, day=1))  # 根据年月日输出那天是星期几，返回值是0-6，0代表星期1，6代表星期天


def main():
    basic_demo()


if __name__ == '__main__':
    main()
