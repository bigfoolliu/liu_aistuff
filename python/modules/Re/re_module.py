#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
re模块，正则匹配
"""

import re


def search_demo():
    """
    1. search()
    在匹配时会扫描整个字符串，然后返回第一个成功匹配的结果。也就是说，正则表达式
    可以是字符串的一部分，在匹配时，search()方法会依次扫描字符串，直到找到第一个
    符合规则的字符串，然后返回匹配内容，如果搜索完了还没有找到，就返回None
    """
    content = """
            Hello, this is tony liu,
            my phone number is 010-12345678,
            my e-mail is heyheyhey@sina.com.
            """
    search = r'\d{3}-\d{8}|\d{4}-\{7,8}'  # 电话号的正则表达式
    result = re.search(search, content)
    print(type(result.group()))
    print(result.group(0))


def match_demo():
    """
    2. match()

    传入要匹配的字符串以及正则表达式，就可以检测这个正则表达式是否匹配字符串。

    match()方法会尝试从字符串的起始位置匹配正则表达式，如果匹配，就返回匹配成功
    的结果；如果不匹配，就返回None
    """
    content = 'Hello 123 4567 World_This is a Regex Demo'
    # print(len(content))

    result = re.match(r"^Hello\s\d\d\d\s\d{4}\s\w{10}", content)

    # 使用.*号，.代表任意字符，*代表匹配前面的字符无限次
    result2 = re.match(r"Hello.*Demo$", content)

    # 非贪婪的方式获取数字.*?
    result3 = re.match(r"He.*?(\d+)\s(\d+).*$", content)

    print(result)
    print(result.group())
    print(result.span())

    print(result2.group())

    print(result3.group())
    print(result3.group(1))
    print(result3.group(2))


def findall_demo():
    """
    3. findall()

    如果想要获取匹配正则表达式的所有内容，那该怎么办呢？这时就要借助findall()方法了。
    该方法会搜索整个字符串，然后返回匹配正则表达式的所有内容。
    """
    html = """<div id="songs-list">
        <h2 class="title">经典老歌</h2>
        <p class="introduction">
            经典老歌列表
        </p>
        <ul id="list" class="list-group">
            <li data-view="2">一路上有你</li>
            <li data-view="7">
                <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
            </li>
            <li data-view="4" class="active">
                <a href="/3.mp3" singer="齐秦">往事随风</a>
            </li>
            <li data-view="6">
                <a href="/4.mp3" singer="beyond">光辉岁月</a></li>
            <li data-view="5">
                <a href="/5.mp3" singer="陈慧琳">记事本</a></li>
            <li data-view="5">
                <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
            </li>
        </ul>
    </div>
    """
    # 参数有re.S，不会对\n符进行中断，可以匹配更多的内容
    results = re.findall('<li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)

    # print(results)
    print(type(results))

    for result in results:
        # print(result)
        print(result[0], result[1], result[2])


def sub_demo():
    """
    4. sub()

    除了使用正则表达式提取信息外，有时候还需要借助它来修改文本。比如，想要把一串文本中的
    所有数字都去掉
    """
    content = '54aK54yr5oiR54ix5L2g'

    # sub()第一个参数匹配想要替换的内容，第二个参数匹配替换内容
    content = re.sub(r'\d+', '', content)

    print(content)


def complile_demo():
    """
    5. compile()

    前面所讲的方法都是用来处理字符串的方法，最后再介绍一下compile()方法，这个方法可以将
    正则字符串编译成正则表达式对象，以便在后面的匹配中复用，即重复使用正则表达式
    """
    content1 = '2018-4-6 19:18'
    content2 = '2018-4-6 19:19'
    content3 = '2018-4-6 19:20'

    pattern = re.compile(r'\d{2}:\d{2}')
    print(type(pattern))

    result1 = re.sub(pattern, '', content1)
    result2 = re.sub(pattern, '', content2)
    result3 = re.sub(pattern, '', content3)

    print(result1, result2, result3)


def constant_demo():
    """常量操作"""
    text = '你好a'
    pattern = '你好A'
    print('默认模式:', re.findall(pattern, text))
    print('忽略大小写模式:', re.findall(pattern, text, re.IGNORECASE))


if __name__ == "__main__":
    # search_demo()
    # match_demo()
    # findall_demo()
    # sub_demo()
    # complile_demo()
    constant_demo()

