#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
接口服务

规则说明:
调用单表接口需要指明支持的请求方法(GET,POST,PUT,DELETE),如果未指定，默认不注册该单表接口.
可以重新自定义的单表接口请求方式的处理逻辑
"""


from app.api.base import Service
from app.models.model import *


class ArticleAPI(Service):
    """文章单表接口,对文章所用的操作通过该接口完成"""
    # 指定对应的模型
    __model__ = Article
    # 指定能够操作的方式
    __methods__ = ["GET", "POST", "PUT", "DELETE"]
    # 定义该服务的名称
    service_name = "article"
