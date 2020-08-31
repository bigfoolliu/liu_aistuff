#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python yield的使用

send方法用于与生成器的交互

- 运行至yield函数返回一个值并暂停执行，相当于f.send(None)
- next(f)也等价于f.send(None)

f.send()有三个步骤（作用）：
1. 将send中的数值赋给yield的结果 ret = yield i中的ret
2. 重新启动生长器往下走
3. 再次执行next(f),相当于函数又返回了一次值

将生成器重置,可以通过重新定义的方式:
a = Generator()
b = Generator()
"""


def generator_basic(n=3):
    """自定义生成器"""
    # yield  # 类似于return None
    for i in range(n):
        yield i  # 类似于return i
        print("haha")
        print("haha2")
        yield n
    yield "over"


def yield_demo1():
    """yield基本使用"""
    a = generator_basic()
    try:
        for m in range(100):  # 为了让迭代结束
            print(next(a))
    except StopIteration:
        print("iter is over")


def generator_send():
    """用send与生成器交互的示例"""
    for i in range(10):
        ret = yield i
        if ret == "break":  # 根据接收到的交互进行不同的操作
            print("break, over")
            break
    print("generator over")


def yield_demo2():
    """yield使用2之send方法"""
    a = generator_send()
    # a.send(111)
    print(next(a))
    a.send(111)  # 将111赋值给了ret
    print(a.send(111))  # 将111赋值给了ret
    print(next(a))
    print(next(a))
    print(next(a))
    a.send("break")
    # try:
    #     a.send("break")
    #     # print(next(a))
    #     # print(next(a))
    # except StopIteration:
    #     print("iteration stopped.")


if __name__ == "__main__":
    yield_demo1()
    # yield_demo2()
