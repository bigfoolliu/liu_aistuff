#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
pyquery模式示例
"""

from pyquery import PyQuery as pq


def init_demo():
    """
    1. 初始化
    """
    html = """
    <div>
        <ul>
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
    """
    doc = pq(html)  # 生成类<class 'pyquery.pyquery.PyQuery'>

    print(type(doc))
    print(doc('li'))
    print(doc('ul'))

    # 初始化的参数还可以传入网页url
    # 首先请求该url，用得到的HTML内容完成初始化
    doc = pq(url='http://cuiqingcai.com')
    print(doc('title'))

    # 等价于
    import requests
    doc = pq(requests.get('http://cuiqingcai.com').text)
    print(doc('title'))

    # 传递本地的文件名
    doc = pq(filename='pyquery_demo.html')
    print(doc('h2'))


def css_demo():
    """
    2. 基本CSS选择器
    """
    html = """
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
     </div>
    """
    doc = pq(html)
    # 先选取id为container的节点，然后选取内部class为list的内部的所有li节点
    print(doc('#container .list li'))
    print(type(doc('#container .list li')), '\n\n')  # 类型仍然为PyQuery类

    # 查找节点，用find()方法
    items = doc('.list')

    print(type(items))  # PyQuery类
    print(items, '\n\n')

    # find()方法查找的是所有子孙节点
    lis = items.find('li')

    print(type(lis))  # PyQuery类
    print(lis, '\n\n')

    # 只查找子节点，用children()方法
    lis = items.children('li')
    print(lis)
    lis = items.children('.active')
    print(lis, '\n\n')

    # 查找父节点，用parent()方法
    lis = items.parent()
    print(lis, '\n\n')

    # 查找祖父节点，用parents()方法
    # 查找兄弟节点，用siblings()方法
    li = doc('.list .item-0.active')
    print(li, '\n\n')
    print(li.siblings(), '\n\n')


def ergodic_demo():
    """
    3. 遍历
    """
    html = """
    <div id="container">
        <ul class="list">
            <li class="item-0">first item</li>
            <li class="item-1"><a href="link2.html">second item</a></li>
            <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
            <li class="item-1 active"><a href="link4.html">fourth item</a></li>
            <li class="item-0"><a href="link5.html">fifth item</a></li>
        </ul>
    </div>
    """

    # 对于单个节点可以直接打印输出，也可以直接转成字符串
    doc = pq(html)
    li = doc('.list .item-0.active')

    print(li)
    print(str(li)[0:10], '\n\n')

    # 对于多个节点，需要遍历，调用items()方法
    lis = doc('li').items()
    for li in lis:
        print(li, type(li))


def attr_demo():
    """
    4.获取信息
    包括获取属性信息，获取文本信息
    attr()方法获取属性
    """
    html = """
    <div class="wrap">
        <div id="container">
            <ul class="list">
                <li class="item-0">first item</li>
                <li class="item-1"><a href="link2.html">second item</a></li>
                <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
                <li class="item-1 active"><a href="link4.html">fourth item</a></li>
                <li class="item-0"><a href="link5.html">fifth item</a></li>
            </ul>
        </div>
    </div>
    """
    doc = pq(html)
    a = doc('.item-0.active a')

    print(a, type(a))

    # print(a.attr())，错误
    # 下面两个语句作用相同
    print(a.attr.href)
    print(a.attr('href'), '\n\n')

    # 结果包含多个节点时，调用attr()方法只会得到第一个节点属性，需要遍历
    a = doc('a')
    for item in a.items():
        print(a.attr('href'))

    print('\n\n')
    # text()获取文本，会忽略掉节点内部包含的HTML，只返回文本信息
    print(a.text())  # 多节点会返回所有节点文本，中间用空格分割开
    for item in a.items():
        print(item.text())

    print('\n\n')
    # html()方法，可获取节点内部的html文本
    for item in a.items():
        print(item.html())


def node_demo():
    """
    5.节点操作
    包括为节点添加class，移除某个节点等
    addClass()方法，添加一个类
    removeClass()方法，移除一个类
    """
    html = """
    <div class="wrap">
        <div id="container">
            <ul class="list">
                <li class="item-0">first item</li>
                <li class="item-1"><a href="link2.html">second item</a></li>
                <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
                <li class="item-1 active"><a href="link4.html">fourth item</a></li>
                <li class="item-0"><a href="link5.html">fifth item</a></li>
            </ul>
        </div>
    </div>
    """
    doc = pq(html)

    li = doc('.item-0.active')
    print(li)

    li.removeClass('active')
    print(li)

    li.addClass('active')
    print(li)


if __name__ == "__main__":
    init_demo()
    css_demo()
    ergodic_demo()
    attr_demo()
    node_demo()
