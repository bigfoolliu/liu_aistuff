#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python建造者模式实现
"""


from abc import ABCMeta, abstractmethod


class Builder(object):
    """接口类，定义创建对象的方法"""

    __metaclass__ = ABCMeta

    @abstractmethod
    def draw_left_arm(self):
        pass

    @abstractmethod
    def draw_right_arm(self):
        pass

    @abstractmethod
    def draw_body(self):
        pass


class Thin(Builder):
    """创造者类"""

    def draw_left_arm(self):
        print("画左手")

    def draw_right_arm(self):
        print("画右手")

    def draw_body(self):
        print("画瘦身体")


class Fat(Builder):
    """创造者类"""

    def draw_left_arm(self):
        print("画左手")

    def draw_right_arm(self):
        print("画右手")

    def draw_body(self):
        print("画胖身体")


class Director(object):
    """
    指挥员类，可以指定由哪个创造者来创造
    接收创造者对象为参数
    """

    def __init__(self, person):
        self.person = person

    def draw(self):
        self.person.draw_left_arm()
        self.person.draw_right_arm()
        self.person.draw_body()


if __name__=='__main__':
    thin = Thin()
    fat = Fat()
    director_thin = Director(thin)
    director_thin.draw()
    director_fat = Director(fat)
    director_fat.draw()
