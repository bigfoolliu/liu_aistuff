# mac高效使用技巧

<!-- vim-markdown-toc Marked -->

* [1.命令行命令](#1.命令行命令)
        * [1.通用系统命令](#1.通用系统命令)
        * [1.2其他命令行命令](#1.2其他命令行命令)
* [2.safari命令](#2.safari命令)
* [3.终端命令](#3.终端命令)
* [4.安装python环境](#4.安装python环境)
* [5.安装使用mysql](#5.安装使用mysql)
* [6.pycharm快捷键](#6.pycharm快捷键)
* [7.系统快捷键](#7.系统快捷键)
* [8.开发工具](#8.开发工具)

<!-- vim-markdown-toc -->

## 1.命令行命令

### 1.通用系统命令

```shell
ctrl + a  # 光标移动到行首
ctrl + e  # 光标移动到行尾
ctrl + q  # 删除当前行的命令
ctrl + w  # 删除光标所在单词

ctrl + command + space  # 快速调出表情
ctrl + b  # 向后翻页
ctrl + f  # 向前翻页

command + ctrl + q  # 锁定屏幕
command + q  # 关闭应用
command + m  # 最小化应用(会导致command + tab键的时候不能看到)
command + h  # 隐藏当前窗口(建议使用，command + tab键的时候可以显示)
command + option + h  # 隐藏其他所有窗口

command + down  # 选中文件之后可以打开
command + space  # 打开spotlight

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

command + tab  # 切换窗口

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

```shell
# 查看网络上传下载速度
fast
fash --upload

# cat的替代命令，可以高亮度
bat file
bat ./*.file  # 可以同时查看多个文件
```

## 2.safari命令

```shell
command + t  # 新建标签页面
command + w  # 关闭标签页面

command + tab  # 移动至下一个标签页
command + shift + tab  # 移动到上一个标签页
```

## 3.终端命令

- [安装homenbrew](https://www.wandouip.com/t5i171897/)
- [终端颜色设定介绍](https://blog.csdn.net/liumiaocn/article/details/102962691)

```shell
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
```

## 4.安装python环境

- [mac安装pyenv以及pyenv的使用](https://www.cnblogs.com/kumufengchun/p/10986498.html)

## 5.安装使用mysql

- [mac安装mysql](https://blog.csdn.net/w605283073/article/details/80417866?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task)
- **当前使用的mysql密码强度为1(medium), Lxxxxxxxx?**

```shell
brew install mysql

brew services start mysql
brew services stop mysql

# mysql终端代码高亮工具mycli
brew install mycli
mycli mysql://root@127.0.0.1:3306/data_base
```

## 6.pycharm快捷键

```shell
command + backspace  # 删除当前行
```

## 7.系统快捷键

```shell
command + space  # 打开spotlight搜索 
```

## 8.开发工具

- pycharm
- vim
- alfred: 替代spotlight
- dash for mac: api以及文档查询工具
- homebrew: 软件包安装,管理
- iterm2: 替代原生终端
- oh-my-zsh: 终端工具5
- material ui: 主题
 
