#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
time模块的使用
"""

import time


def basic_demo():
    time_stamp = time.time()  # 时间戳, 1610502602.780431
    print(time_stamp)

    local_time = time.localtime()  # 当前的时间元组, time.struct_time(tm_year=2021, tm_mon=1, tm_mday=13, tm_hour=9, tm_min=50, tm_sec=46, tm_wday=2, tm_yday=13, tm_isdst=0), tm_wday表示是一周中的第几天(0-6, 0表示周一)， tm_yday表示一年中的第几天(1-366), tm_isdat表示是否为夏令时(-1, 0, 1, -1)
    print(local_time.tm_yday)

    local_time2 = time.localtime(1610501602.780431)  # 指定时间戳获取时间元组
    print(local_time2)

    asc_time = time.asctime()  # 'Wed Jan 13 10:02:25 2021'
    print(asc_time)


def stamp_to_asc_demo():
    """将时间戳转换为具体日期"""
    cur_time_str = time.asctime(time.localtime(time.time()))
    print(cur_time_str)


def format_time_demo():
    """
    将时间按照指定格式输出
    %y 年，去掉世纪的年份,如20
    %Y 年，完整的年，如2020
    %m 月
    %d 日
    %H 时
    %M 分
    %S 秒

    %x 日期，2020/01/01
    $X 时间，23:00:00
    %c 详细日期时间，Wed Jan 13 10:13:52 2021

    %p 上下午
    
    %j 指定一天是一年当中的第几天
    %U 该年中的几个星期,从周日算起
    %w 一个
    """
    _time = time.strftime('%c')
    print(_time)


def main():
    # basic_demo()
    # stamp_to_asc_demo()
    format_time_demo()


if __name__ == '__main__':
    main()
