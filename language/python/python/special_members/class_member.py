#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


class A(object):
    """
    this is a brief description of class A
    """

    def __init__(self):  # 构造方法，类创建对象时候自动触发
        self._dict = {}

    def __del__(self):  # 析构方法，当对象在内存中被释放时自动调用
        print('i am deleted')

    def __call__(self):  # 对象后面加括号，触发执行
        print('i am called')

    def __str__(self):  # 打印对象时候print(xx)时候触发
        return 'a, hello'

    def __getitem__(self, key):  # 用于字典操作，获取数据
        if self._dict.get(key):
            return self._dict[key]
        return 'not found key'

    def __setitem__(self, key, value):  # 用于字典操作，设置数据
        self._dict[key] = value
        print(f'set key {key} to {value}')

    def __delitem__(self, key):  # 用于字典操作，删除数据时触发
        if key in self._dict:
            del self._dict[key]
            print(f'key {key} deleted')
        else:
            print(f'key {key} not found')



class B(object):

    def __init__(self):
        self._list = []

    def __setslice__(self, start, end, sequence):  # python2使用
        self._list[start:end] = sequence

    def __getslice__(self, start, end):  # python2使用，用于列表操作，获取分片
        print(f'get from {start} to {end}')
        return self._list[start:end]

    def __delslice__(self, start, end):
        del self._list[start:end]


class C(object):

    def __init__(self):
        self._list = [1, 2, 3]

    def __iter__(self):  # 用于迭代器，for循环的实质就是调用内部的__iter__方法
        return iter(self._list)


def func():
    print('func run')


# 类本身是type类的构造方法创建
# 此为另外一种创建类的方式
# 三个参数分别为类名，当前类的基类，类的成员
d = type('D', (object,), {'func': func})
print(type(d))  # 'type'


class E(list):

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        return super().__init__(self, *args, **kwargs)



if __name__ == "__main__":
    print(A.__doc__)  # 查看类的描述信息

    a = A()
    print(a.__module__)  # 查看当前操作的对象在哪个模块
    print(a.__class__)  # 查看当前对象的类是什么

    a()  # __call__调用

    # print(a.__dict__)  # 类或对象的所有成员
    print(A.__dict__)

    print(a)  # __str__触发

    a['name'] = 'tony'  # __setitem__触发

    print(a['name'])  # __getitem__触发

    del a['age']
    del a['name']


    # b = B()
    # b[0:4] = [1, 2, 3, 4]
    # print(a[0:2])  # 触发__getslice__

    c = C()
    for i in c:
        print(i)

    
    e = E()
    print(type, e)
    print(e)
    a = []