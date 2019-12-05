#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
同一存放所有的蓝图和自定义的MethoeView
"""


from app.api.api_test import test_bp
from app.api.services import ArticleAPI


router = [
    test_bp,
    ArticleAPI,
]
