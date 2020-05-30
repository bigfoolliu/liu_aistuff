#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""查找和替换字符串"""

import re

s = "this is china, and i love it"
target = "loe"

# 查找
ret = re.findall(target, s)
print(s, ret)

# 替换
ret = re.sub("i", "we", s)
print(s, ret)

print(s.replace("china", "world"))
