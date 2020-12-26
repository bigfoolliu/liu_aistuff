#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
class super函数使用


super是为了解决多重继承时候父类的查找问题
调用基类的同一方法
"""


class MyList(list):

    def __new__(cls, *args, **kwargs):
        print('__new__ in list1 called')
        super().__new__(cls, *args, **kwargs)
    
    def __init__(self, *args, **kwargs):
        list.__init__(self, *args, **kwargs)  # 方法一：直接调用

    def say(self, word):
        print(f'hey, list1 say {word}')


class MyList2(MyList):

    def __new__(cls, *args, **kwargs):
        print('__new__ in list2 called')
        return super().__new__(cls, *args, **kwargs)  # __new__等类方法的super调用
    
    def __init__(self, *args, **kwargs):
        print('__init__ called')
        super(MyList2, self).__init__(*args, **kwargs)  # 方法二：使用super调用
    
    def say(self, word):
        super(MyList2, self).say(word)
        print(f'hey, list2 say {word}')


if __name__ == "__main__":
    # my_list = MyList()
    # print(my_list)

    my_list2 = MyList2()
    print(my_list2)


    my_list21 = MyList2()
    print(my_list21)

    my_list2.say('yoo')
