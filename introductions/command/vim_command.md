# vim快捷键

<!-- vim-markdown-toc Marked -->

* [1.基础命令](#1.基础命令)
        * [1.1替换](#1.1替换)
        * [1.2查找](#1.2查找)
        * [1.3拷贝和剪切](#1.3拷贝和剪切)
        * [1.4跳转](#1.4跳转)
        * [1.5保存和退出](#1.5保存和退出)
        * [1.6撤销与反撤销](#1.6撤销与反撤销)
        * [1.7补全](#1.7补全)
        * [1.8其他](#1.8其他)
* [2.vimrc相关配置](#2.vimrc相关配置)
* [3.高级操作](#3.高级操作)
        * [3.1跳转到函数定义处](#3.1跳转到函数定义处)
        * [3.2vim查看二进制文件](#3.2vim查看二进制文件)
        * [3.3多行编辑](#3.3多行编辑)
        * [3.4不退出执行命令行](#3.4不退出执行命令行)
* [4.vim插件使用](#4.vim插件使用)
        * [4.1vundle](#4.1vundle)
        * [4.2NERDTree](#4.2nerdtree)
        * [4.3vim-markdown](#4.3vim-markdown)
        * [4.4vim-markdown-toc](#4.4vim-markdown-toc)

<!-- vim-markdown-toc -->

- [vim从入门到精通中文版](https://github.com/wsdjeg/vim-galore-zh_cn)
- [vim插件安装](https://zhuanlan.zhihu.com/p/108697739)

## 1.基础命令

```sh
# 通过编辑 `~/.vimrc`文件可以保存vim的配置，可以使用网上众多的配置。

a  # 在光标后插入字符
A  # 在行尾插入字符

o  # 在当前行之后插入新的空行
v  # 进入visual模式,可以使用j, k, l来移动光标确定选择的内容

vim a.txt  # 打开单个文件
vim a.txt b.txt  # 打开多个文件

:open a.txt  # 在vi窗口中打开一个新文件
:split a.txt  # 在新窗口中打开一个新文件

ctrl + b  # 快速回退一页
ctrl + f  # 快速前进一页

ctrl + d  # 向下翻半页
ctrl + u  # 向上翻半页

:!command  # 在vim中执行shell命令

10k  # 快速跳转到相对当前行为10行的前面第10行
```

### 1.1替换

```sh
:%s/A/B/g  # 全文中将所有的A替换为B
:%s/A/B/gc  # 回车后会将光标移动到每一次A出现的位置并提示

:s/A/B/g  # 本行中将所有A替换为B
:%s/A/B  # 只替换从光标位置开始目标的第一次
```

### 1.2查找

```sh
/text  # 查找text,按n键查找下一个,按Ｎ查找前一个,shift+n到上一个
```

### 1.3拷贝和剪切

```sh
dd  # 剪切当前行
10d  # 剪切当前开始的10行
Ｄ  # 剪切当前字符至行尾

p  # 粘贴
2yy  # 拷贝当前后开始的2行
yy  # 拷贝当前行
ZZ  # 保存并退出

:1, 10 copy 20  # 将1-10行的内容复制到20行
:1, 10 move 20  # 将1-10行的内容剪切到20行

y0  # 复制到行首部,不包括光标所在字符
y$  # 复制到行尾,包含光标所在字符
```

### 1.4跳转

```sh
:number  # 跳转到指定的行

gg  # 快速跳转至文件开头
G  # 快速跳转至文件末尾

w  # 跳到下一个单词的开头
e  # 跳到这个单词的末尾
b  # 

%  # 跳到对应的括号的位置
*  # 跳到当前光标的下一个或者上一个相同单词的地方

0  # 跳到第一列
$  # 跳到最后一列

g_  # 跳到当前行的最后一个字符
^  # 跳到当前行的第一个字符

fa  # 跳到这行a字母的下一个出现的地方
t,  # 跳到,字符的前一个字符

5k  # 相对行号跳转到向上第5行
6j  # 相对行号跳转到向下第6行

d5k  # 删除当前行到上面5行
d5j  # 删除当前行到下面5行
```

### 1.5保存和退出

```sh
:q!  # 不保存退出
:wq  # 保存退出
:wq temp.py  # 以一个文件名保存并退出
:e!  # 放弃所有修改，从上次保存开始处再编辑
```

### 1.6撤销与反撤销

```sh
u   撤销上一步操作
ctrl + r  反撤销
```

### 1.7补全

```sh
ctrl + n  # 插入模式下按下有简单的提示
```

### 1.8其他

```sh
:noh  # 取消选中的高亮
```

## 2.vimrc相关配置

```sh
:syntax on  基本的语法高亮
:set number 显示行号
```

## 3.高级操作

### 3.1跳转到函数定义处

```sh
gd  # 跳转至函数的定义处
ctrl + o  # 返回上一次的位置
```

### 3.2vim查看二进制文件

```sh
# 以二进制的格式打开文件
vim -b hello.o

# 调用系统shell命令将文件转换为十六进制显示
:%!xxd

# 再次调用系统shell命令将文件转换为原始格式显示
:%!xxd -r
```

### 3.3多行编辑

```text
1. ctrl+v 进入可视块模式
2. j/k上下选择
3. I进入插入模式编辑
4. 退出编辑模式即可看到多行编辑效果
5. 多行删除则选中待删除的内容，然后d
```

### 3.4不退出执行命令行

```sh
:!command
```

## 4.vim插件使用

### 4.1vundle

- vim插件管理器，不能并行处理
- [github地址](https://github.com/VundleVim/Vundle.vim)

```sh
# 安装
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim

# 将配置文件放到.vimrc


# 常用命令

:PluginList       - 查看已经安装的插件
:PluginInstall    - 安装插件
:PluginUpdate     - 更新插件
:PluginSearch     - 搜索插件，例如 :PluginSearch xml就能搜到xml相关的插件
:PluginClean      - 删除插件，把安装插件对应行删除，然后执行这个命令即可
h: vundle         - 获取帮助
```


### 4.2NERDTree

- 目录管理器
- [github地址](https://github.com/preservim/nerdtree)

```sh

# 移动光标定位
h j k l

# 光标在左右窗口切换
ctrl+w+w

# 切换当前窗口左右布局
ctrl + w + r

# 模糊搜索文件
ctrl + p

# 切换到前一个tab
g T

# 切换到后一个tab
g t

# 将光标所处的目录设置为家目录，进入其他目录之后，CD直接跳转回来
cd
```

### 4.3vim-markdown

- markdown扩展
- [github地址](https://github.com/plasticboy/vim-markdown)
- [使用vim+markdown高效记笔记](https://github.com/plasticboy/vim-markdown)

```sh
"查看所有配置建议
:help vim-markdwon
[[ "跳转上一个标题
]] "跳转下一个标题
]c "跳转到当前标题
]u "跳转到副标题
zr "打开下一级折叠
zR "打开所有折叠
zm "折叠当前段落
zM "折叠所有段落
:Toc "显示目录
```

### 4.4vim-markdown-toc

- [github地址](https://github.com/mzlogin/vim-markdown-toc)
- 生成markdown文件的toc
- [为markdown生成Toc的插件](https://mazhuang.org/2015/12/19/vim-markdown-toc/)

```sh
# 在当前光标后生成目录
:GenTocMarked

# 更新目录
:UpdateToc

# 取消储存时自动更新目录
let g:vmt_auto_update_on_save = 0

# 生成 GFM 链接风格的 Table of Contents。
# 适用于 GitHub 仓库里的 Markdown 文件，比如 README.md，也适用用于生成 GitBook 的 Markdown 文件。
:GenTocGFM

# 生成 Redcarpet 链接风格的 Table of Contents。
# 适用于使用 Redcarpet 作为 Markdown 引擎的 Jekyll 项目或其它地方。
:GenTocRedcarpet
```

