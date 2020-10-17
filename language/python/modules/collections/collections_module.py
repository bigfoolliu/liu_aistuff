#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
collections模块示例
包含了一些特殊的容器，针对python内置容器list, dict等提供了新的替代选择

- Counter: 字典的子类，提供了可哈希对象的计数功能，主要对访问对象的频率进行计数
- defaultdict: 字典的子类，提供了一个工厂函数，为字典查询提供了默认值
- OrderedDict: 字典的子类，保留了字典key被添加时候的顺序
- namedtuple: 创建命名元组子类的工厂函数,类似元组，但是元素的访问更加方便，不必通过索引值，而是类型字典访问
- deque: 双端队列，类似list，实现了在两端快速添加(append)和弹出(pop)
- ChainMap: 类似dict，将多个映射集合到一个视图里面，是管理嵌套上下文和覆盖的有用工具。
"""


from collections import (ChainMap, Counter, OrderedDict, defaultdict, deque,
                         namedtuple)


def counter_basic_demo():
    """
    Counter基本示例
    Counter可以传字符串，元组，列表，字典
    """
    string = "hello, hello, this is u, that is me"

    # 直接统计字符出现的次数，以及直接获取某个字符出现的次数
    a = Counter(string)
    print(a, a["l"])

    # 统计单词的个数,以及直接获取某个单词出项的次数
    b = Counter(string.split())
    print(b, b["hello"])

    # 将Counter对象转换为dict
    print("dict: ", dict(b))

    # elements()返回迭代器，每个元素重复计数的次数，用来获取所有元素
    print("elements: ", list(b.elements()))

    # 获取词频最高的n个元素，默认为0，即返回所有元素
    print("most common: ", b.most_common(1))


def counter_add_demo():
    """
    Counter相加示例
    将相同字符或者单次的个数相加
    """
    a = Counter("hello u".split())
    b = Counter("hello me too".split())
    print(a, b)

    # +和update效果相同
    print(a+b)
    print(a.update(b), a)

    # 减去次数
    print(b-a)

    # 清空
    print(a.clear(), a)


def defaultdict_basic_demo():
    """
    defaultdict示例
    为字典没有的key提供一个默认的值，而这个默认值可以随意指定类型，而一般的字典没有的key直接引用会报异常
    """
    # 不使用默认工厂，报错
    d = defaultdict()
    # print(d, d["a"])

    # 使用str作为默认工厂
    d = defaultdict(str)
    print(d, d["a"])

    # 使用int作为默认工厂
    fruit = defaultdict(int)
    print(fruit, fruit["apple"])
    fruit["banana"] += 5
    print(fruit, fruit["banana"])

    # 使用list作为默认工厂
    d = defaultdict(list)
    print(d, d["ages"])


def ordered_dict_demo():
    """
    OrderedDict示例
    """
    d = OrderedDict({"k1": "v1", "k2": "v2", "k3": "v3"})
    print(d)

    # 添加或者修改key的值都不会改变原有顺序
    d["k4"] = "v4"
    print(d)
    d.update(k1="v5")
    print(d)


def namedtuple_demo():
    """
    namedtuple示例
    """
    # 几种不同的创建方式
    person = namedtuple("Person", ["name", "age", "height"])
    person = namedtuple("Person", "name, age, height")
    person = namedtuple("Person", "name age height")
    print(person)

    # 实例化
    tony = person("tony", 10, 160)
    print(tony)
    print(tony.name, tony.age, tony.height)


def deque_demo():
    """
    deque示例

    - 一个新的双向队列对象
    - 从左到右初始化(用方法 append()) ，从 iterable （迭代对象) 数据创建。如果 iterable 没有指定，新队列为空。
      - 支持线程安全，对于从两端添加(append)或者弹出(pop)，复杂度O(1)
    - 如果 maxlen 没有指定或者是 None ，deques 可以增长到任意长度。否则，deque就限定到指定最大长度。一旦限定长度的deque满了，当新项加入时，同样数量的项就从另一端弹出。

    append(x)：添加x到右端
    appendleft(x)：添加x到左端
    clear()：清楚所有元素，长度变为0
    copy()：创建一份浅拷贝
    count(x)：计算队列中个数等于x的元素
    extend(iterable)：在队列右侧添加iterable中的元素
    extendleft(iterable)：在队列左侧添加iterable中的元素，注：在左侧添加时，iterable参数的顺序将会反过来添加
    index(x[,start[,stop]])：返回第 x 个元素（从 start 开始计算，在 stop 之前）。返回第一个匹配，如果没找到的话，升起 ValueError 。
    insert(i,x)：在位置 i 插入 x 。注：如果插入会导致一个限长deque超出长度 maxlen 的话，就升起一个 IndexError 。
    pop()：移除最右侧的元素
    popleft()：移除最左侧的元素
    remove(value)：移去找到的第一个 value。没有抛出ValueError
    reverse()：将deque逆序排列。返回 None 。
    maxlen：队列的最大长度，没有限定则为None。
    """
    d = deque(maxlen=3)
    print(d)

    # 将元素添加到右端
    d.append(1)
    d.append(2)
    d.append(3)
    d.append(4)
    print(d)

    # 将元素添加到左端
    d.appendleft(5)
    print(d)

    # 创建一份浅拷贝
    d_copy = d.copy()
    print(d_copy)

    # 清除所有元素
    d.clear()
    print(d)


def chainmap_demo():
    """
    ChainMap示例
    """
    d1 = {"name": "tony", "age": 10}
    d2 = {"destination": "china", "distance": 200}

    combined_d = ChainMap(d1, d2)
    print(combined_d)

    reversed_combined_d = ChainMap(d2, d1)
    print(reversed_combined_d)

    for k, v in combined_d.items():
        print(k, v)


if __name__ == "__main__":
    # counter_basic_demo()
    # counter_add_demo()

    # defaultdict_basic_demo()

    # ordered_dict_demo()

    namedtuple_demo()

    # deque_demo()

    # chainmap_demo()
