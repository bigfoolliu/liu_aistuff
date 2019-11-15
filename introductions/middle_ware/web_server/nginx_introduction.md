# nginx知识

<!-- TOC -->

- [nginx知识](#nginx知识)
    - [指令上下文](#指令上下文)
    - [nginx模块化体系(nginx core)](#nginx模块化体系nginx-core)
    - [Nginx如何做到热部署](#nginx如何做到热部署)
        - [nginx启动和关闭的方式](#nginx启动和关闭的方式)
    - [1.nginx主要应用场景](#1nginx主要应用场景)
    - [2.nginx的组成](#2nginx的组成)
    - [3.选择版本](#3选择版本)
    - [4.编译出自己的nginx](#4编译出自己的nginx)
    - [5.nginx的语法](#5nginx的语法)
    - [6.nginx命令行](#6nginx命令行)
    - [7.配置静态资源服务器](#7配置静态资源服务器)
    - [8.搭建一个具备缓存功能的反向代理服务器](#8搭建一个具备缓存功能的反向代理服务器)
    - [9.用GoAccess实现可视化并实时监控access日志](#9用goaccess实现可视化并实时监控access日志)
    - [10.ssl协议与https](#10ssl协议与https)

<!-- /TOC -->

[nginx教程](http://tengine.taobao.org/book/chapter_02.html)
[nginx.io(快速生成nginx的配置文件)](https://nginxconfig.io/)

nginx却是先加载一个主配置文件nginx.conf，在nginx.conf里再加载conf.d目录下的子配置文件（一般最少一个default.conf文件）

kill -HUP pid: 从容地重启nginx，我们一般用这个信号来重启nginx，或重新加载配置，因为是从容地重启，因此`服务是不中断的`。

## 指令上下文

- main: nginx在运行时与具体业务功能（比如http服务或者email服务代理）无关的一些参数，比如工作进程数，运行的身份等。
- http: 与提供http服务相关的一些配置参数。例如：是否使用keepalive啊，是否使用gzip进行压缩等。
- server: http服务上支持若干虚拟主机。每个虚拟主机一个对应的server配置项，配置项里面包含该虚拟主机相关的配置。在提供mail服务的代理时，也可以建立若干server.每个server通过监听的地址来区分。
- location: http服务中，某些特定的URL对应的一系列配置项。
- mail: 实现email相关的SMTP/IMAP/POP3代理时，共享的一些配置项（因为可能实现多个代理，工作在多个监听地址上）。

具体有哪些配置指令，以及这些配置指令可以出现在什么样的上下文中，需要参考nginx的使用文档.()

## nginx模块化体系(nginx core)

模块的分类
nginx的模块根据其功能基本上可以分为以下几种类型：

- event module: 搭建了独立于操作系统的事件处理机制的框架，及提供了各具体事件的处理。包括ngx_events_module， ngx_event_core_module和ngx_epoll_module等。nginx具体使用何种事件处理模块，这依赖于具体的操作系统和编译选项。
- phase handler: 此类型的模块也被直接称为handler模块。主要负责处理客户端请求并产生待响应内容，比如ngx_http_static_module模块，负责客户端的静态页面请求处理并将对应的磁盘文件准备为响应内容输出。
- output filter: 也称为filter模块，主要是负责对输出的内容进行处理，可以对输出进行修改。例如，可以实现对输出的所有html页面增加预定义的footbar一类的工作，或者对输出的图片的URL进行替换之类的工作。
- upstream: upstream模块实现反向代理的功能，将真正的请求转发到后端服务器上，并从后端服务器上读取响应，发回客户端。upstream模块是一种特殊的handler，只不过响应内容不是真正由自己产生的，而是从后端服务器上读取的。
- load-balancer: 负载均衡模块，实现特定的算法，在众多的后端服务器中，选择一个服务器出来作为某个请求的转发服务器。

## Nginx如何做到热部署

所谓热部署，就是配置文件nginx.conf修改后，不需要stop Nginx，不需要中断请求，就能让配置文件生效！（nginx -s reload 重新加载/nginx -t检查配置/nginx -s stop）

### nginx启动和关闭的方式

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

# 重启nginx
# 首先验证配置文件的准确性走
# 方式一，启动的时候加减
cd /usr/local/nginx/sbin/
nginx -s poload

# 方式二，
# 找到当前nginx的进程号，然后用-HUP参数推进重启
ps -ef | grep nginx
kill -HUP 2255
```

## 1.nginx主要应用场景

[nginx教程，核心知识100讲，youtobe地址](https://www.youtube.com/watch?v=uYPO4tJPAAY&list=PLSKUOdPqiSdtP6wNRo2vjHiWwcrC7MD8X&index=10)
[nginx官方帮助文档，配置文件等](http://nginx.org/en/docs/)

1. 静态资源服务，通过本地文件系统提供服务
2. 反向代理服务，缓存，负载均衡等
3. API服务

## 2.nginx的组成

1. nginx的二进制可执行文件，各模块编译出来的一个文件
2. nginx.conf配置文件，控制nginx的行为
3. access.log访问日志，记录每一条http请求信息
4. error.log错误日志，定位问题

## 3.选择版本

[开源版(偶数版本为稳定版)](http://nginx.org/)
[商业版](http://nginx.com)

## 4.编译出自己的nginx

1. 下载
2. 配置
3. 编译
4. 安装

```shell
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

## 5.nginx的语法

1. 配置文件由指令和指令块组成
2. 每条指令由;分号结尾，指令与参数间以空格分割
3. 指令块以{}大括号将多条指令结合
4. include语句允许组合多个配置文件以提升可读性
5. 使用#添加注释
6. 使用$使用变量
7. 部分指令的参数支持正则表达式

## 6.nginx命令行

- 格式: nginx -s reload
- 帮助：-h
- 使用指定的配置文件：-c
- 指定配置指令：-g
- 指定运行目录：-p
- 发送信号：-s
  
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

- 测试配置文件是否有语法错误：-t -T
- 打印版本信息和编译信息：-v -V

## 7.配置静态资源服务器

1. 配置nginx.conf文件
2. 重新加载nginx

```nginx
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

```shell
sbin/nginx -s reload
```

## 8.搭建一个具备缓存功能的反向代理服务器

```text
正向代理：在客户端进行配置。
反向代理：在服务端配置。
```

上面的nginx静态服务器作为上游服务，上游服务一般是业务比较麻烦，性能较差，所以可以配置多台，下游的反向代理服务器可以根据**负载均衡算法**来将请求发给不同的上游服务器，减轻上游服务器的压力。

- 反向代理针对是动态内容，减轻上游服务器的压力
- 缓存是针对一段静态内容（长时间不变），提高响应速度，可以设置缓存时间，即使该静态内容变化了，也不管

1. 配置上游服务器，一般上游服务器对公网不提供访问
2. 配置反向代理服务器

```nginx
# 静态资源服务器
server {
    # 只让本机的进程来访问8080端口
    listen 127.0.0.1:8080;
}
```

```nginx
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

## 9.用GoAccess实现可视化并实时监控access日志

pass

## 10.ssl协议与https

ssl: Secure Socket Layer.

CA机构颁发的证书：

- DV证书
- OV证书
- EV证书
