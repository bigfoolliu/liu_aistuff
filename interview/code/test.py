#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def task():
    begin = yield
    end = yield
    yield
    for x in range(begin, end):
        yield x


t = task()
t.send(None)
t.send(3)
t.send(6)
print t.next()
print [x for x in t]

