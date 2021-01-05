#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
保存知乎“发现”页面“热门话题”部分，将问题和答案保存为文本形式
"""

import requests
from bs4 import BeautifulSoup
from pyquery import PyQuery as pq

url = "https://www.zhihu.com/explore"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
}

html = requests.get(url, headers=headers).text

data_offset = int(input('data_offset:'))

# 使用PyQuery库得到结果
doc = pq(html)  # 得到PyQuery类

items = doc('.explore-tab .feed-item').items()

for item in items:
    question = item.find('h2').text()
    author = item.find('.author-link-line').text()

    answer = pq(item.find('.content').html()).text()

    file = open('txt_saving.txt', 'a', encoding='utf-8')
    file.write('\n'.join([question, author, answer]))
    file.write('\n' + '=' * 50 + '\n')
    file.close()
