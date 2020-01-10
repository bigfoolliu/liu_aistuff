# vi快捷键

<!-- TOC -->

- [vi快捷键](#vi快捷键)
    - [1.基础命令](#1基础命令)
        - [1.1替换](#11替换)
        - [1.2查找](#12查找)
        - [1.3拷贝和剪切](#13拷贝和剪切)
        - [1.4跳转](#14跳转)
        - [1.5保存和退出](#15保存和退出)
        - [1.6撤销](#16撤销)
    - [2.vimrc相关配置](#2vimrc相关配置)
    - [3.高级操作](#3高级操作)

<!-- /TOC -->

- [vim从入门到精通中文版](https://github.com/wsdjeg/vim-galore-zh_cn)

## 1.基础命令

```shell
# 通过编辑 `~/.vimrc`文件可以保存vim的配置，可以使用网上众多的配置。

x   删除光标出的字符
i   insert before the cursor
a   insert after the cursor
o   insert a new line at the current line
v   进入visual模式,可以使用j, k, l来移动光标确定选择的内容

vi `file`   open single file
vi `file1` `file2`  open multi file

:open `file`    在vi窗口中打开一个新文件
:split `file`   在新窗口中打开一个新文件

ctrl + b    快速回退一页
ctrl + f    快速前进一页
```

### 1.1替换

```shell
:%s/A/B/g  全文中将所有的A替换为B
:%s/A/B/gc  回车后会将光标移动到每一次A出现的位置并提示

:s/A/B/g  本行中将所有A替换为B
:%s/A/B  只替换从光标位置开始目标的第一次
```

### 1.2查找

```shell
/text   查找text,按n键查找下一个,按Ｎ查找前一个,shift+n到上一个
```

### 1.3拷贝和剪切

```shell
dd  剪切当前行
10d 剪切当前开始的10行
Ｄ  剪切当前字符至行尾

yy  拷贝当前行
2yy 拷贝当前后开始的2行
p   粘贴
ZZ  保存并退出

:1, 10 copy 20  将1-10行的内容复制到20行
:1, 10 move 20  将1-10行的内容剪切到20行
```

**将vim中的内容复制到系统剪切板：**

- [将vim中的内容复制到系统剪切板](https://www.cnblogs.com/callmelord/p/11579646.html)

```shell
# 基本步骤
# 1.安装插件
sudo apt-get install vim-gnome

# 2.vim进入visual模式，选中块，然后使用命令 "+y 来将内容复制到系统剪切板
```

### 1.4跳转

```shell
:`number`   跳转到指定的行

g   快速跳转至文件开头
G   快速跳转至文件末尾

w   跳到下一个单词的开头
e   跳到这个单词的末尾

%   跳到对应的括号的位置
*   跳到当前光标的下一个或者上一个相同单词的地方

0   跳到第一列
$   跳到最后一列

g_  跳到当前行的最后一个字符
^   跳到当前行的第一个字符

fa  跳到这行a字母的下一个出现的地方
t,  跳到,字符的前一个字符
```

### 1.5保存和退出

```shell
:q!  不保存退出
:wq     保存退出
:wq temp.py 以一个文件名保存并退出
:e!     放弃所有修改，从上次保存开始处再编辑
```

### 1.6撤销

```shell
u   撤销上一步操作
```

## 2.vimrc相关配置

```shell
:syntax on  基本的语法高亮
:set number 显示行号
```

## 3.高级操作

```shell
gd 跳转至函数的定义处
```
