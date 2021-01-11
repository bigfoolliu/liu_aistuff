#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""

python3.5开始，PEP484为python引入了类型注解(type hints)


typing模块：

1. 类型检查，防止运行时出现参数和返回值类型不符合。
2. 作为开发文档附加说明，方便使用者调用时传入和返回参数类型。
3. 该模块加入后并不会影响程序的运行，不会报正式的错误，只有提醒pycharm目前支持typing检查，参数类型错误会黄色提示。


基本类型：

int，long，float：整型，长整形，浮点型；
bool，str：布尔型，字符串类型；
List，Tuple，Dict，Set：列表，元组，字典，集合；
Iterable，Iterator：可迭代类型，迭代器类型；
Generator：生成器类型；
Any：它可以代表所有类型，所有的无参数类型注解都默认为Any 类型；
NoReturn，None：无返回值注解。
Sequence：是 collections.abc.Sequence 的泛型，不需要严格区分 list或tuple 类型时使用。

"""


from typing import List, Any, Union
from typing import NoReturn


def func(a: int=0, b: str) -> List[int or str]:
    """类型注解的基本示例"""
    l1 = []
    l1.append(a)
    l1.append(b)
    return l1


def no_return_demo() -> NoReturn:
    """没有返回值的示例"""
    print('no return demo')


# 创建一个自己类型
Vector = List[float]


def senior_demo() -> Vector:
    return [1.0, 2.0]


if __name__ == "__main__":
    print(func(1, 'a'))
    no_return_demo()
    senior_demo()
