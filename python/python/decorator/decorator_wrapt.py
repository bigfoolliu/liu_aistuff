#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
使用wrapt模块实现更扁平的装饰器

使装饰器可以同时为普通函数，类方法等同时实现装饰作用
"""

import random
import wrapt


def provide_number(min_num, max_num):
    @wrapt.decorator
    def wrapper(wrapped, instance, args, kwargs):
        """
        wrapped: 被装饰的函数或者类的方法
        instance: 
            - 如果被装饰的为普通类方法，该值为类实例
            - 如果被装饰的为classmethod类方法，该值为类
            - 如果被装饰的为类/静态方法/函数，该值为None
        args: 调用时的位置参数，注意不需要*
        kwargs: 调用时的关键字参数，注意不需要**
        """
        num = random.randint(min_num, max_num)
        args = (num, ) + args  # 该装饰器的作用是将被装饰的对象的首个参数替换为随机生成的
        return wrapped(*args, **kwargs)
    return wrapper


@provide_number(1, 100)
def fool(num):
    print("num is {}".format(num))


fool()
