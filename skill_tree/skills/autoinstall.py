#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
将该模块放入项目，可以自动导入缺失的库

使用方式(加入不确定是否安装了requests):
import autoinstall
import requests

python3 importc查找机制：
1. sys.module中
2. sys.meta_path中
3. sys.path中
"""


import sys
import os
from importlib import import_module


class AutoInstall(object):
    _loaded = set()
    
    @classmethod
    def find_sepc(cls, name, path, target=None):
        if path is None and name not in cls._loaded:
            cls._loaded.add(name)
            print("installing ", name)
            try:
                ret = os.system("pip install {}".format(name))
                if ret == 0:
                    return import_module(name)
            except Exception as e:
                print("install failed {}".format(e))
        return None


sys.meta_path.append(AutoInstall)
