# windows常用命令

<!-- vim-markdown-toc Marked -->

* [1.基本操作](#1.基本操作)

<!-- vim-markdown-toc -->

## 1.基本操作

```sh
# 打开cmd窗口
win + r, cmd


cls  # 清除屏幕

start a.ext  # 启动某个程序

systeminfo  # 查看系统信息

shutdown  # 关机
shutdown /s /t 3600  # 一小时之后关闭
shutdown /r  # 重启

tasklist  # 显示当前运行的程序(包括pid)
taskkill /pid 12  # 结束指定进程
taskkill /im notepad.exe  # 结束指定名称的进程

cd  # 显示当前目录

dir  # 显示当前目录的子文件夹和文件
dir /S  # 递归显示当前目录下的文件
dir key*  # 显示当前目录下的以key开头的文件和文件夹的信息

tree  # 显示目录结构

ren a.txt b.txt  # 重命名文件
move a.txt dir  # 移动文件到指定文件夹

del a.txt  # 删除文件

type a.txt  # 查看文件内容

md dir  # 创建一个目录
rd dir  # 删除一个目录

copy a.txt dir  # 拷贝一个文件到指定文件夹 


ipconfig /all  # 查看ip信息
```

