# nginx知识

<!-- TOC -->autoauto- [nginx知识](#nginx知识)auto    - [1.基本介绍](#1基本介绍)auto        - [1.3语法](#13语法)auto        - [1.4主要应用场景](#14主要应用场景)auto        - [1.5组成](#15组成)auto        - [1.7编译出自己的nginx](#17编译出自己的nginx)auto    - [2.nginx命令](#2nginx命令)auto        - [1.3nginx启动和关闭](#13nginx启动和关闭)auto        - [2.2nginx操作命令](#22nginx操作命令)auto    - [3.nginx配置](#3nginx配置)auto        - [3.1全局块常用配置](#31全局块常用配置)auto        - [3.2events块配置](#32events块配置)auto        - [3.3http全局块配置](#33http全局块配置)auto        - [3.4http中server块配置](#34http中server块配置)auto    - [a.其他](#a其他)auto        - [a.1nginx如何做到热部署](#a1nginx如何做到热部署)auto        - [a.2配置静态资源服务器](#a2配置静态资源服务器)auto        - [a.3搭建一个具备缓存功能的反向代理服务器](#a3搭建一个具备缓存功能的反向代理服务器)autoauto<!-- /TOC -->

- [nginx教程](http://tengine.taobao.org/book/chapter_02.html)
- [nginx.io(快速生成nginx的配置文件)](https://nginxconfig.io/)
- [nginx中文文档](http://www.nginx.cn/doc/)
- [nginx英文文档](https://nginx.org/en/docs/)

## 1.基本介绍

- nginx是`先加载一个主配置文件nginx.conf`，`在nginx.conf里再加载conf.d目录下的子配置文件`

### 1.3语法

1. 配置文件由指令和指令块组成
2. 每条`指令由;分号结尾`，指令与参数间以空格分割
3. 指令块以{}大括号将多条指令结合
4. include语句允许组合多个配置文件以提升可读性
5. 使用#添加注释
6. 使用$使用变量
7. 部分指令的参数支持正则表达式

### 1.4主要应用场景

- [nginx教程，核心知识100讲，youtobe地址](https://www.youtube.com/watch?v=uYPO4tJPAAY&list=PLSKUOdPqiSdtP6wNRo2vjHiWwcrC7MD8X&index=10)
- [nginx官方帮助文档，配置文件等](http://nginx.org/en/docs/)

1. 静态资源服务，通过本地文件系统提供服务
2. 反向代理服务，缓存，负载均衡等
3. 动静分离，将动态页面和静态页面分开为不同的服务器，提高速度
4. API服务

### 1.5组成

1. nginx的二进制可执行文件，各模块编译出来的一个文件
2. nginx.conf配置文件，控制nginx的行为
3. access.log访问日志，记录每一条http请求信息
4. error.log错误日志，定位问题

### 1.7编译出自己的nginx

- [开源版(偶数版本为稳定版)](http://nginx.org/)
- [商业版](http://nginx.com)

```shell
# 1. 下载
# 2. 配置
# 3. 编译
# 4. 安装

# 下载
wget http://nginx.org/download/nginx-1.16.0.tar.gz
tar -xzf nginx-1.16.0.tar.gz
cd nginx-1.16.0

# 配置
# 将nginx的对于vim的配置文件拷贝，让vim可以识别nginx的语法
cp -r contrib/vim/* ~/.vim/

# 编译
# 使用默认参数或者自定义编译(./configure --help查看)至指定目录
./configure --prefix=/home/admin/nginx

# 安装
cd /home/admin/nginx
make install

# 热部署
# 即使用新版本的nginx来替换原有的nginx,但不停止服务
# 备份原有的nginx二进制文件，将新版本的nginx二进制文件替换掉原来的
cd /home/admin/nginx/sbin
cp nginx nginx.old
cp -r /nginx /home/admin/nginx/sbin/ -f
# 向nginx的master进程发送信号,此时会生成新的nginx的master和worker进程
kill -USR2 1314
# 向旧的nginx的master进程发送信号让其优雅退出
kill -WINCH 1314
```

## 2.nginx命令

### 1.3nginx启动和关闭

```shell
# 找到nginx的安装位置，带上参数-c，最后加上nginx的配置文件的地址
/usr/local/nginx/sbin/nginx -c /usr/local/nginx/conf/nginx.conf

# 从容停止，在进程中找到nginx(带 master 的process)并杀掉进程
ps -ef | grep nginx
kill -QUIT 2072

# 快速停止
ps -ef | grep nginx
kill -TERM 2132

# 强制停止
pkill -9 nginx
```

### 2.2nginx操作命令

```shell
# 重载配置文件，不停止原有服务
nginx -s reload

# 优雅的停止文件
nginx -s quit

# 立刻停止服务
nginx -s stop

# 重新开始记录日志文件
nginx -s reopen
```

## 3.nginx配置

### 3.1全局块常用配置

- 配置影响影响全局的命令
- 包括nginx的用户组
- nginx进程pid存放路径
- 日志存放路径
- 允许生成worker process数量等

```shell
# 指定Nginx Worker进程运行用户，涉及文件访问权限
user root;
user wwwuser wwwgroup;

# 修改 Nginx 进程最大可打开文件数: https://blog.csdn.net/liupeifeng3514/article/details/79007079
# 操作系统启动多少个工作进程运行nginx
worker_processes auto;
worker_processes 4;

# 配置文件的包含，Nginx.conf include使用：https://blog.csdn.net/ruby113028/article/details/52461452
inlude /usr/local/nginx/conf/vhosts/*.conf;
```

### 3.2events块配置

- 涉及的指令主要影响nginx服务器与用户的网络连接

```shell
events {
    # 单个工作进程可以允许同时建立外部连接的数量
    worker_connections 1024;

    # on/off，默认on，多个Worker将以串行方式来处理，其中有一个Worker会被唤醒，其他的Worker继续保持休眠状态，防止"惊群效应"
    accept_mutex on;

    # 设置一个进程是否同时接受多个网络连接，默认为off
    multi_accept on;
}
```

### 3.3http全局块配置

- 文件引入
- MIME-TYPE定义
- 日志自定义
- 连接超时时间
- 单链接请求数上限

```shell
http {
}
```

### 3.4http中server块配置

- 虚拟主机(从用户角度看就是一台独立的硬件主机)相关配置
- 每一个server就是一个虚拟主机
- `每个http块可以包含多个server块`
- `每个server块可以包含多个location块`

```shell
# 表示该虚拟主机监听的端口
listen  80;
listen  192.168.0.1:80;  # 同时指定ip和端口

# 用于配置基于名称的虚拟主机，nginx的server_name的作用：https://blog.csdn.net/cheng_kohui/article/details/82930464
server_name www.test.site;  # 指定单个的域名
server_name *.test.site;  # 基于正则表达式的域名匹配


```

## a.其他

### a.1nginx如何做到热部署

所谓热部署，就是配置文件nginx.conf修改后，不需要stop Nginx，不需要中断请求，就能让配置文件生效！（nginx -s reload 重新加载/nginx -t检查配置/nginx -s stop）

### a.2配置静态资源服务器

1. 配置nginx.conf文件
2. 重新加载nginx

```shell
# gzip压缩打开可以让访问文件时候进行压缩传输，减少请求时间
# gzip_min_length只小于多少字节就不再压缩
# gzip_comp_level表示压缩级别
# gzip_types表示对哪些文件类型进行压缩
gzip on;
gzip_min_length 1;
gzip_comp_level 2;
gzip_types text/plain text/css application/javascript image/gif image/png;

server {
    listen 8080;
    server_name tonyliu.pub;
    access_log logs/tonyliu.access.log main;

    # / 表示所有的url请求
    location / {
        # static为静态文件目录
        alias static/;

        # 将文件夹及其目录结构信息提供出去,即可以共享静态资源的目录
        autoindex on;

        # 带宽有限，所有限制对大文件的访问速度，设置为100k/s到浏览器
        set $limit_rate 100k;
    }
}

server {
    listen 80;
    location / {
        alias /data/edgebox/local/register_tmplate;
        autoindex on;
        set $limit_rate 100k;
        }
}
```

### a.3搭建一个具备缓存功能的反向代理服务器

- `正向代理`：在客户端进行配置
- `反向代理`：在服务端配置，针对是动态内容，减轻上游服务器的压力

1. 配置上游服务器，一般上游服务器对公网不提供访问
2. 配置反向代理服务器

```shell
# 静态资源服务器
server {
    # 只让本机的进程来访问8080端口
    listen 127.0.0.1:8080;
}
```

```shell
# 反向代理服务器，对公网提供访问
http {

    # 配置缓存文件的目录
    proxy_cache_path /tmp/nginxcache levels=1:2 keys_zone=my_cache:10m max_size=10g inactive=60m use_tmp_path=off;

    server {
    listen 80;
    server_name tonyliu.pub;

    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forward_for;
        proxy_pass http://local;

        proxy_cache my_cache;
        proxy_cache_key $host$uri$is_args$args;
        proxy_cache_valid 200 304 302 ld;
        }
    }
}
```
