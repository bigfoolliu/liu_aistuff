# shell基本知识

<!-- vim-markdown-toc Marked -->

* [1.设置shell环境](#1.设置shell环境)
* [2.shell语法](#2.shell语法)
        - [2.1if使用](#2.1if使用)
        - [2.2命令行变量传递](#2.2命令行变量传递)
* [3.shell使用范例](#3.shell使用范例)
        - [3.1shell中调用另一个shell(exec, fork, source)](#3.1shell中调用另一个shell(exec,-fork,-source))
        - [3.2shell相关命令](#3.2shell相关命令)
        - [3.3进程内存监控程序](#3.3进程内存监控程序)
* [4.shell编程最佳实践](#4.shell编程最佳实践)
        - [4.1开头有蛇棒](#4.1开头有蛇棒)
        - [4.2代码有注释](#4.2代码有注释)
        - [4.3参数要规范](#4.3参数要规范)
        - [4.4缩进问题](#4.4缩进问题)
        - [4.5单行太长要分行](#4.5单行太长要分行)
        - [4.6shell中的main函数](#4.6shell中的main函数)
        - [4.7考虑作用域](#4.7考虑作用域)
        - [4.8函数返回值](#4.8函数返回值)
        - [4.9查找路径](#4.9查找路径)
        - [4.10使用新写法](#4.10使用新写法)
* [5.常用命令](#5.常用命令)

<!-- vim-markdown-toc -->

## 1.设置shell环境

- [设置bash环境](http://billie66.github.io/TLCL/book/chap12.html)
- [shell编程范例](https://tinylab.gitbooks.io/shellbook/)
- [shell脚本静态检查工具-shellcheck](https://github.com/koalaman/shellcheck)

## 2.shell语法

### 2.1if使用

比如： `if [ $a -eq $b ]`

- -eq：等于
- -ne：不等于
- -gt：大于 （greater）
- -lt：小于  （less）
- -ge：大于等于
- -le：小于等于

**语句中：**

- if [ -n str1 ]：当串的长度大于0时为真(串非空)
- if [ -z str1 ]：当串的长度为0时为真(空串)
- `v1=$(command)`: 将命令执行的结果赋给v1

**if-else语句中：**

if [ -f file ]

1. -d file      True if the file is a directory
2. -e file      True if the file exists (note that this is not particularly portable, thus -f is generally used)
3. -f file      True if the provided string is a file
4. -g file      True if the group id is set on a file
5. -L file      True if file is a symbolic link.
6. -r file      True if the file is readable
7. -s file      True if the file has a non-zero size
8. -u           True if the user id is set on a file
9. -w           True if the file is writable
10. -x          True if the file is an executable
11. -z string   True if string is empty.
12. -n string   True if string is not empty.

```sh
$#  传递到脚本的参数个数
$*  以一个单字符串显示所有向脚本传递的参数
$$  脚本运行的当前进程ID号
$!  后台运行的最后一个进程的ID号
$@  与$*相同，但是使用时加引号，并在引号中返回每个参数。
$-  显示Shell使用的当前选项，与set命令功能相同。
$?  显示最后命令的退出状态。0表示没有错误，其他任何值表明有错误。
```

### 2.2命令行变量传递

```sh
# 脚本文件名
file_name=$0

# 命令行第一个参数,一次类推
param1=$1

$# 表示传递到脚本的参数个数
$* 表示以一个单字符串显示所有向脚本传递的参数
$$ 表示脚本运行的当前进程ID号
$! 表示后台运行的最后一个进程的ID号
$@ 与$*相同，依次返回每个参数
$- 表示Shell使用的当前选项，与set命令功能相同
$? 表示最后命令的退出状态。0表示没有错误，其他任何值表明有错误
```

## 3.shell使用范例

### 3.1shell中调用另一个shell(exec, fork, source)

- fork  ( /directory/script.sh):
  fork是最普通的, 就是直接在脚本里面用/directory/script.sh来调用script.sh这个脚本.运行的时候开一个sub-shell执行调用的脚本，sub-shell执行的时候, parent-shell还在。sub-shell执行完毕后返回parent-shell. sub-shell从parent-shell继承环境变量.但是sub-shell中的环境变量不会带回parent-shell

- exec (exec /directory/script.sh)
  exec与fork不同，不需要新开一个sub-shell来执行被调用的脚本.  被调用的脚本与父脚本在同一个shell内执行。但是使用exec调用一个新脚本以后, 父脚本中exec行之后的内容就不会再执行了。这是exec和source的区别.

- source (source /directory/script.sh 也可以用点命令，即 . /directory/script.sh)
  与fork的区别是不新开一个sub-shell来执行被调用的脚本，而是在同一个shell中执行. 所以被调用的脚本中声明的变量和环境变量, 都可以在主脚本中得到和使用.

### 3.2shell相关命令

```sh
# 在其之后的代码一旦出现了返回值为非零，则整个脚本立即退出
set -e

# 在其之后的代码中出现了返回值非零，脚本不退出，继续执行后面的代码
set +e

# 在当前目录下的所有文件中查找包含`linux`字符串的文件
egrep linux *

# 将当前脚本中的变量传入到指定文件中
envsubst < setup.py

# pushd和popd操作一个目录栈，从而可以快速的切换目录
pushd  # 在栈顶(当前目录)和第二个目录交换并切换当前目录、
pushd +n  # 切换到第n个目录(从0计数)
pushd /app  # 将/app放入目录栈
popd  # 将栈顶的目录删除
popd +n  # 将第n个目录删除
dirs  # 显示目录栈中的所有目录，每次pushd执行完成之后会默认执行一次
```

### 3.3进程内存监控程序

```sh
#!/bin/bash

gst_memo_log="/gst_memo_log.txt"
process=gst-launch
process_pid=$(ps -ef | grep $process | grep -v 'grep' | awk '{print $2}')


while [ "$process_pid" != "" ]
do
    cur_time=`date +%Y-%m-%d,%H:%M:%S`
    memo_use=$(cat /proc/$process_pid/statm | awk '{print $2}')
    info="$cur_time ---  $process_pid --- $memo_use"

    echo $info  >> "$gst_memo_log"

    sleep 10

    process_pid=$(ps -ef | grep $process | grep -v 'grep' | awk '{print $2}')
done
```

## 4.shell编程最佳实践

### 4.1开头有蛇棒

```sh
# 查看本机支持的shell
cat /etc/shells

# 可以在shell脚本中指定：如
/bin/sh
/bin/dash
```

### 4.2代码有注释

一般包括下面几个部分：

- shebang
- 脚本的参数
- 脚本的用途
- 脚本的注意事项
- 脚本的写作时间，作者，版权等
- 各个函数前的说明注释
- 一些较复杂的单行命令注释

### 4.3参数要规范

```sh
# 判断参数的个数
if [[ $# != 2 ]];then
    echo "Parameter incorrect."
    exit 1
fi
```

### 4.4缩进问题

缩进方法主要有”soft tab”和”hard tab”两种：

- 所谓soft tab就是使用n个空格进行缩进(n通常是2或4)
- 所谓hard tab当然就是指真实的\t字符
- 对于if和for语句之类的，我们最好不要把then，do这些关键字单独写一行

### 4.5单行太长要分行

```sh
# 使用\来分行，且\前面加空格
./configure \
–prefix=/usr \
–sbin-path=/usr/sbin/nginx \
–conf-path=/etc/nginx/nginx.conf
```

### 4.6shell中的main函数

```sh
# shell脚本中的main函数
#!/usr/bin/env bash

func1(){
    #do sth
}
main(){
    func1
}
main "$@"
```

### 4.7考虑作用域

- shell中变量的作用域默认是全局的
- 声明局部变量: `local a=99;`

### 4.8函数返回值

- 默认函数只能返回整数

```sh
# 函数返回字符串的折中方式
func(){
    echo "2333"
}
res=$(func)
echo "This is from $res."
```

### 4.9查找路径

```sh
# 先进入当前脚本的路径，然后根据该路径获取其他路径
script_dir=$(cd $(dirname $0) && pwd)
script_dir=$(dirname $(readlink -f $0 ))
```

### 4.10使用新写法

- 尽量使用func(){}来定义函数，而不是func{}
- 尽量使用[[]]来代替[]
- 尽量使用$()将命令的结果赋给变量，而不是反引号
- 在复杂的场景下尽量使用printf代替echo进行回显

## 5.常用命令

```sh
# 查看当前使用的shell
echo $SHELL


```

