#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
pyecharts模块实现数据可视化

- github地址： https://github.com/pyecharts/pyecharts/
"""

from pyecharts.charts import Bar
from pyecharts import options as opts


def bar_demo():
    # V1 版本开始支持链式调用
    # bar = (Bar().add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"]).
    # add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105]).
    # add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49]).
    # set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况")))
    # bar.render()

    # 不习惯链式调用的开发者依旧可以单独调用方法
    bar = Bar()
    bar.add_xaxis(["衬衫", "毛衣", "领带", "裤子", "风衣", "高跟鞋", "袜子"])
    bar.add_yaxis("商家A", [114, 55, 27, 101, 125, 27, 105])
    bar.add_yaxis("商家B", [57, 134, 137, 129, 145, 60, 49])
    bar.set_global_opts(title_opts=opts.TitleOpts(title="某商场销售情况"))
    bar.render()


if __name__ == "__main__":
    bar_demo()
