#!/bin/bash
# shell中循环的几种写法

# 1.for in的写法
# 1.1遍历已知的一些元素，或者使用 {1 2 3}
for i in 1 2 3
do
    echo "$i"
done


# 1.2遍历当前目录下的文件
for file in ./*
do
    echo "$file"
done


# 1.3等宽的01-10
for i in $(seq -w 10)
do
    echo "$i"
done


# 1.4遍历执行命令的结果
a=$(ls)
for i in $a
do
    echo "$i"
done
