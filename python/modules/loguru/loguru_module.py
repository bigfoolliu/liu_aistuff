#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
loguru模块
更简单的日志记录方式
"""

from loguru import logger


def basic_use():
    """最简单使用"""
    logger.debug("this is a debug message")
    logger.warning("this is a warning message")


def use_file():
    """将日志记录到文件中"""
    logger.add("runtime.log")
    logger.debug("runtime log")


def self_define():
    """add可以设置更多的参数，level可以设置超过该等级的则添加"""
    trace = logger.add('runtime2.log', format="{time} {level} {message}", level="INFO")

    logger.info("this is another info log")
    logger.debug("this is another debug log")
    logger.warning("this is another warning log")

    logger.remove(trace)
    logger.info("this is infooooo log")


if __name__ == "__main__":
    # basic_use()
    # use_file()
    self_define()
