#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu



"""
类继承
"""


"""
1.让子类重写了父类的方法但是仍然调用父类的方法
"""

class A(object):

    def show(self):
        print("A show")


class B(A):

    def show(self):
        print("B show")

obj = B()
obj.show()  # B show

obj1 = B()
obj1.__class__ = A  # 通过class方法指定类对象
obj1.show() # A show