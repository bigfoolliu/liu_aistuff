# memcache

<!-- vim-markdown-toc Marked -->

* [1.简介](#1.简介)

<!-- vim-markdown-toc -->

## 1.简介

```sh
# mac安装
brew install memcached

# 启动
# -p 指定端口号（默认11211）
# -t 线程数（默认4）
# -l 连接的IP地址, 默认是本机
# -d start 启动memcached服务
# -d restart 重起memcached服务
# -d stop|shutdown 关闭正在运行的memcached服务
# -m 最大内存使用，单位MB。默认64MB
# -M 内存耗尽时返回错误，而不是删除项 
# -c 最大同时连接数，默认是1024
# -f 块大小增长因子，默认是1.25
# -n 最小分配空间，key+value+flags默认是48

memcached -m 32 -p 11211 -d start
brew services start memcached
```
