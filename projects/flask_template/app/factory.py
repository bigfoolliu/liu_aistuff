#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
工厂文件
创建app,以及对其创建过程中的一些配置
"""


import atexit
import logging
import logging.config
import os
import platform

import yaml
from flask import Blueprint, Flask

from app.api import api_test
from app.api.router import router
from app.utils.core import JSONEncoder, db, scheduler


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

    # 日志文件目录和设置
    if not os.path.exists(app.config["LOGGING_PATH"]):
        os.mkdir(app.config["LOGGING_PATH"])
    with open(app.config["LOGGING_CONFIG_PATH"], "r", encoding="utf-8") as f:
        dict_conf = yaml.safe_load(f.read())
    logging.config.dictConfig(dict_conf)

    # 响应设置
    with open(app.config["RESPONSE_MESSAGE"], "r", encoding="utf-8") as f:
        msg_conf = yaml.safe_load(f.read())
    app.config.update(msg_conf)

    # 使用自定义的flask的json解析类
    app.json_encoder = JSONEncoder

    # 注册数据库连接
    db.app = app
    db.init_app(app)

    # 使用定时任务
    if app.config.get("SCHEDULER_OPEN"):
        scheduler_init(app)

    # 注册测试蓝图
    # app.register_blueprint(api_test.test_bp)
    register_api(app, router)
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


def scheduler_init(app):
    """
    将app传入，且保证系统多进程启动的时候定时任务只启动一次
    启动任务的时候设置文件锁，当能获取到文件锁的时候，就不再启动任务
    TODO:需要重点关注，刚开始运行时候会有BlockingIOError
    """
    if platform.system() != "Windows":
        fcntl = __import__("fcntl")
        f = open("scheduler.lock", "wb")
        try:
            fcntl.flock(f, fcntl.LOCK_EX | fcntl.LOCK_NB)
            scheduler.init_app(app)
            scheduler.start()
            app.logger.debug("scheduler start......")
        except Exception as e:
            app.logger.error("scheduler error, ", e)

        def unlock():
            fcntl.flock(f, fcntl.LOCK_UN)
            f.close()
        
        atexit.register(unlock)
    else:
        msvcrt = __import__("msvcrt")
        f = open("scheduler.lock", "wb")
        try:
            msvcrt.locking(f.fileno(), msvcrt.LK_NBLCK, 1)
            scheduler.init_app(app)
            scheduler.start()
            app.logger.debug("scheduler start......")
        except Exception as e:
            app.logger.error("scheduler error, ", e)

        def _unlock_file():
            try:
                f.seek(0)
                msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
            except:
                pass
        
        atexit.register(_unlock_file)


def register_api(app, routers):
    """注册蓝图和自定义的MethodView"""
    for router in routers:
        # 如果类型为Blueprint则直接注册
        if isinstance(router, Blueprint):
            app.register_blueprint(router)
        else:
            # 如果类型为自定义的MethodView则需要进行多重判断
            try:
                endpoint = router.__name__
                view_func = router.as_view(endpoint)
                # url默认为类名的小写
                url = "/{}/".format(router.__name__.lower())
                if "GET" in router.__methods__:
                    app.add_url_rule(url, defaults={"key": None}, view_func=view_func, methods=["GET",])
                    app.add_url_rule("{}<string:key>".format(url), view_func=view_func, methods=["GET",])
                if "POST" in router.__methods__:
                    app.add_url_rule(url, view_func=view_func, methods=["POST",])
                if "PUT" in router.__methods__:
                    app.add_url_rule("{}<string:key>".format(url), view_func=view_func, methods=["PUT",])
                if "DELETE" in router.__methods__:
                    app.add_url_rule("{}<string:key>".format(url), view_func=view_func, methods=["DELETE",])
            except Exception as e:
                print("exception: ", e)
                raise ValueError(e)
