#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
plotly模式使用

创建图表的更好的方式


- github: https://github.com/plotly/plotly.py
- doc: https://plot.ly/python/
"""

import plotly.graph_objects as go


def basic_demo():
    fig = go.Figure(data=go.Bar(y=[4, 2, 1, 3, 5]))
    fig.show()


if __name__ == "__main__":
    basic_demo()
