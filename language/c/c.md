# c语言

<!-- vim-markdown-toc Marked -->

* [1.基础知识](#1.基础知识)
* [2.c语言基础](#2.c语言基础)
* [3.Clion和cMake](#3.clion和cmake)

<!-- vim-markdown-toc -->

## 1.基础知识

### 1.1gcc编译器

- [gcc基础知识](https://www.cnblogs.com/roverliang/p/11493452.html)

流行的 C++ 编译器有以下这些：

1. Linux 系统下的 `GCC`；
2. Windows 系统下的 `MinGW-w64（GCC 的 Windows 版本）`；
3. Windows 系统下的`Microsoft C++ complier`（微软 Visual Studio 带的）；
4. macOS 里面的 `Clang`

```sh
# 将main.c文件编译为可执行文件
gcc main.c -o main

# 查看可执行文件信息
file main

clang --version
```

### 1.x make命令

```sh
# 创建hello.c
# 同一目录下执行，make hello，即创建名为hello的文件
# 1.查看当前目录下文件是否存在
# 2.查找当前目录下是否有文件以hello开头
# 3.存在hello.c, 执行运行命令cc hello.c -o hello来构建它

make hello

# 添加-Wall选项。告诉cc编译器要报告所有的警告
make -Wall hello
```

## 2.c语言基础

### 2.1c语言概述

使用c语言的7个步骤：

1. 定义程序目标
2. 设计程序
3. 编写代码
4. 编译
   1. 编译器将源代码编译为中间代码
   2. 链接器
5. 运行程序
6. 测试和调试程序
7. 维护和修改程序

### 2.2格式化字符

- `％d`整型输出，％ld长整型输出
- `％o`以八进制数形式输出整数
- `％x`以十六进制数形式输出整数
- `％u`以十进制数输出unsigned型数据(无符号数)
- `％c`用来输出一个字符
- `％s`用来输出一个字符串
- `％f`用来输出实数，以小数形式输出，（备注：浮点数是不能定义如的精度的，所以“%6.2f”这种写法是“错误的”！！！）
- `％e`以指数形式输出实数
- `％g`根据大小自动选f格式或e格式，且不输出无意义的零

### 2.3转义字符

- `\a`响铃(BEL)
- `\b`退格(BS) ，将当前位置移到前一列
- `\f`换页(FF)，将当前位置移到下页开头
- `\n`换行(LF) ，将当前位置移到下一行开头
- `\r`回车(CR) ，将当前位置移到本行开头
- `\t`水平制表(HT)
- `\v`垂直制表(VT)
- `\'`单引号
- `\"`双引号
- `\\`反斜杠

## 3.Clion和cMake

- [官网介绍](https://www.jetbrains.com/help/clion/clion-quick-start-guide.html)
- cmake使用CMakeLists文件来构建项目，类似makefile

CMakeLists文件编写:

TODO:
