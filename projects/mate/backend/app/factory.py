#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


from flask import Flask
from app.api.router import routers


def create_app(config_name=None, config_path=None):
    """
    根据指定的配置来读取创建flask的app
    :param config_name: <str>需要读取的具体某项配置内容
    :param config_path: <str>配置文件的路径
    :return : Flask object
    """
    app = Flask(__name__)
    for router in routers:
        print("register router:{}".format(router))
        app.register_blueprint(router)
    return app
