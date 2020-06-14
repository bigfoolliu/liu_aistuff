# tmux会话管理器

!-- vim-markdown-toc Marked -->

* [1.介绍](#1.介绍)
* [2.基本命令](#2.基本命令)

<!-- vim-markdown-toc -->

## 1.介绍

- [阮一峰tmux使用](http://www.ruanyifeng.com/blog/2019/10/tmux.html)

会话的重要特点:

1. 窗口与其中启动的进程是连在一起
2. 打开窗口，会话开始
3. 关闭窗口，会话结束，会话内部的进程也会随之终止，不管有没有运行完

## 2.基本命令

```shell
tmux new  # 创建一个新的tmux会话
tmux new -s mysession  # 创建一个叫mysession的会话

tmux a  # 连接上一个会话
tmux new -t mysession  # 连接已经命名的会话

tmux ls  # 显示会话列表

tmux kill-session  # 关闭上次打开的会话
tmux kill-session -t s1  # 关闭会话s1
tmux kill-server  # 关闭所有会话

# 退出当前会话,就不会保存会话了
ctrl + d
exit

tmux detatch  # 会话窗口分离，但是会话和里面的进程仍然在运行
tmux attach -t my-sess  # 接入已经存在的会话

tmux switch -t my-sess2  # 切换到另外一个会话

tmux rename-session -t my-sess1 my-sess2  # 将绘画重命名 

ctrl+b :  # 进入命令行模式

ctrl+b :set -g mouse on  # 设置全局鼠标可用

ctrl+b s  # 列出会话，可切换
ctrl+b $  # 重命名会话

ctrl+b n  # 切换至下一个会话
ctrl+b p  # 切换至上一个会话

# 窗口管理

ctrl+b c  # 创建一个新窗口
ctrl+b d  # 分离(结束)当前会话
ctrl+b 0~9  # 选择编号0-9的窗口

ctrl+b &  # 关闭当前窗口

# 窗格管理

ctrl+b %  # 水平方向创建窗格
ctrl+b "  # 垂直方向创建窗格

ctrl+b Up/Down/Left/Right  # 根据箭头方向来切换窗格

ctrl+b q  # 显示窗格编号

ctrl+b x  # 关闭当前窗格
ctrl+b space(空格键)  # 重新排列当前窗口下的所有的窗格

ctrl+b !  # 将当前窗格置于新的窗口
ctrl+b z  # 放大当前窗格(再次按下将还原)
ctrl+b i  # 显示当前窗格信息
```

