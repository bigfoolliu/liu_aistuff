#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
工厂文件
"""


import logging
import logging.config
import os

import yaml

from app.api import api_test
from app.utils.core import JSONEncoder
from flask import Flask


def create_app(config_name=None, config_path=None):
    """
    根据指定的配置来读取创建flask的app
    :param config_name: <str>需要读取的具体某项配置内容
    :param config_path: <str>配置文件的路径
    :return : Flask object
    """
    app = Flask(__name__)
    if not config_path:
        pwd = os.getcwd()
        config_path = os.path.join(pwd, "config/config.yaml")
    if not config_name:
        config_name = "PRODUCTION"
    conf = read_yaml(config_name, config_path)
    app.config.update(conf)

    # 日志设置
    if not os.path.exists(app.config["LOGGING_PATH"]):
        os.mkdir(app.config["LOGGING_PATH"])
    with open(app.config["LOGGING_CONFIG_PATH"], "r", encoding="utf-8") as f:
        dict_conf = yaml.safe_load(f.read())
    logging.config.dictConfig(dict_conf)

    # 响应设置
    root_path = os.path.dirname(os.getcwd())
    msg_config_path = os.path.join(pwd, "config/msg.yaml")
    with open(msg_config_path, encoding="utf-8") as f:
        msg_conf = yaml.safe_load(f.read())
    app.config.update(msg_conf)

    # 使用自定义的flask的json解析类
    app.json_encoder = JSONEncoder

    # 注册测试蓝图
    app.register_blueprint(api_test.test_bp)
    return app


def read_yaml(config_name, config_path):
    """
    读取yaml格式的配置文件
    :param config_name: <str>需要读取的具体某项配置内容
    :param config_path: <str>配置文件的路径
    :return : 具体配置项对应的值
    """
    if config_path and config_name:
        with open(config_path, "r") as f:
            conf = yaml.safe_load(f.read())
        if config_name in conf.keys():
            return conf[config_name.upper()]
        else:
            raise KeyError("未找到对应的配置信息")
    else:
        raise ValueError("请输入正确的配置名称和正确的配置文件路径")
