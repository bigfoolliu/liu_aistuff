# c语言

<!-- vim-markdown-toc Marked -->

* [1.gcc基础](#1.gcc基础)
* [2.c语言基础](#2.c语言基础)

<!-- vim-markdown-toc -->

## 1.基础知识

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

## 2.c语言基础

```sh
# 将文件输出重定向到指定文件
hello > text.txt
```

## 3.Clion和cMake

- [官网介绍](https://www.jetbrains.com/help/clion/clion-quick-start-guide.html)
- cmake使用CMakeLists文件来构建项目，类似makefile

CMakeLists文件编写:
