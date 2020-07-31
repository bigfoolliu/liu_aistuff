# gcc编译器

<!-- vim-markdown-toc Marked -->

* [1.gcc介绍](#1.gcc介绍)
* [2.gcc命令](#2.gcc命令)

<!-- vim-markdown-toc -->

## 1.gcc介绍

- [gcc基础知识](https://www.cnblogs.com/roverliang/p/11493452.html)

gcc命令下各选项的含义:
 
- -E：仅作预处理，不进行编译、汇编和链接
- -S：仅编译到汇编语言，不进行汇编和链接
- -c：编译、汇编到目标代码（也就是计算机可识别的二进制）
- -o：执行命令后文件的命名
- -g：生成调试信息
- -w：不生成任何警告
- -Wall：生成所有的警告

## 2.gcc命令

```shell
# 将hello.c预处理输出hello.i文件
gcc -E hello.c -o hello.i

# 将预处理输出文件hello.i汇编成hello.s文件
gcc -S hello.i -o hello.s

# 将汇编输出文件hello.s编译输出hello.o文件
gcc -c hello.s -o hello.o


# 将编译输出文件hello.o链接成最终可执行文件hello
gcc hello.o -o hello


# 直接输入下面代码一步到位
gcc hello.c -o hello


# 当有多个文件需一起编译时，可输入
gcc *.c -o hello

```

