#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
datetime模块的简单使用
"""


from datetime import datetime, timedelta
import time


def get_utc_demo():
    """获取UTC时间并转换格式"""
    now_time = datetime.now()
    utc_time = now_time - timedelta(hours=8)              # UTC只是比北京时间提前了8个小时
    utc_time = utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")    # 转换成Aliyun要求的传参格式...
    print("utc_time:{} type:{}".format(utc_time, type(utc_time)))


def str_to_timestamp_demo():
    """字符串转换为时间戳"""
    time_str = "2020-02-11 14:00"
    time_stamp = time.strptime(time_str, "%Y-%m-%d %H:%M")
    print("time_stamp:{} type:{}".format(time_stamp, type(time_stamp)))

    time_stamp_float = time.mktime(time_stamp)
    print(time_stamp_float, type(time_stamp_float))


def timestamp_to_datetime_demo():
    """时间戳转换为datetime时间"""
    time_stamp = int("1581696000")
    datetime_time = datetime.fromtimestamp(time_stamp)
    print("datetime_time:{} type:{}".format(datetime_time, type(datetime_time)))


def get_add_reduce_time_demo(time_str, time_format, time_delta):
    """将字符串时间增加或者减少之后再转换为字符输出"""
    unix_time = time.mktime(time.strptime(time_str, time_format))
    datetime_obj = datetime.fromtimestamp(unix_time)

    ret_time = datetime_obj + timedelta(seconds=time_delta)
    ret_time_str = ret_time.strftime(time_format)
    return ret_time_str


if __name__ == "__main__":
    # get_utc_demo()
    # str_to_timestamp_demo()
    # timestamp_to_datetime_demo()
    print(get_add_reduce_time_demo('2020-02-15 00:00', "%Y-%m-%d %H:%M", 15*60))
    print(get_add_reduce_time_demo('2020-02-15 00:00', "%Y-%m-%d %H:%M", -15*60))

