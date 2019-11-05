#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
读取.ini配置文件
"""
from configparser import ConfigParser


cfg = ConfigParser()

cfg.read('config.ini')

cfg.sections()

cfg.get('installation','library')

cfg.getboolean('debug','log_errors')

cfg.getint('server','port')

cfg.getint('server','nworkers')

print(cfg.get('server','signature'))
