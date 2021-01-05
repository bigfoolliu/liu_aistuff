#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
1. get()方法

对应urllib中的urlopen()方法
"""
# import requests
#
# response = requests.get('https://www.baidu.com/')
#
# print(type(response))
#
# print(response.status_code)
#
# print(type(response.text))
#
# print(response.text)
#
# print(response.cookies)


"""
2. 抓取网页
"""
import requests
import re

# 构造请求头，以浏览器的方式发起请求
headers = {
	'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

response = requests.get('https://www.zhihu.com/explore', headers=headers)

# 用正则表达式匹配问题内容
pattern = re.compile('explore-feed.*?question_link.*?>(.*?)</a>', re.S)

titles = re.findall(pattern, response.text)

print(titles)


if __name__ == "__main__":
	pass
