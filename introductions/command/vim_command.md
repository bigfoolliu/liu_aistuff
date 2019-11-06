# vi快捷键

<!-- TOC -->

- [vi快捷键](#vi%e5%bf%ab%e6%8d%b7%e9%94%ae)
  - [1.基础命令](#1%e5%9f%ba%e7%a1%80%e5%91%bd%e4%bb%a4)
  - [2.vimrc相关配置](#2vimrc%e7%9b%b8%e5%85%b3%e9%85%8d%e7%bd%ae)
  - [3.高级操作](#3%e9%ab%98%e7%ba%a7%e6%93%8d%e4%bd%9c)

<!-- /TOC -->

- [vim从入门到精通中文版](https://github.com/wsdjeg/vim-galore-zh_cn)

## 1.基础命令

```shell
# 通过编辑 `~/.vimrc`文件可以保存vim的配置，可以使用网上众多的配置。

x   删除光标出的字符
dd  delete the whole line
i   insert before the cursor
a   insert after the cursor
o   insert a new line at the current line
v   进入visual模式,可以使用j, k, l来移动光标确定选择的内容

vi `file`   open single file
vi `file1` `file2`  open multi file

u   撤销上一步操作

dd  删除当前行
10d 删除当前开始的10行
Ｄ  删除当前字符至行尾

cc  剪切当前行
c2c 剪切当前2行
yy  拷贝当前行
2yy 拷贝当前后开始的2行
p   粘贴
ZZ  保存并退出

g   快速跳转至文件开头
G   快速跳转至文件末尾
w   跳到下一个单词的开头
e   跳到这个单词的末尾
%   跳到对应的括号的位置
`*` 跳到当前光标的下一个或者上一个相同单词的地方
0   跳到第一列
^   跳到当前行的第一个字符
$   跳到最后一列
g_  跳到这行的最后一个字符
fa  跳到这行a字母的下一个出现的地方
t,  跳到,字符的前一个字符

:`number`   跳转到指定的行
:%s/A/B/g  将所有的A替换为B

:q!  不保存退出
:wq     保存退出
:wq temp.py 以一个文件名保存并退出
:e!     放弃所有修改，从上次保存开始处再编辑

:1, 10 copy 20  将1-10行的内容复制到20行
:1, 10 move 20  将1-10行的内容剪切到20行

:open `file`    在vi窗口中打开一个新文件
:split `file`   在新窗口中打开一个新文件

ctrl + b    快速回退一页
ctrl + f    快速前进一页

10gg    快速跳转到第10行
/text   查找text,按n键查找下一个,按Ｎ查找前一个,shift+n到上一个
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
