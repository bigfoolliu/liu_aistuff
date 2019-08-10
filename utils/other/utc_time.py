#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
将本地时间转换为UTC时间
"""

from datetime import datetime, timedelta

def get_utc():
    now_time = datetime.now()
    utc_time = now_time - timedelta(hours=8)              # UTC只是比北京时间提前了8个小时
    utc_time = utc_time.strftime("%Y-%m-%dT%H:%M:%SZ")    # 转换成Aliyun要求的传参格式...
    return utc_time

print(get_utc())
