#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
tenacity模块，用于重试

在什么情况下才进行重试？
重试几次呢?
重试多久后结束？
每次重试的间隔多长呢？
重试失败后的回调？
"""


import time
from requests import exceptions
from tenacity import retry, wait_fixed, stop_after_attempt, stop_after_delay, retry_if_exception_type, retry_if_result


# 1.无条件重试，重试间隔2s
@retry(wait=wait_fixed(2))
def retry_demo():
    print('trying...')
    raise Exception


# 2.只重试5次
@retry(stop=stop_after_attempt(5))
def retry_demo1():
    print('trying...')
    time.sleep(0.5)
    raise Exception


# 3.重试3s后不再重试
@retry(stop=stop_after_delay(3))
def retry_demo2():
    print('trying...')
    time.sleep(0.5)
    raise Exception


# 4.设置重试的条件, 同时设置一个终止的条件
@retry(retry=retry_if_exception_type(exceptions.Timeout), stop=stop_after_attempt(3))
def retry_demo3():
    print('trying...')
    time.sleep(1)
    raise exceptions.Timeout


# 5.设置回调函数
def is_false(value):
    """重试的条件,value是函数的返回值"""
    return value is False


def call_back(retry_state):
    """回调函数"""
    print(f'call_back, return value is{retry_state},{type(retry_state)}')
    print(f'value is {retry_state.outcome.result()}')


@retry(retry=retry_if_result(is_false),
       stop=stop_after_attempt(3),
       retry_error_callback=call_back)  # call_back接收的是tenacity.Future对象
def retry_demo4():
    print('trying...')
    time.sleep(1)
    return False


if __name__ == '__main__':
    # retry_demo()
    # retry_demo1()
    # retry_demo2()
    # retry_demo3()
    retry_demo4()
