#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
datetime模块的简单使用
"""

from datetime import datetime, timedelta
import time
from dateutil.relativedelta import relativedelta


def get_utc_demo():
    """
    获取UTC时间并转换格式
    """
    now_time = datetime.now()
    utc_time = now_time - timedelta(hours=8)  # UTC只是比北京时间提前了8个小时
    utc_time = utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")  # 转换成Aliyun要求的传参格式...
    print("utc_time:{} type:{}".format(utc_time, type(utc_time)))


def str_to_timestamp_demo():
    """
    字符串转换为时间戳
    """
    time_str = "2020-02-11 14:00"
    time_stamp = time.strptime(time_str, "%Y-%m-%d %H:%M")
    print("time_stamp:{} type:{}".format(time_stamp, type(time_stamp)))

    time_stamp_float = time.mktime(time_stamp)
    print(time_stamp_float, type(time_stamp_float))


def timestamp_to_datetime_demo():
    """
    时间戳转换为datetime时间
    """
    time_stamp = int("1581696000")
    datetime_time = datetime.fromtimestamp(time_stamp)
    print("datetime_time:{} type:{}".format(datetime_time, type(datetime_time)))


def get_add_reduce_time_demo(time_str, time_format, time_delta):
    """
    将字符串时间增加或者减少之后再转换为字符输出
    """
    unix_time = time.mktime(time.strptime(time_str, time_format))
    datetime_obj = datetime.fromtimestamp(unix_time)

    ret_time = datetime_obj + timedelta(seconds=time_delta)
    ret_time_str = ret_time.strftime(time_format)
    return ret_time_str


def timedelta_is_year_demo():
    """
    当时间间隔年的时候
    """
    now = datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    print("now_str:", now_str)

    year_later = now + relativedelta(years=1)
    year_later_str = year_later.strftime("%Y-%m-%d %H:%M:%S")
    print("1 year later:", year_later_str)


def calculate_months(begin_date, end_date):
    """
    计算两个日期之间相隔的月份, 并将连续的月份输出
    eg: 输入2019-10 2020-01, 输出[2019-10, 2019-11, 2019-12, 2020-01]
    """
    if begin_date > end_date:
        return None

    begin_year = int(begin_date[0:4])
    end_year = int(end_date[0:4])
    begin_month = int(begin_date[5:7])
    end_month = int(end_date[5:7])

    month_delta = (end_year - begin_year) * 12 + (end_month - begin_month)

    ret = []
    for i in range(month_delta + 1):
        if i == 0:
            ret.append(begin_date)
            continue
        # 新的相加
        _temp_year = begin_year + (begin_month + i) // 12
        _temp_month = (begin_month + i) % 12
        if _temp_month == 0:
            _temp_month = 12
        ret.append("-".join([str(_temp_year), str(_temp_month)]))
    return ret


if __name__ == "__main__":
    # get_utc_demo()
    # str_to_timestamp_demo()
    # timestamp_to_datetime_demo()
    # print(get_add_reduce_time_demo('2020-02-15 00:00', "%Y-%m-%d %H:%M", 15*60))
    # print(get_add_reduce_time_demo('2020-02-15 00:00', "%Y-%m-%d %H:%M", -15*60))

    # timedelta_is_year_demo()

    print(calculate_months('2019-10', '2020-02'))  # [2019-10, 2019-11, 2019-12, 2020-01, 2020-02]
    print(calculate_months('2020-01', '2020-02'))  # [2020-01, 2020-02]
