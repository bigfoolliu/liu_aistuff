# shell介绍

<!-- vim-markdown-toc Marked -->

* [1.基础](#1.基础)
* [2.数值计算](#2.数值计算)
        * [2.1整数运算](#2.1整数运算)

<!-- vim-markdown-toc -->

## 1.基础

运行*test.sh文件*几种方式(首先该文件有可执行权限):

1. ./test.sh直接运行
2. 将脚本作为bash解释器的参数：bash ./test.sh
3. source ./test.sh
4. . ./test.sh

```shell
# 查看当前使用的shell
echo $SHELL;

# 查看各个命令的类型
type expr;
```

特点：

- 不需要编译和链接
- 出错调试麻烦，因为愈发错误和逻辑错误都在运行时出现

调试技巧：

- [shell脚本调试技巧](https://www.ibm.com/developerworks/cn/linux/l-cn-shell-debug/index.html)
- [bash的调试手段](http://tinylab.org/bash-debugging-tools/)
- 使用*echo*，输出一些变量或者信息
- 使用*set -x*在语句前面可以在命令执行之前将命令打印出来
- 使用*trap*机制，此为最佳
- 其他

## 2.数值计算

### 2.1整数运算

```shell
# 让整数加1
# 方式1
i=0;
((i++));

# 方式2
let i++;

# 方式3,注意+号之间有空格隔开
expr $i + 1;

# 方式4,$1和$2分别指代前面的$i和1
echo $i 1 | awk '{printf $1+$2}';
```
