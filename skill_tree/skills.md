# effiency提高效率的小技巧

<!-- TOC -->

- [effiency提高效率的小技巧](#effiency提高效率的小技巧)
    - [1.为命令设置别名(alias)](#1为命令设置别名alias)
    - [2.dotfiles快速将恢复自身配置](#2dotfiles快速将恢复自身配置)
    - [3.项目里重复的工作写成makefile](#3项目里重复的工作写成makefile)
    - [4.快速为项目选择一个source license](#4快速为项目选择一个source-license)
    - [5.量化工作](#5量化工作)
    - [6.会话以及终端管理tmux](#6会话以及终端管理tmux)
    - [7.windows虚拟桌面(workspace)](#7windows虚拟桌面workspace)
    - [8.必读书籍](#8必读书籍)
    - [9.开发者工具](#9开发者工具)
    - [10.chrome高效使用](#10chrome高效使用)
    - [11.ssh免密以及别名登录](#11ssh免密以及别名登录)

<!-- /TOC -->

[效率指南](https://leohxj.gitbooks.io/a-programmer-prepares/effciency/coder-guide.html)

## 1.为命令设置别名(alias)

[alias为命令设置别名](https://blog.csdn.net/doiido/article/details/43762791)

## 2.dotfiles快速将恢复自身配置

[dotfiles入门](https://luolei.org/dotfiles-tutorial/)
[dotfiles合集](http://dotfiles.github.io/)

## 3.项目里重复的工作写成makefile

[makefile由浅入深](https://zhuanlan.zhihu.com/p/47390641)

## 4.快速为项目选择一个source license

[chooselicense.com](https://choosealicense.com)

## 5.量化工作

[quantify your code](https://blog.newrelic.com/culture/quantify-your-code/)

## 6.会话以及终端管理tmux

[使用tmux加速操作](http://cenalulu.github.io/linux/tmux/)

## 7.windows虚拟桌面(workspace)

[win10虚拟桌面](https://sspai.com/post/45594)

- win + ctrl + d: 创建新的虚拟桌面
- win + ctrl + left/right: 左右切换虚拟桌面
- win + ctrl + f4: 删除当前的虚拟桌面
- win + w: windowslink工作区
- win + e: 打开资源管理器
- win + r, psr.exe：打开步骤计数器

## 8.必读书籍

[程序员必读书单](http://lucida.me/blog/developer-reading-list/)

## 9.开发者工具

[免费开发工具](https://github.com/ripienaar/free-for-dev)

## 10.chrome高效使用

- ctrl + t: 打开新的标签页
- ctrl + n: 打开新的窗口
- ctrl + pgUp/pgDown: 切换标签页
- ctrl + w/f4: 关闭当前标签页
- alt + space + n: 最小化当前窗口
- alt + space + x: 最大化当前窗口

## 11.ssh免密以及别名登录

```shell
# 1.本地生成公钥和私钥,默认放置路径为~/.ssh/id_rsa以及~/.ssh/id_rsassh-keygen.pub
# 需要输入一个密码需要记忆,如果输入为空则为免密登录
ssh-keygen
# 2.将本地的公钥放到远程主机
ssh-copy-id ubuntu@192.168.6.121
# 3.登录时候需要输入自己的密码或者为空
ssh ubuntu@192.168.6.121

# 如果需要将远程主机取别名在~.ssh/config文件中加入
Host 1
    HostName 192.168.1.1
    User ubuntu
    Port 22
```
