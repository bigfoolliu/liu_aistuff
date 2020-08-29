#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
一个用来生成各类虚假数据的库
"""


import mimesis


def fake_person():
    person = mimesis.Person()
    print(person.name())
    print(person.full_name())
    print(person.age())


if __name__ == "__main__":
    fake_person()
