'''
coding:utf-8

'''

import os
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from urllib.parse import quote
from lxml import etree
import csv
import requests

base_url = "https://book.douban.com/"


def get_one_page(page):
    """
    获取豆瓣读书html
    """
    # 单页的书单有20项
    # 使用quote()便于url编码
    page_url = base_url + 'tag/{}?'.format(quote(tag)) + 'start={}&type=T'.format(20 * page)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
    }
    try:
        response = requests.get(page_url, headers=headers)
        response.encoding = 'utf-8'
        html = response.text
    except TimeoutException:
        print('{}页面打开失败，url为{}。'.format(page, page_url))

    parse_one_page(html)


def parse_one_page(html):
    """
    使用XPath解析html
    """
    page_html = etree.parse(html, etree.HTMLParser())
    try:
        book_name = page_html.xpath('//li[@class="subject-item"]/div[@class="info"]/h2/a/@title')
        book_pub = page_html.xpath('//li[@class="subject-item"]/div[@class="info"]/div[@class="pub"]/text()')

        book_info = {
            'book_name': book_name,
            'information': book_pub
        }
    except NoSuchElementException:
        print('节点不存在！')

    save_file(book_info)


def save_file(book_lists):
    """
    存储书单
    """
    with open('book_list.csv', 'w', encoding='utf-8') as book_list_csv:
        writer = csv.writer(book_list_csv, delimiter=' ')
        writer.writerow(book_lists)


def main(tag):
    """
    主函数
    ：param tag：豆瓣图书标签，str类型
    """
    pages = int(input('输入页数：'))
    for page in range(0, pages):
        get_one_page(page)


if __name__ == "__main__":
    """
    python模拟程序接口
    模块是被直接运行的则代码块被运行，若模块是被导入的则代码块不被运行
    """
    tag = '小说'
    main(tag)
