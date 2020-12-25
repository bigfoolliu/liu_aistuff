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

### 1.2make命令

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

```sh
# 将文件输出重定向到指定文件
hello > text.txt
```

## 3.Clion和cMake

- [官网介绍](https://www.jetbrains.com/help/clion/clion-quick-start-guide.html)
- cmake使用CMakeLists文件来构建项目，类似makefile

CMakeLists文件编写:

TODO:
