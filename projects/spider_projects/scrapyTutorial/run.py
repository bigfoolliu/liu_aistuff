#!-*-coding:utf-8-*-
# !@Date: 2018/11/25 21:11
# !@Author: Liu Rui
# !@github: bigfoolliu


"""
使用该脚本来执行运行,而不必在命令行里输入命令
"""
from scrapy import cmdline

cmdline.execute('scrapy crawl tencent3'.split())
