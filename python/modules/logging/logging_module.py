#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python logging模块的使用

- https://www.cnblogs.com/liujiacai/p/7804848.html

FATAL：致命错误
CRITICAL：特别糟糕的事情，如内存耗尽、磁盘空间为空，一般很少使用
ERROR：发生错误时，如IO操作失败或者连接问题
WARNING：发生很重要的事件，但是并不是错误时，如用户登录密码错误
INFO：处理请求或者状态变化等日常事务
DEBUG：调试过程中使用DEBUG等级，如算法中每个循环的中间状态
"""


import json
import logging
import logging.config
import os
from logging.handlers import RotatingFileHandler

import yaml


def basic_demo():
    """最基本的使用"""
    # 设置等级，等于或大于该等级的才能显示
    # logging.basicConfig(level=logging.DEBUG)
    logging.info("this is info")
    logging.debug("this is debug")
    logging.warning("this is warning")
    logging.critical("this is critical")
    logging.error("this is error")


def set_format_demo():
    # 设置日志输出格式，时间，代码，等级，以及具体信息
    my_format = "%(asctime)s-%(name)s-%(module)s-%(pathname)s-%(lineno)s-%(levelname)s-%(message)s"
    logging.basicConfig(format=my_format)
    logging.debug("this is debug")
    logging.warning("this is warning")
    logging.critical("this is critical")
    logging.error("this is error")


def handler_demo():
    """增加handler"""
    stupid_logger = logging.Logger("stupid_logger")
    stupid_logger.setLevel(logging.DEBUG)

    # 将日志写入文件，且该文件会自动增加
    log_handler = RotatingFileHandler(filename="logs/logging_module.log", maxBytes=1024*1024*1, backupCount=10)
    log_formatter = logging.Formatter("%(asctime)s-%(module)s-%(lineno)s:%(message)s")
    log_handler.setFormatter(log_formatter)

    # 将日志同时输出到控制台
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    stupid_logger.addHandler(log_handler)
    stupid_logger.addHandler(console_handler)

    stupid_logger.debug("tis is stupid logger debug")
    stupid_logger.info("this is stupid logger info")
    stupid_logger.warning("this is stupid logger warning")
    stupid_logger.critical("this is stupid logger critical")
    stupid_logger.error("this is stupid logger error")


def set_log_with_yaml(default_path="logging.yaml", default_level=logging.DEBUG, env_key="LOG_CFG"):
    """
    从yaml配置文件中读取logging配置
    default_path: 配置文件路径
    default_level: 默认日志等级
    env_key: 环境变量
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r") as f:
            # 加载yaml文件，然后使用字典的格式加载配置
            config = yaml.load(f)
            print(config)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
    
    logging.info("set log yaml info message")
    logging.warning("set log yaml warning message")
    logging.critical("set log yaml critical message")


def set_log_with_json(default_path="./logging.json", default_level=logging.DEBUG, env_key="LOG_CFG"):
    """
    从json配置文件中读取logging配置
    default_path: 配置文件路径
    default_level: 默认日志等级
    env_key: 环境变量
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, "r") as f:
            config = json.load(f)
            print(config)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
    
    logging.info("set log json info message")
    logging.warning("set log json warning message")
    logging.critical("set log json critical message")


if __name__ == "__main__":
    # basic_demo()
    # set_format_demo()
    # handler_demo()
    # set_log_with_yaml()
    set_log_with_json()
