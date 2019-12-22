#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
用户输入的数据：使用模板字符串避免安全问题
python3.6或者更高：使用字符串插值，否则使用format做字符串格式化

1. format函数的更多使用
2. 进制转换格式
"""


def format_basic_demo():
    # 1.位置映射
    print("ip and port:{}:{}".format("192.168.0.1", 8080))

    # 2.关键字映射
    print("{server} is {1}:{0}".format(8080, "192.168.1.0", server="super cool server"))

    # 3.元素访问
    print("{0[0]} {0[1]}: this is {1[0]}".format(("hello", "tony"), ("jesus", "christ")))

    # 4.填充对齐
    # ^ > < 分别对应居中，左对齐，右对齐
    for i in range(1, 10):
        a = 1
        while a <= i:
            print("{0}*{1}={2:0>2}".format(a, i, a*i), end="\t")
            a += 1
        print()

def format_f_demo():
    """
    python 3.6之后新增的字面量
    """
    name = "fuck"
    print(f"hello {name}")


def format_template_demo():
    """
    使用模板模块
    """
    from string import Template
    a = Template("I am ${name} and I am ${age} years old")
    print(a.substitute(name="tony", age=23))


if __name__ == "__main__":
    # format_basic_demo()
    # format_f_demo()    
    # format_template_demo()
