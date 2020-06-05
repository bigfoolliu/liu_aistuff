#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
lxml库的使用

解析html
"""

from lxml import etree


def etree_demo1():
    """
    1. etree模块
    """
    # 该文本最后一个li节点没有闭合，但是etree模块可以自动修正HTML文本
    text = """
    <div>
        <ul>
             <li class="item-0"><a href="link1.html">first item</a></li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-inactive"><a href="link3.html">third item</a></li>
             <li class="item-1"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a>
         </ul>
     </div>
     """

    html = etree.HTML(text)  # 基于文本text创建了一个HTML类，构建了一个XPath解析对象
    result = etree.tostring(html)  # 调用tostring()方法即可输出修正后的HTML代码，但是结果是bytes类型
    print(result.decode('utf-8'))

    # 从文本文件中读取
    html2 = etree.parse('./lxml_test.html', etree.HTMLParser())

    result2 = etree.tostring(html2)
    print(result2.decode('utf-8'))


def etree_demo2():
    """
    2. //选取所有节点
    """
    html = etree.parse('./lxml_test.html', etree.HTMLParser())

    result = html.xpath('//*')  # 返回的是list，包含每一个节点，*代表任意节点

    print(type(result))
    print(result, '\n\n')

    # 当只获取指点的节点时，只需指定名称
    result2 = html.xpath('//ul')
    print(result2)


def etree_demo3():
    """
    3. 通过/或者//选取子节点
    """
    html = etree.parse('./lxml_test.html', etree.HTMLParser())
    result = html.xpath('//li/a')  # 选取所有li节点下的子节点a节点
    result2 = html.xpath('//ul//a')  # 选取所有a节点下的子孙a节点

    print(type(result), '\n', result)
    print(type(result2), '\n', result2)


def etree_demo4():
    """
    4. ..查找父节点
    """
    html = etree.parse('./lxml_test.html', etree.HTMLParser())
    # 选取对应属性a节点的父节点，然后再获取其属性
    result = html.xpath('//a[@href="link3.html"]/../@class')
    print(type(result), result)


def etree_demo5():
    """
    5. 属性匹配

    使用@进行属性过滤
    """
    html = etree.parse('./lxml_test.html', etree.HTMLParser())
    result = html.xpath('//li[@class="item-1"]')
    print(result)


def etree_demo6():
    """
    6. text()方法，文本获取
    """
    html = etree.parse('./lxml_test.html', etree.HTMLParser())

    # 此处result并没有获取到任何文本，只获取到了一个换行符，这是为什么呢？因为XPath中text()前面是/，
    # 而此处/的含义是选取直接子节点，很明显li的直接子节点都是a节点，文本都是在a节点内部的，
    # 所以这里匹配到的结果就是被修正的li节点内部的换行符，因为自动修正的li节点的尾标签换行了
    result = html.xpath('//li[@class="item-0"]/text()')
    print(result)

    # 先定位至li节点下的a节点即可获取文本
    result2 = html.xpath('//li[@class="item-0"]/a/text()')
    print(result2)

    # 要想获取子孙节点内部的所有文本，可以直接用//加text()的方式，但是会夹杂换行符等特殊字符
    result3 = html.xpath('//li[@class="item-0"]//text()')
    print(result3)


def etree_demo7():
    """
    7. 用@获取属性
    """
    html = etree.parse('./lxml_test.html', etree.HTMLParser())
    result = html.xpath('//li/a/@href')
    print(result)


def etree_demo8():
    """
    8. 属性多值匹配
    contains()
    """
    html = etree.parse('./lxml_test.html', etree.HTMLParser())
    result = html.xpath('//li[contains(@class, "li")]/a/text()')

    print(result)


def etree_demo9():
    """
    9. 多属性匹配
    and连接，还有其他运算符可参照：https://cuiqingcai.com/5545.html
    """
    html = etree.parse('./lxml_test.html', etree.HTMLParser())
    result = html.xpath('//li[contains(@class, "li") and @name="item"]/a/text()')
    print(result)


def etree_demo10():
    """
    10. 按序选择

    在选择的时候某些属性可能同时匹配了多个节点，但是只想要其中的某个节点，如第二个节点或者
    最后一个节点，可以利用中括号传入索引的方式
    """
    text = """
    <div>
        <ul>
             <li class="item-0"><a href="link1.html">first item</a></li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-inactive"><a href="link3.html">third item</a></li>
             <li class="item-1"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a>
         </ul>
     </div>
    """
    html = etree.HTML(text)
    result = html.xpath('//li[1]/a/text()')
    print(result)
    result = html.xpath('//li[last()]/a/text()')
    print(result)
    result = html.xpath('//li[position()<3]/a/text()')
    print(result)
    result = html.xpath('//li[last()-2]/a/text()')
    print(result)


if __name__ == "__main__":
    # etree_demo1()
    # etree_demo2()
    # etree_demo3()
    # etree_demo4()
    # etree_demo5()
    etree_demo6()
    etree_demo7()
    etree_demo8()
    etree_demo9()
    etree_demo10()
