# mac基础命令教程

## 1.系统命令

```shell

command + ctrl + q  # 锁定屏幕
command + q  # 关闭应用
command + w  # 最小化应用

command + down  # 选中文件之后可以打开

command + space  # 打开spotlight

command + shift + 3  # 截取整个屏幕
command + shift + 4  # 截取部分区域

ctrl + command + space  # 快速调出表情

command + c  # 拷贝(win中的复制)
command + v  # 粘贴
command + alt + v  # 粘贴(但不保留复制的文件，类似于剪切)
command + backspace  # 删除选中的文件
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

```shell
# shell相关
cat /etc/shells  # 查看当前可用的shells
echo $SHELL  # 查看当前使用的shell
chsh -s /bin/bash  # 将终端shell切换为bash，需要重启
chsh -s /bin/zsh  # 将终端shell切换为zsh，需要重启

ctrl + a  # 跳到命令首部
ctrl + e  # 跳到命令尾部

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
```

## 4.安装python环境

- [mac安装pyenv以及pyenv的使用](https://www.cnblogs.com/kumufengchun/p/10986498.html)

```shell
```

