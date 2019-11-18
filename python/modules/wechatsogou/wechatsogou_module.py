#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
微信公众号爬虫接口
"""


import wechatsogou


wechats = wechatsogou.WechatSogouAPI()
name = "编程派"
wechat_infos = wechats.search_gzh(name)

print(list(wechat_infos))
