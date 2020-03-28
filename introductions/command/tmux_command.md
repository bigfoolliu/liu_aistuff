# tmux会话管理快捷键

<!-- vim-markdown-toc Marked -->

* [1.常用命令](#1.常用命令)

<!-- vim-markdown-toc -->


## 1.常用命令

```shell
tmux new        create a new tmux session
tmux new -s mysession       创建一个叫mysession的会话

tmux ls     显示会话列表

tmux a      连接上一个会话
tmux a -t mysession     连接指定的会话

tmux kill-session       关闭上次打开的会话
tmux kill-session -t s1     关闭会话s1
tmux kill-server        关闭所有会话

常用快捷键:

ctrl+b s        列出会话，可切换
ctrl+b $        rename the session

ctrl+b n        切换至下一个会话
ctrl+b p        切换至上一个会话

窗口管理：

ctrl+b c        创建一个新窗口
ctrl+b d        分离(结束)当前会话
ctrl+b 0~9      选择编号0-9的窗口

ctrl+b &        关闭当前窗口

窗格管理:

ctrl+b %        水平方向创建窗格
ctrl+b "        垂直方向创建窗格

ctrl+b Up/Down/Left/Right   根据箭头方向来切换窗格

ctrl+b q        显示窗格编号

ctrl+b x        关闭当前窗格
ctrl+b space(空格键)        重新排列当前窗口下的所有的窗格

ctrl+b !        将当前窗格置于新的窗口
ctrl+b z        放大当前窗格(再次按下将还原)
ctrl+b i        显示当前窗格信息
```

