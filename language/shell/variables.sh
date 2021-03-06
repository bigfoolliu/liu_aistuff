#!/bin/bash
# 变量和特殊的变量

# 1.整数加1

i=1
((i++))  # 方法1,推荐使用,效率也比较高
echo "$i"

let i++  # 方法2,不推荐
echo "$i"

expr $i + 1  # 方法3，不推荐
echo "$i"


# 2.产看命令的类型, 分为内部的命令和外部的命令,外部命令在/usr/bin目录下
type type
type let
type expr


# 3.累加到某个值
while [ "$i" -lt 100 ]
do
    ((i++))
done
echo "$i"


# 4.求模
((a="$i" % 13))
echo "$a"


# 5.求幂
((b=5**2))
echo "$b"


# 6.产生随机数字(0-32767)
echo $((RANDOM))
echo $RANDOM


# 7.传入的特殊变量

# $#  # 表示传递到脚本的参数个数
# $*  # 表示以一个单字符串显示所有向脚本传递的参数
# $$  # 表示脚本运行的当前进程ID号
# $!  # 表示后台运行的最后一个进程的ID号
# $@  # 与$*相同，依次返回每个参数
# $-  # 表示Shell使用的当前选项，与set命令功能相同
# $?  # 表示最后命令的退出状态。0表示没有错误，其他任何值表明有错误


echo "传递进的参数个数为: $#"
echo "单字符显示所有传入的参数: $*"
echo "当前脚本运行的最后一个进程的id号为: $!"
echo "当前脚本运行的当前的进程id号为: $$"

# echo $(("所有传入的参数为："+"$@"))
echo "最后退出的状态为: $?"
