#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
pyecharts模块实现数据可视化
"""


from pyecharts import Bar


bar = Bar("pyecharts demo主标题", "副标题")
bar.add("服装", ["衬衫", "羊毛衫", "裤子"])
bar.render()