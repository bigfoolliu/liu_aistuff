# MAC高效使用技巧

<!-- vim-markdown-toc Marked -->

* [1.命令行命令](#1.命令行命令)
        - [1.1通用系统命令](#1.1通用系统命令)
        - [1.2其他命令行命令](#1.2其他命令行命令)
* [2.safari命令](#2.safari命令)
* [3.终端命令](#3.终端命令)
        - [3.1brew](#3.1brew)
        - [3.2iterm2](#3.2iterm2)
        - [3.3fzf](#3.3fzf)
        - [3.4musicbox](#3.4musicbox)
        - [3.5zsh插件命令](#3.5zsh插件命令)
        - [3.6youtube-dl](#3.6youtube-dl)
        - [3.7uglifyjs](#3.7uglifyjs)
        - [3.8term2048](#3.8term2048)
* [4.安装python环境](#4.安装python环境)
* [5.安装使用mysql](#5.安装使用mysql)
* [6.pycharm快捷键](#6.pycharm快捷键)
* [7.系统快捷键](#7.系统快捷键)
* [8.其他](#8.其他)
        - [8.1开发工具](#8.1开发工具)
        - [8.2使用技巧](#8.2使用技巧)

<!-- vim-markdown-toc -->

## 1.命令行命令

### 1.1通用系统命令

```sh
ctrl + a  # 光标移动到行首,加#使命令失效
ctrl + e  # 光标移动到行尾
ctrl + q  # 删除当前行的命令
ctrl + w  # 删除光标所在单词
ctrl + l  # 清屏，类似于clear
ctrl + k  # 删除到末尾的命令

ctrl + command + space  # 快速调出表情
ctrl + b  # 向后翻页
ctrl + f  # 向前翻页

command + ctrl + q  # 锁定屏幕
command + q  # 关闭应用
command + m  # 最小化应用(会导致command + tab键的时候不能看到)
command + h  # 隐藏当前窗口(建议使用，command + tab键的时候可以显示)
command + z  # 万能的还原操作
command + option + h  # 隐藏其他所有窗口

command + down  # 选中文件之后可以打开
command + space  # 打开sPOTLight

command + [  # finder返回
command + ]  # finder前进
command + left  # 定位到行首
command + right  # 定位到行尾

command + ⬆️   # 返回上层目录

command + shift + 3  # 截取整个屏幕
command + shift + 4  # 截取部分区域
command + shift + 5  # 打开截屏录屏等(实用)

command + shift + 音量键  # 精确调节音量
command + shift + 亮度键  # 精确调节亮度

command + c  # 拷贝(win中的复制)
command + v  # 粘贴
command + alt + v  # 粘贴(但不保留复制的文件，类似于剪切)
command + backspace  # 删除选中的文件
command + shift + option + v  # 去除格式粘贴

command + tab  # 切换不同应用程序的窗口
command + \`  # 切换同一应用程序的不同窗口

# 恢复最小化的窗口
command + tab 到应用后，松开 tab，然后按 option 上，再松开 command

# 关闭，打开mkworker进程（用于spotlight建立索引，占用大量cpu）
sudo mdutil -a -i off
sudo mdutil -a -i on

F11  # 显示桌面
ctrl + command + f  # 进入/退出全屏

# 调整finder大小
# 按住options键，调整之后关闭，再次打开则是设定好的大小

# 重建聚焦索引
sudo mdutil -a -i on


# 使用文件默认的打开app来打开文件
open <file_name>
# 使用指定的app来打开文件
open -a /Applications/*.app <file_name>
# 在finder中打开指定的路径
open ./


ctrl + command + space  # 快速打开emoji表情😄
```

### 1.2其他命令行命令

```sh
# 查看网络上传下载速度
fast
fash --upload

# cat的替代命令，可以高亮度
bat file
bat ./*.file  # 可以同时查看多个文件
```

## 2.safari命令

```sh
command + t  # 新建标签页面
command + w  # 关闭标签页面

command + tab  # 移动至下一个标签页
command + shift + tab  # 移动到上一个标签页
```

## 3.终端命令

### 3.1brew

- [安装homebrew](https://www.wandouip.com/t5i171897/)
- [终端颜色设定介绍](https://blog.csdn.net/liumiaocn/article/details/102962691)

```sh
# shell相关
cat /etc/shells  # 查看当前可用的shells
echo $SHELL  # 查看当前使用的shell
chsh -s /bin/bash  # 将终端shell切换为bash，需要重启
chsh -s /bin/zsh  # 将终端shell切换为zsh，需要重启

ctrl + a  # 跳到命令首部
ctrl + e  # 跳到命令尾部

ctrl + w  # 删除当前光标前到单词首位的字符
ctrl + k  # 删除光标之前到行尾的字符
ctrl + u  # 删除光标之前到行首的字符

# homebrew命令
brew update  # 更新 Homebrew
brew upgrade  # 更新所有安装过的软件包
brew upgrade wget  # 更新指定的软件包
brew search wget  # 查找软件包
brew install wget  # 安装软件包
brew remove wget  # 卸载软件包
brew list  # 列出已安装的软件包
brew info wget  # 查看软件包信息
brew deps wget  # 列出软件包的依赖关系
brew outdated  # 列出可以更新的软件包

# homebrew修改为国内源
cd "$(brew --repo)"
git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/brew.git

cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
git remote set-url origin https://mirrors.tuna.tsinghua.edu.cn/git/homebrew/homebrew-core.git

ncdu  # 查看磁盘目录占用情况

sudo killall -HUP mDNSResponder  # 最新版本系统刷新dns缓存
```

### 3.2iterm2

- [iterm官网](https://www.iterm2.com/index.html)
- [设置鼠标滑动可以翻转页面](https://blog.csdn.net/weixin_34138521/article/details/94600287)
- [iterm2设置自动登陆目标服务器](https://note.youdao.com/ynoteshare1/index.html?id=426e9cfe0d81b3449f54e2e9da5beb8b&type=note)

基本使用技巧：

- 双击选中，三击选中整行，四击只能选中（可配置）
- command键技巧：选中字符可拖拽；点击url可访问；点击文件可以用默认程序打开；点击文件夹可在finder打开
- 用于使用了vim-mode，可以使用esc+v，来将当前输入的命令进入vim模式,可以复制，粘贴

常用命令:

```sh
# 将当前窗口分割
command + d  # 水平分割
command + shift + d  # 垂直分割

# 将当前活动窗口最大化,再次点击将会显示隐藏窗口
command + shift + enter

# 拆分的窗格之间导航
command + [
command + ]

# 窗口导航
command + 左/右箭头
command + 数字  # 直接导航到指定窗口

# 开启搜索
command + f

# 标记和回到标记
command + shift + m
command + shift + j

# 查看粘贴历史
command + shift + h

# 倒退时间以准确查看最近一段时间的屏幕上的内容
command + option + b

# 打开/关闭全屏窗口
command + enter

# shell集成(需要安装iTerm2 > Install Shell Integration)
# 图片操作
imgcat a.png  # 命令行查看图片
imgls ./  # ls增强版，可以让图片有个缩略图
# 其他用途
# 1.单击即可从远程下载文件
# 2.从本地的finder拖动即可将文件复制到远程

# tmux集成
# 基本使用一致，但是进入时候需要-CC
tmux -CC attach-session -t a

# 清除当前行的命令
ctrl + u
```

### 3.3fzf

- 主要功能是查找文件，历史命令查询，快速进入目录
- [知乎打造fzf](https://zhuanlan.zhihu.com/p/53380250)
- [fzf使用](http://einverne.github.io/einverne.github.io/post/2019/08/fzf-usage.html)

```sh
# 安装
brew install fd fzf

# 命令历史,可以直接使用数字来指定
ctrl + r

# 设置好预览，直接预览文件
pp

# 搜索当前目录下的内容
ctrl + t

# 设置别名快速vim编辑文件
vfzf

# 设置别名快速cd
dfzf
```

### 3.4musicbox

```sh
# 命令行版本网易云
musicbox
```

### 3.5zsh插件命令

```sh
# emoji
display_emoji  # 显示所有可展示的emoji
echo $emoji[family]  # 展示特定的emoji
random_emoji  # 随机显示一个emoji

# git
glols  # git log图形化展示
gl  # git pull
gcm  # git checkout master
gcd  # git checkout develop
gst  # git status

# battery
battery_time_remaining  # 查看电量剩余
battery_pct  # 查看电池容量
battery_is_charing  # 查看电池是否在充电

# jump
mark ***  # 将当前目录一个指定的标记
unmark ***  # 删除当前标记
jump ***  # 跳转去标记的目录
marks  # 查看所有的标记

# web-search
baidu xxx  # 使用百度搜索关键词
google xxx  # 谷歌搜索关键词
github xxx
bing xxx
stackoverflow xxx
image xxx  # duckduckgo图片网站搜索

# extract
extract file  # 快速解压文件

# redis-cli
redis-cli  # 进入redis，可以有提示

# encode
encode64 "aa"  # 将数据编码为base64
e64 "aa"
decode64 "aa"  # 将base64解码为原始数据
d64 "aa"

# urltools
urlencode https://www.github.com  # url进行编码
urldecode https://www.github.com  # url进行解码

# python
IPython  # 交互式python环境
pyfind  # 在当前目录递归寻找.py文件
pyclean ./   # 删除指定目录内部的字节码文件和换缓存文件

# copy
copydir  # 将当前路径复制进系统剪贴板
copyfile xxx  # 将文件内容复制进系统剪贴板

# jsontools
echo '{"a":1}' | pp_json  # 美化输出json
less a.json | is_json  # 判读文件是否为合法的json格式文件
echo '{"b":2, "a":1}' | urlencode_json  # 将内容json编码

# vi-mode
# 允许用vim的方式来使用命令行,esc进入normal模式，v来编辑

# zsh_reload
src  # 直接source .zsh配置文件
```

### 3.6youtube-dl

- 从视频网站平台下载视频

```sh
```

### 3.7uglifyjs

- js代码格式化优化工具
- [uglifyjs](https://github.com/mishoo/UglifyJS)

```sh
# 全局安装
npm install uglify-js -g

# 将js代码简单压缩，合并为一行
uglifyjs 1.js -o 1.min.js

# 使用单引号替换双引号的美化或者直接美化
uglifyjs 1.js -b quote_style=1 -o 1b.js
```

### 3.8term2048

```sh
# 启动终端版2048
term2048
```

## 4.安装python环境

- [mac安装pyenv以及pyenv的使用](https://www.cnblogs.com/kumufengchun/p/10986498.html)

## 5.安装使用mysql

- [mac安装mysql](https://blog.csdn.net/w605283073/article/details/80417866?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)
- **当前使用的mysql密码强度为1(medium), Lxxxxxxxx?**

```sh
brew install mysql

brew services start mysql
brew services stop mysql

# mysql终端代码高亮工具mycli
brew install mycli
mycli mysql://root@127.0.0.1:3306/data_base
```

## 6.pycharm快捷键

```sh
command + backspace  # 删除当前行
```

## 7.系统快捷键

```sh
command + space  # 打开spotlight搜索
```

## 8.其他

### 8.1开发工具

- pycharm
- vim
- alfred: 替代spotlight
- dash for mac: api以及文档查询工具
- homebrew: 软件包安装,管理
- iterm2: 替代原生终端
- oh-my-zsh: 终端工具5
- material ui: 主题

### 8.2使用技巧

- 对于只是想简单查看一下内容的文档,按空格，使用**预览**功能打开,速度更快
