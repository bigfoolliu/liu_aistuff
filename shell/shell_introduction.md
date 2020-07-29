# shell基本知识

<!-- vim-markdown-toc Marked -->

* [1.shell if中的符号](#1.shell-if中的符号)
        - [语句中](#语句中)
        - [if-else语句中](#if-else语句中)
        - [shell中调用另一个shell(exec, fork, source)](#shell中调用另一个shell(exec,-fork,-source))
        - [shell相关命令](#shell相关命令)
        - [设置shell环境](#设置shell环境)
        - [进程内存监控程序](#进程内存监控程序)

<!-- vim-markdown-toc -->

- [shell编程范例](https://tinylab.gitbooks.io/shellbook/)

## 1.shell if中的符号

比如： `if [ $a -eq $b ]`

- -eq：等于
- -ne：不等于
- -gt：大于 （greater）
- -lt：小于  （less）
- -ge：大于等于
- -le：小于等于

### 语句中

- if [ -n str1 ]：当串的长度大于0时为真(串非空)
- if [ -z str1 ]：当串的长度为0时为真(空串)
- `v1=$(command)`: 将命令执行的结果赋给v1

### if-else语句中

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

### shell中调用另一个shell(exec, fork, source)

- fork  ( /directory/script.sh):
  fork是最普通的, 就是直接在脚本里面用/directory/script.sh来调用script.sh这个脚本.运行的时候开一个sub-shell执行调用的脚本，sub-shell执行的时候, parent-shell还在。sub-shell执行完毕后返回parent-shell. sub-shell从parent-shell继承环境变量.但是sub-shell中的环境变量不会带回parent-shell

- exec (exec /directory/script.sh)
  exec与fork不同，不需要新开一个sub-shell来执行被调用的脚本.  被调用的脚本与父脚本在同一个shell内执行。但是使用exec调用一个新脚本以后, 父脚本中exec行之后的内容就不会再执行了。这是exec和source的区别.

- source (source /directory/script.sh 也可以用点命令，即 . /directory/script.sh)
  与fork的区别是不新开一个sub-shell来执行被调用的脚本，而是在同一个shell中执行. 所以被调用的脚本中声明的变量和环境变量, 都可以在主脚本中得到和使用.

### shell相关命令

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

### 设置shell环境

- [设置bash环境](http://billie66.github.io/TLCL/book/chap12.html)

### 进程内存监控程序

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
