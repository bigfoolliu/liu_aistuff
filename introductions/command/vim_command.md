# vim快捷键

<!-- vim-markdown-toc marked -->

* [1.基础命令](#1.基础命令)
        - [1.1替换](#1.1替换)
        - [1.2查找](#1.2查找)
        - [1.3复制,删除,剪切和粘贴](#1.3复制,删除,剪切和粘贴)
        - [1.4跳转,移动](#1.4跳转,移动)
        - [1.5保存和退出](#1.5保存和退出)
        - [1.6撤销与反撤销](#1.6撤销与反撤销)
        - [1.7补全](#1.7补全)
        - [1.8插入,修改,交换](#1.8插入,修改,交换)
        - [1.9寄存器](#1.9寄存器)
        - [1.10窗口操作](#1.10窗口操作)
        - [1.11标注](#1.11标注)
        - [1.12重复](#1.12重复)
        - [1.x其他](#1.x其他)
* [2.vimrc相关配置](#2.vimrc相关配置)
* [3.高级操作](#3.高级操作)
        - [3.1跳转到函数定义处](#3.1跳转到函数定义处)
        - [3.2vim查看二进制文件](#3.2vim查看二进制文件)
        - [3.3多行编辑](#3.3多行编辑)
        - [3.4不退出执行命令行](#3.4不退出执行命令行)
        - [3.5分屏](#3.5分屏)
        - [3.6定位技巧](#3.6定位技巧)
* [4.vim插件使用](#4.vim插件使用)
        - [4.1vundle](#4.1vundle)
        - [4.2nerdtree](#4.2nerdtree)
        - [4.3vim-markdown](#4.3vim-markdown)
        - [4.4vim-markdown-toc](#4.4vim-markdown-toc)
* [5.介绍](#5.介绍)
        - [5.1模式](#5.1模式)
        - [5.2按键映射](#5.2按键映射)
        - [5.3寄存器](#5.3寄存器)
        - [5.4可视模式](#5.4可视模式)

<!-- vim-markdown-toc -->

## 1.基础命令

- [vim从入门到精通中文版](https://github.com/wsdjeg/vim-galore-zh_cn)
- [vim插件安装](https://zhuanlan.zhihu.com/p/108697739)

```sh
# 通过编辑 `~/.vimrc`文件可以保存vim的配置，可以使用网上众多的配置。
:help  # 进入帮助

a  # 在光标后插入字符
a  # 在行尾插入字符

o  # 在当前行之后插入新的空行
v  # 进入visual模式,可以使用j, k, l来移动光标确定选择的内容

vim a.txt  # 打开单个文件
vim a.txt b.txt  # 打开多个文件

:open a.txt  # 在vi窗口中打开一个新文件

ctrl + b  # 快速回退一页
ctrl + f  # 快速前进一页

ctrl + d  # 向下翻半页
ctrl + u  # 向上翻半页

ctrl + e  # 向下翻滚一行
ctrl + y  # 向上翻滚一行

:!command  # 在vim中执行shell命令

10k  # 快速跳转到相对当前行为10行的前面第10行

viw  # 快速选中并高亮当前光标处的单词
caw  # 快速删除当前单词，并进入插入模式


vim scp://cirdan@192.168.225.22/info.txt  # 编辑远程的文件
```

### 1.1替换

```sh
:%s/a/b/g  # 全文中将所有的a替换为b
:%s/a/b/gc  # 回车后会将光标移动到每一次a出现的位置并提示
:%s/a/b  # 只替换从光标位置开始目标的第一次

:s/a/b/g  # 本行中将所有a替换为b
:.,+5s/a/b  # 替换本行到下面第五行的a为b
```

### 1.2查找

```sh
/text  # 查找text,按n键查找下一个,按ｎ查找前一个,shift+n到上一个

# vim默认使用正则表达式查找
/^a  # 查找以a开头的字符


*  # 查找当前光标下的单词
# 其中一个修改组合技巧，先查找当前光标下的单词，然后替换内容，跳到下一个单词，重复,可以快速替换多个单词
* cw<esc> n .
```

### 1.3复制,删除,剪切和粘贴

```sh
2yy  # 拷贝当前后开始的2行
yy  # 拷贝当前行
zz  # 保存并退出,注意是大写

:1, 10 copy 20  # 将1-10行的内容复制到20行
:1, 10 move 20  # 将1-10行的内容剪切到20行

y0  # 复制到行首部,不包括光标所在字符
y$  # 复制到行尾,包含光标所在字符

dd  # 剪切当前行
10d  # 剪切当前开始的10行

shift + d(d)  # 删除光标后整行内容

d0  # 删除到行首
d  # 删除到行尾
d$  # 删除到行尾

d5k  # 删除当前行到上面5行
d5j  # 删除当前行到下面5行

dw  # 删除当前光标之后的一个单词
2dw  # 删除当前光标之后的2个单词

dl  # 删除一个字符
daw  # delete a word，删除一个文本对象，比如当前光标下的单词
dap  # delete a paragraph，删除一个段落

p  # 光标前粘贴
p  # 光标后面粘贴

x  # 删除光标之后的单个字符
x  # 删除光标之前的单个字符
3x  # 剪切光标后面3个字符
3x  # 剪切光标前面3个字符


# 插入模式下
ctrl + w  # 删除删除前一个单词
ctrl + u  # 删除至行首
```

### 1.4跳转,移动

```sh
:number  # 跳转到指定的行

gg  # 快速跳转至文件开头
g  # 快速跳转至文件末尾

w  # 跳到下一个单词的开头
3w  # 跳到下3个单词的开头

b  # 跳到上一个单词的开头
3b  # 跳到上3个单词的开头

e  # 跳到下个单词的末尾
ge  # 移动到上个单词的末尾

%  # 跳到对应的括号的位置
*  # 跳到当前光标的下一个或者上一个相同单词的地方

0  # 跳到第一列
$  # 跳到最后一列
^  # 跳到当前行的第一个字符

g_  # 跳到当前行的最后一个字符,不包括换行符
vg_  # 选中到当前行的最后一个字符,不包括换行符

fa  # 单字符查找,跳到这行a字母的下一个出现的地方
;  # 可以重复查找f命令所查找的命令

t,  # 跳到,字符的前一个字符

5k  # 相对行号跳转到向上第5行
6j  # 相对行号跳转到向下第6行
```

### 1.5保存和退出

```sh
:q!  # 不保存退出
:wq  # 保存退出

:wq temp.py  # 以一个文件名保存并退出
:e!  # 放弃所有修改，从上次保存开始处再编辑

:w temp.py  # 将当前文件保存为指定文件名并继续编辑
```

### 1.6撤销与反撤销

```sh
u  # 撤销上一步操作
ctrl + r  # 反撤销
```

### 1.7补全

```sh
ctrl + n  # 插入模式下按下有简单的提示

tab  # 设置代码段之后可以展示
```

### 1.8插入,修改,交换

```sh
# 插入
i  # 在当前光标的前面开始插入
i # 在当前行的第一个非空字符前插入

gi  # 在当前行的第一列插入

a  # 在行尾插入
a  # 在光标后插入

o  # 在下面新建一行插入
o  # 在上面新建一行插入


# 修改
c   # change，改变文本，类似d，只是在结束之后会进入插入模式
cw  # 先删除该单词然后立马进入插入模式，即修改单词
c2w  # 先删除接下里的两个单词，然后进入插入模式


# 交换
xp  # 前后两个字符的位置反了使用，将光标放在前一个字符上
```

### 1.9寄存器

```sh
:help registers  # 查看寄存器帮助信息

:reg  # 查看目前寄存器的情况

# 将内容复制到系统剪贴板,需要使用+寄存器, 选中内容后：
"+y
```

### 1.10窗口操作

```sh
:sp[lit]  # 水平分割一个新窗口.
:split a.txt  # 在水平的新窗口中打开一个文件.

:vs[plit]  # 垂直分割一个新窗口.
:vsplit a.txt  # 在垂直的新窗口中打开一个文件


:clo[se]  # 关闭当前的窗口,可以避免在剩下一个窗口的时候关闭vim
```

### 1.11标注

```sh
:marks  # 显示所有的标注

m + 任意字符  # 给当前为位置标注
`m  # 跳转到刚才标注的行
```

### 1.12重复

```sh
# 比如在每一行的行尾加一个m字符，可以执行 $am, 然后到下一行直接运行 .
.  # 重复执行上一步的修改，可以减少重复操作
```

### 1.x其他

```sh
:noh  # 取消选中的高亮

g ctrl + g  # 统计文件中的字符个数


>  # 对当前行缩进，单行或者多行
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
vim -b hello.o  # 以二进制的格式打开文件

:%!xxd  # 调用系统shell命令将文件转换为十六进制显示

:%!xxd -r  # 再次调用系统shell命令将文件转换为原始格式显示
```

### 3.3多行编辑

```text
1. ctrl+v 进入可视块模式
2. j/k上下选择
3. i进入插入模式编辑
4. 退出编辑模式即可看到多行编辑效果
5. 多行删除则选中待删除的内容，然后d
```

### 3.4不退出执行命令行

```sh
:!command   # 不退出直接执行命令
```

### 3.5分屏

```sh
# 直接分屏打开多个文件
vim -on [file1] [file2]  # 水平分屏打开
vim -on [file1] [file2]  # 垂直分屏打开

# 在已经打开一个文件的情况下分屏
:new  # 打开一个空的窗口
:vs [file]  # 垂直分屏
:sp [file]  # 水平分屏

# 分屏之间的光标移动
ctrl + w + w  # 不同的分屏之间切换,两个分屏时方便
ctrl + w + [hjkl]  # 上下左右不同窗口切换

:qall  # 直接关闭所有窗口退出
:wall  # 保存所有窗口的内容
```

### 3.6定位技巧

```sh
w  # 正向移动到下一单词的开头
b  # 反向移动到当前单词/上一单词的开头

e  # 移动到当前单词/下一单词的结尾
ge  # 反向移动到上一单词的结尾

0或者^  # 移动到行首
$  # 移动到行尾

l  # 向右边移动一个字符
10 l  # 向右移动80个字符

10 |  # 直接移动到当前行的第10列(从1开始)
```

## 4.vim插件使用

### 4.1vundle

- vim插件管理器，`不能并行处理`
- [github地址](https://github.com/vundlevim/vundle.vim)

```sh
# 安装
git clone https://github.com/vundlevim/vundle.vim.git ~/.vim/bundle/vundle.vim

# 将配置文件放到.vimrc
:w

# 常用命令
:pluginlist       # 查看已经安装的插件
:plugininstall    # 安装插件
:pluginupdate     # 更新插件
:pluginsearch     # 搜索插件，例如 :pluginsearch xml就能搜到xml相关的插件
:pluginclean      # 删除插件，把安装插件对应行删除，然后执行这个命令即可
h: vundle         # 获取帮助
```

### 4.2nerdtree

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
g t

# 切换到后一个tab
g t

# 将光标所处的目录设置为家目录，进入其他目录之后，cd直接跳转回来
cd
```

### 4.3vim-markdown

- markdown扩展
- [github地址](https://github.com/plasticboy/vim-markdown)
- [使用vim+markdown高效记笔记](https://github.com/plasticboy/vim-markdown)

```sh
# 查看所有配置建议
:help vim-markdown

`[[`  # 跳转上一个标题
]]  # 跳转下一个标题
]c  # 跳转到当前标题
]u  # 跳转到副标题
zr  # 打开下一级折叠
zr  # 打开所有折叠
zm  # 折叠当前段落
zm  # 折叠所有段落
:toc  # 显示目录
```

### 4.4vim-markdown-toc

- [github地址](https://github.com/mzlogin/vim-markdown-toc)
- 生成markdown文件的toc
- [为markdown生成toc的插件](https://mazhuang.org/2015/12/19/vim-markdown-toc/)

```sh
# 在当前光标后生成目录
:gentocmarked

# 更新目录
:updatetoc

# 取消储存时自动更新目录
let g:vmt_auto_update_on_save = 0

# 生成 gfm 链接风格的 table of contents。
# 适用于 github 仓库里的 markdown 文件，比如 readme.md，也适用用于生成 gitbook 的 markdown 文件。
:gentocgfm

# 生成 redcarpet 链接风格的 table of contents。
# 适用于使用 redcarpet 作为 markdown 引擎的 jekyll 项目或其它地方。
:gentocredcarpet
```

### 4.5nerdcommenter

```sh
# 先选中多行
\cc  # <leader>表示符号\
\cu  # 取消注释
```

### 4.6easy-motion

- 屏幕快速跳转

```sh
\\w  # 快速标记当前页面光标下部所有的单词
\\b  # 快速标记当前页面光标上部所有的单词

\\j  # 标记下方的行
\\k  # 标记上方的行
```

## 5.介绍

### 5.1模式

- 插入模式,insert
- 命令模式,command-line
- 可视模式,visual
- 普通模式,normal

### 5.2按键映射

- 除非递归映射是必须的，否则配置都是使用非递归
- `:map` 和`:noremap`, 前者递归，后者不递归，使用模式:`normal, visual, operator-pending`
- `:nmap` 和`nnoremap`, 前者递归，后者不递归，使用模式: `normal`
- `:xmap` 和`:xnoremap`, 前者递归，后者不递归，使用模式: `visual`
- `:cmap` 和`:cnoremap`, 前者递归，后者不递归，使用模式: `command-line`
- `:omap` 和`:onoremap`, 前者递归，后者不递归，使用模式: `operator-pending`
- `:imap` 和`:inoremap`, 前者递归，后者不递归，使用模式: `insert`

### 5.3寄存器

存储文本的地方，复制粘贴就是在寄存中存和取文本。

- 使用命令`:register`或者`:reg`查看当前所有寄存器中的内容

### 5.4可视模式

```sh
# 三种不同的可视模式
v  # 进入面向字符的可视模式

V  # 进入面向行的可视模式,直接选中整行

ctrl + v  # 进入面向块的可视模式

gv  # 重选上次的高亮区域

o  # 在可视模式下，可以切换高亮选区的活动端，即开始端选错了不用退出重新选
```

### 5.5命令行模式

### 5.6文件

### 5.7更快的移动和跳转

## 6.neovim使用

```sh
# 安装
brew install neovim

# 配置文件路径: ～/.config/nvim/init.vim

# 安装vim-plug插件管理器
curl -fLo ~/.local/share/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
```

