#!/bin/bash
# 条件语句


name="liu"

if [ "$name" == "liu" ]
then
    echo "hello, $name"
elif [ "$name" == "tony" ]
then
    echo "hello tony"
fi


# 与或非，注意这里的true和false和0与1是刚好相反的
# 与
if true && true
then
    echo "true"
fi

# 或
if true || false
then
    echo "true"
fi


# 非
if ! false
then
    echo "false"
fi


# 如果ping通则执行后面的命令
ping -c 1 www.baidu.com && echo "ping baidu sccced"

