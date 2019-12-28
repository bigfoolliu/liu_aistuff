#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python 字符串操作

https://www.runoob.com/python/python-strings.html
"""


def basic_demo():
    """
    基本操作
    """
    print("hello" + "python")  # 字符串拼接    
    print("a" * 5)  # 字符串操作
    print("he" in "hello")  # 逻辑操作
    
    print(r"\n")  # 原始字符串
    
    # 三引号可以将复杂的字符串进行复制
    print("""this is me,
that is you""")

    # 定义一个unicode字符串
    n = u"python"
    face = chr(0x1F600)  # 表情
    print(n, type(n))
    print(face)


def index_demo():
    """
    字符串索引操作示例：https://www.runoob.com/w3cnote/python-string-index.html
    1. 索引：s[0]
    2. 切片：s[起始索引:结束索引:步长]，通常上边界不包括在提取字符串内
        2.1 起始索引为0，可以省略
        2.2 s最后一个索引可以取-1
        2.3 结束索引省略，默认取到最后
        2.4 反向取值，必须加步长
        2.5 步长必须与索引的方向一致
    """
    s = "hello,python"
    print(s[-1])  # 最后一个元素
    print(s[-1:1:-1])  # 步长为-1，从最后一个元素到下标为1的元素(不包含)


def operate_demo():
    """
    字符串操作函数示例
    """
    s = " abcada asd"
    print(s.capitalize())  # 首字母大写

    new_s = s.center(10)  # 原字符串居中并使用空格填充至指定长度的新字符串
    print(new_s, len(new_s))

    print(s.count("a", 2, 5))  # 返回指定字符出现的次数并可以指定统计间
    print(s.expandtabs(tabsize=4))  # 将字符串中的tab符号转换为空格，默认tabsize为8
    print(s.find("b", 1, 5))  # 检测obj是否在字符串中，在则返回索引，否返回-1，且可以指定搜索区间

    print(s.join(["1", "2", "3"]))  # 将字符串以指定分隔符将所有字符串合并为一个新的字符串

    print(s.strip())  # 去除字符串左右空格
    print(s.lstrip())  # 去除字符串左边的空格
    print(s.rstrip())  # 去除字符串右边的空格

    print(s.ljust(50, "0"))  # 将原字符串左对齐，并使用指定字符来填充至指定长度，如果指定长度小于原字符串长度则返回原字符串
    print(s.rjust(50, "0"))  # 将原字符串右对齐，并使用指定字符来填充至指定长度，如果指定长度小于原字符串长度则返回原字符串

    print(s.lower())  # 将字符串中的所有字母小写

    print(s.split("a"))  # 将字符串以指定字符分割为列表
    print(s.swapcase())  # 将字符串中的大小写翻转

    print(s.title())  # 返回标题化的字符串，即所有单词首字母大写

    s = " abcada \n asd"
    print(s.splitlines(keepends=True))  # 按照行('\r', '\r\n', \n')分隔，返回包含各行作为元素的列表，如果keepends为 False，不包含换行符
    print(s.splitlines(keepends=False))



def is_demo():
    """
    is 的示例
    """
    s = "123a"
    print("is num:", s.isalnum())  # 判断是否至少有一个字符并且所有字符都是字母或者数字
    print("is alpha:", s.isalpha())  # 判断是否至少有一个字符并且所有字符都是字母
    print("is decimal:", s.isdecimal())  # 判断是否只包含十进制数字
    print("is digit:", s.isdigit())  # 判断是否只包含数字
    print("is lower:", s.islower())  # 判断是否至少包含一个区分大小写的字符，并且所有区分大小写的都是小写的
    print("is numeric:", s.isnumeric())  # 判断是否只包含数字字符
    print("is space:", s.isspace())  # 判断是否只包含空格
    print("is title:", s.istitle())  # 判断是否是标题化的
    print("is upper:", s.isupper())  # 判断是否至少包含一个区分大小写的字符，并且所有区分大小写的都是大写的

    print(s.endswith(" "))  # 判断字符串是否以obj结尾
    print(s.startswith("1"))  # 判断字符串是否以obj开头


if __name__ == "__main__":
    # basic_demo()
    # index_demo()
    operate_demo()
    # is_demo()
