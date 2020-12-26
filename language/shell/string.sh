#!/bin/bash
# 字符串的相关操作

# 1.计算字符串的长度
s="the test string"
echo "the length of s is: ${#s}"


# 2.控制字符输出的颜色
echo "\033[31;40m $s"  # 前景色为黑色，背景为红色


# 3.取字符串的部分, 下标从0开始
echo "${s:1:3}"  # 1-3
echo "${s:(-3)}"  # -3-0
