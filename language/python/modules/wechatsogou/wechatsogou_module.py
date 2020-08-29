#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
微信公众号爬虫接口(有问题)
"""


import wechatsogou


def basic_demo():
    wechats = wechatsogou.WechatSogouAPI()
    name = "编程派"
    wechat_infos = wechats.search_gzh(name)
    print(list(wechat_infos))


if __name__ == "__main__":
    basic_demo()
