#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
chromee driver操作浏览器
"""


from selenium import webdriver
import time

wd = webdriver.Chrome()
wd.get("https://www.baidu.com")    # 打开百度浏览器
wd.find_element_by_id("kw").send_keys("天气")   # 定位输入框并输入搜索词
wd.find_element_by_id("su").click()   #点击[百度一下]按钮进行搜索
time.sleep(3)   #等待3秒
wd.quit()   #关闭浏览器

