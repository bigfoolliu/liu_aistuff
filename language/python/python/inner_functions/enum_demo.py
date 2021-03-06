#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python枚举类和普通类的不同

- python Enum枚举类的使用: https://www.cnblogs.com/skaarl/p/10279428.html

1.枚举类值不可变
2.具有防止相同标签的功能，不同标签的值可以相同
3.枚举类型是单例模式，不能实例化

使用场景：
当某个类的对象是有限且固定的，比如性别，季节等。
"""

from enum import Enum


def basic_demo():
    # 定义枚举类方式一：直接使用
    # 创建一个Month类型的枚举类
    months = Enum("Month", ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

    # 访问枚举的成员
    print(months)
    print(months.Jan)  # 引用一个常量

    # 获取该枚举对象的值和变量名
    print(months.Jan.value)
    print(months.Jan.name)

    print(months(1))
    print(months["Jan"])

    # # 枚举所有的成员
    # print(type(months))
    # for name, member in months.__members__.items():
    #     print("name: ", member.name, "value:", member.value)  # value属性是自动赋值给成员的int常量，默认从1计数
    #     print(name, member)


# 定义枚举类方式二：继承使用
class Gender(Enum):
    """自定义一个枚举类"""
    Male = 0
    Female = 1


def inhert_demo():
    male = Gender(0)
    female = Gender(1)
    print(male, type(male))
    print(female, type(female))

    for gender, value in Gender.__members__.items():
        print(f'gender: {gender}, value: {value}')


if __name__ == "__main__":
    basic_demo()
    inhert_demo()
