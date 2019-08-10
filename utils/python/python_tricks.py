#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#author: bigfoolliu

# 1.字符串反转
s = "hello, world"
s = s[::-1]

# 2.zip
v = [(1, 2, 3), (4, 5, 6)]
zip(*v)

# 3.取值
p = [4, 5, 6]
x, y, z = p

# 4.变量调换
a, b = 11, 22
b, a = a, b

# 5.打印某个月
import calendar
month = calendar.month(2019, 7)
print(month)
