# nginx知识

<!-- vim-markdown-toc Marked -->

* [1.概述](#1.概述)
    - [1.1组成](#1.1组成)
    - [1.2应用场景](#1.2应用场景)
    - [1.3编译nginx](#1.3编译nginx)
* [2.nginx命令](#2.nginx命令)
    - [2.1nginx启动和关闭](#2.1nginx启动和关闭)
    - [2.2nginx操作命令](#2.2nginx操作命令)
* [3.nginx配置](#3.nginx配置)
    - [3.1配置介绍](#3.1配置介绍)
        + [3.1.1配置语法](#3.1.1配置语法)
        + [3.1.2配置结构](#3.1.2配置结构)
        + [3.1.3配置最佳实践](#3.1.3配置最佳实践)
    - [3.2全局块常用配置](#3.2全局块常用配置)
    - [3.3events块配置](#3.3events块配置)
    - [3.4http全局块配置](#3.4http全局块配置)
    - [3.5http中server块配置](#3.5http中server块配置)
* [4.常用配置](#4.常用配置)
    - [4.1典型配置](#4.1典型配置)
    - [4.2静态资源服务器](#4.2静态资源服务器)
    - [4.3反向代理服务器](#4.3反向代理服务器)
    - [4.4负载均衡服务器](#4.4负载均衡服务器)
    - [4.5配置动静分离](#4.5配置动静分离)
    - [4.6适配移动端](#4.6适配移动端)
    - [4.7配置HTTPS](#4.7配置https)
    - [4.8图片防盗链](#4.8图片防盗链)
    - [4.9请求过滤](#4.9请求过滤)
    - [4.10HTTP转发HTTPS](#4.10http转发https)
    - [4.11图片等缓存](#4.11图片等缓存)
* [a.其他](#a.其他)
    - [a.1nginx如何做到热部署](#a.1nginx如何做到热部署)

<!-- vim-markdown-toc -->

## 1.概述

### 1.1组成

- [nginx配置文件参数详解](https://www.cnblogs.com/airoot/p/12744901.html)
- [nginx教程](http://tengine.taobao.org/book/chapter_02.html)
- [nginx.io(快速生成nginx的配置文件)](https://nginxconfig.io/)
- [nginx中文文档](http://www.nginx.cn/doc/)
- [nginx英文文档](https://nginx.org/en/docs/)
- nginx是`先加载一个主配置文件nginx.conf`，`在nginx.conf里再加载conf.d目录下的子配置文件`

**组成:**

1. nginx的二进制可执行文件，各模块编译出来的一个文件
2. `nginx.conf`配置文件，控制nginx的行为
3. `access.log`访问日志，记录每一条http请求信息
4. error.log错误日志，定位问题


### 1.2应用场景

- [nginx教程，核心知识100讲，youtobe地址](https://www.youtube.com/watch?v=uYPO4tJPAAY&list=PLSKUOdPqiSdtP6wNRo2vjHiWwcrC7MD8X&index=10)
- [nginx官方帮助文档，配置文件等](http://nginx.org/en/docs/)

1. 静态资源服务，通过本地文件系统提供服务
2. 反向代理服务，缓存，负载均衡等
3. 动静分离，将动态页面和静态页面分开为不同的服务器，提高速度
4. API服务


### 1.3编译nginx

- [开源版(偶数版本为稳定版)](http://nginx.org/)
- [商业版](http://nginx.com)

```sh
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

kill -USR2 1314  # 向nginx的master进程发送信号,此时会生成新的nginx的master和worker进程
kill -WINCH 1314  # 向旧的nginx的master进程发送信号让其优雅退出
```

## 2.nginx命令

### 2.1nginx启动和关闭

```sh
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

```sh

nginx -s reload  # 重载配置文件，不停止原有服务
nginx -s quit  # 优雅的停止文件
nginx -s stop  # 立刻停止服务
nginx -s reopen  # 重新开始记录日志文件
```

## 3.nginx配置

### 3.1配置介绍

#### 3.1.1配置语法

1. 配置文件由指令和指令块组成
2. 每条`指令由;分号结尾`，指令与参数间以空格分割
3. 指令块以{}大括号将多条指令结合
4. include语句允许组合多个配置文件以提升可读性
5. 使用#添加注释
6. 使用`$`使用变量
7. 部分指令的参数支持正则表达式

#### 3.1.2配置结构

```sh
# nginx.conf 结构图可以这样概括：

main        # 全局配置，对全局生效
├── events  # 配置影响 Nginx 服务器或与用户的网络连接
├── http    # 配置代理，缓存，日志定义等绝大多数功能和第三方模块的配置
│   ├── upstream # 配置后端服务器具体地址，负载均衡配置不可或缺的部分
│   ├── server   # 配置虚拟主机的相关参数，一个 http 块中可以有多个 server 块
│   ├── server
│   │   ├── location  # server 块可以包含多个 location 块，location 指令用于匹配 uri
│   │   ├── location
│   │   └── ...
│   └── ...
└── ...
```

#### 3.1.3配置最佳实践

1. 为了使 Nginx 配置更易于维护，建议`为每个服务创建一个单独的配置文件`，存储在 /etc/nginx/conf.d 目录，根据需求可以创建任意多个独立的配置文件。
2. 独立的配置文件，建议遵循以下`命名约定 <服务>.conf`，比如域名是 tony.com，那么你的配置文件的应该是这样的 /etc/nginx/conf.d/tony.com.conf，如果部署多个服务，也可以在文件名中加上 Nginx 转发的端口号，比如 tony.com.8080.conf，如果是二级域名，建议也都加上 fe.tony.com.conf。
3. 常用的、`复用频率比较高的配置可以放到 /etc/nginx/snippets 文件夹，在 Nginx 的配置文件中需要用到的位置 include 进去`，以功能来命名，并在每个 snippet 配置文件的开头注释标明主要功能和引入位置，方便管理。比如之前的 gzip、cors 等常用配置，我都设置了 snippet。
4. Nginx `日志相关目录，内以 域名.type.log 命名`（比如 be.tony.com.access.log 和 be.tony.com.error.log ）位于 /var/log/nginx/ 目录中，为每个独立的服务配置不同的访问权限和错误日志文件，这样查找错误时，会更加方便快捷。

### 3.2全局块常用配置

- 配置`影响全局`的命令
- 包括nginx的用户组
- nginx进程pid存放路径
- 日志存放路径
- 允许生成worker process数量等

```sh
# 指定Nginx Worker进程运行用户，涉及文件访问权限
user root;
user wwwuser wwwgroup;

# 修改 Nginx 进程最大可打开文件数: https://blog.csdn.net/liupeifeng3514/article/details/79007079
# 操作系统启动多少个工作进程运行nginx
worker_processes auto;
worker_processes 4;

# 配置文件的包含，Nginx.conf include使用：https://blog.csdn.net/ruby113028/article/details/52461452
include /usr/local/nginx/conf/vhosts/*.conf;
```

### 3.3events块配置

- 涉及的指令主要影响`nginx服务器与用户的网络连接`

```sh
events {
    # 单个工作进程可以允许同时建立外部连接的数量
    worker_connections 1024;

    # on/off，默认on，多个Worker将以串行方式来处理，其中有一个Worker会被唤醒，其他的Worker继续保持休眠状态，防止"惊群效应"
    accept_mutex on;

    # 设置一个进程是否同时接受多个网络连接，默认为off
    multi_accept on;
}
```

### 3.4http全局块配置

- 文件引入
- MIME-TYPE定义
- 日志自定义
- 连接超时时间
- 单链接请求数上限

```sh
http {
}
```

### 3.5http中server块配置

- 虚拟主机(从用户角度看就是一台独立的硬件主机)相关配置
- 每一个server就是一个虚拟主机
- 每个http块可以包含`多个server块`
- 每个server块可以包含`多个location块`

```sh
# 表示该虚拟主机监听的端口
listen  80;
listen  192.168.0.1:80;  # 同时指定ip和端口

# 用于配置基于名称的虚拟主机，nginx的server_name的作用：https://blog.csdn.net/cheng_kohui/article/details/82930464
server_name www.test.site;  # 指定单个的域名
server_name *.test.site;  # 基于正则表达式的域名匹配
```

## 4.常用配置

### 4.1典型配置

```sh
user  nginx;                                # 运行用户，默认即是nginx，可以不进行设置
worker_processes  1;                        # Nginx 进程数，一般设置为和 CPU 核数一样
error_log  /var/log/nginx/error.log warn;   # Nginx 的错误日志存放目录
pid        /var/run/nginx.pid;              # Nginx 服务启动时的 pid 存放位置

events {
    use epoll;                  # 使用epoll的I/O模型(如果你不知道Nginx该使用哪种轮询方法，会自动选择一个最适合你操作系统的)
    worker_connections 1024;    # 每个进程允许最大并发数
}

http {   # 配置使用最频繁的部分，代理、缓存、日志定义等绝大多数功能和第三方模块的配置都在这里设置
    
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '   # 设置日志模式
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    access_log  /var/log/nginx/access.log  main;   # Nginx访问日志存放位置

    sendfile            on;   # 开启高效传输模式
    tcp_nopush          on;   # 减少网络报文段的数量
    tcp_nodelay         on;
    keepalive_timeout   65;   # 保持连接的时间，也叫超时时间，单位秒
    types_hash_max_size 2048;

    include             /etc/nginx/mime.types;      # 文件扩展名与类型映射表
    default_type        application/octet-stream;   # 默认文件类型

    include /etc/nginx/conf.d/*.conf;   # 加载子配置项
    
    server {
    	listen       80;            # 配置监听的端口
    	server_name  localhost;     # 配置的域名
    	
    	location / {
    		root   /usr/share/nginx/html;   # 网站根目录
    		index  index.html index.htm;    # 默认首页文件
    		deny 172.168.22.11;             # 禁止访问的ip地址，可以为all
    		allow 172.168.33.44;            # 允许访问的ip地址，可以为all
    	}
    	
    	error_page 500 502 503 504 /50x.html;   # 默认50x对应的访问页面
    	error_page 400 404 error.html;          # 同上
    }
}
```

### 4.2静态资源服务器

```sh
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

    charset utf-8;  # 防止中文文件名乱码
    
    location / {        # / 表示所有的url请求
        alias static/;  # static为静态文件目录

        autoindex               on;    # 将文件夹及其目录结构信息提供出去,即可以共享静态资源的目录
        autoindex_exact_size    off;   # on(默认)显示文件的确切大小，单位是byte；off显示文件大概大小，单位KB、MB、GB
        autoindex_localtime     off;   # off(默认)时显示的文件时间为GMT时间；on显示的文件时间为服务器时间

        set $limit_rate 100k;   # 带宽有限，所有限制对大文件的访问速度，设置为100k/s到浏览器
    }
}

server {
    listen 80;
    location / {
        alias /data/edgebox/local/register_template;
        autoindex on;
        set $limit_rate 100k;
        }
}
```

### 4.3反向代理服务器

- `正向代理`：在客户端进行配置
- `反向代理`：在服务端配置，针对是动态内容，减轻上游服务器的压力

1. 配置上游服务器，一般上游服务器对公网不提供访问
2. 配置反向代理服务器

```sh
# 静态资源服务器
server {
    # 只让本机的进程来访问8080端口
    listen 127.0.0.1:8080;
}
```

```sh
# 反向代理服务器，对公网提供访问
http {

    # 配置缓存文件的目录
    proxy_cache_path /tmp/nginxcache levels=1:2 keys_zone=my_cache:10m max_size=10g inactive=60m use_tmp_path=off;

    server {
    listen 80;
    server_name a.liu.com;

    location / {
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forward_for;
        proxy_pass b.liu.com;                                        # 将a.liu.com的请求全都代理到b.liu.com，可以绕过跨域问题

        proxy_cache my_cache;
        proxy_cache_key $host$uri$is_args$args;
        proxy_cache_valid 200 304 302 ld;
        }
    }
}
```

### 4.4负载均衡服务器

Nginx 提供了好几种分配方式，`默认为轮询`，就是轮流来。有以下几种分配方式：

- `轮询`，默认方式，每个请求按时间顺序逐一分配到不同的后端服务器，如果后端服务挂了，能自动剔除；
- `weight，权重分配`，指定轮询几率，权重越高，在被访问的概率越大，`用于后端服务器性能不均的情况`；
- `ip_hash`，每个请求按访问 IP 的 hash 结果分配，这样每个访客固定访问一个后端服务器，`可以解决动态网页 session 共享问题`,负载均衡每次请求都会重新定位到服务器集群中的某一个，那么已经登录某一个服务器的用户再重新定位到另一个服务器，其登录信息将会丢失，这样显然是不妥的；
- `fair（第三方）`，按后端服务器的响应时间分配，`响应时间短的优先分配，依赖第三方插件 nginx-upstream-fair`，需要先安装；


```sh
http {
  upstream myserver {
  	# ip_hash;                          # ip_hash 方式
    # fair;                             # fair 方式
    server 127.0.0.1:8081;              # 负载均衡目的服务地址
    server 127.0.0.1:8080;
    server 127.0.0.1:8082 weight=10;    # weight 方式，不写默认为 1
  }
 
  server {
    location / {
        proxy_pass http://myserver;
        proxy_connect_timeout 10;
    }
  }
}

```

### 4.5配置动静分离

动态和静态的请求分开。方式主要有两种:

1. 静态文件独立成单独的域名，放在独立的服务器上，是目前主流推崇的方案
2. 动态跟静态文件混合在一起发布， 通过 Nginx 配置来分开

```sh
# location 指定不同的后缀名实现不同的请求转发, 通过expires设置资源过期时间
# 发送请求，对比服务器该文件最后更新时间没有变化。则不会从服务器抓取，返回状态码 304，如果有修改，则直接从服务器重新下载，返回状态码 200。

server {
  # 配置动态资源
  location /www/ {
  	root /data/;
    index index.html index.htm;
  }
  
  # 配置静态资源
  location /image/ {
  	root /data/;
    autoindex on;
  }
}
```

### 4.6适配移动端

- 移动端适配可以使用前端自适应布局或者直接分开写通过`user-agent`来判断使用pc还是移动端

```sh
server {
  listen 80;
	server_name fe.tony.com;

	location / {
		root  /usr/share/nginx/html/pc;

        # 增加if语句判断用户请求的user-agent, 来指向不同的站点根路径
        if ($http_user_agent ~* '(Android|webOS|iPhone|iPod|BlackBerry)') {
            root /usr/share/nginx/html/mobile;
        }
	    index index.html;
	}
}
```

### 4.7配置HTTPS

- `申请服务器证书`，安装直接看所在云的操作指南即可
- 申请得到的压缩文件夹解压得到，把 xxx.crt 和 xxx.key 文件拷贝到服务器目录

```sh
server {
  listen 443 ssl http2 default_server;   # SSL 访问端口号为 443
  server_name tony.com;         # 填写绑定证书的域名

  ssl_certificate /etc/nginx/https/1_tony.com_bundle.crt;   # 证书文件地址
  ssl_certificate_key /etc/nginx/https/2_tony.com.key;      # 私钥文件地址
  ssl_session_timeout 10m;

  ssl_protocols TLSv1 TLSv1.1 TLSv1.2;                                  # 请按照以下协议配置
  ssl_ciphers ECDHE-RSA-AES128-GCM-SHA256:HIGH:!aNULL:!MD5:!RC4:!DHE;
  ssl_prefer_server_ciphers on;
  
  location / {
    root         /usr/share/nginx/html;
    index        index.html index.htm;

    # 可选配置
    add_header X-Frame-Options DENY;           # 减少点击劫持
    add_header X-Content-Type-Options nosniff; # 禁止服务器自动解析资源类型
    add_header X-Xss-Protection 1;             # 防XSS攻击
  }
}

```

### 4.8图片防盗链

```sh
server {
  listen       80;
  server_name  *.tony.com;
  
  # 图片防盗链
  location ~* \.(gif|jpg|jpeg|png|bmp|swf)$ {
    valid_referers none blocked 192.168.0.2;    # 只允许本机 IP 外链引用
    if ($invalid_referer){
      return 403;
    }
  }
}
```

### 4.9请求过滤

```sh
# 非指定请求全返回 403
if ( $request_method !~ ^(GET|POST|HEAD)$ ) {
  return 403;
}

location / {

  allow 192.168.0.2;    # IP访问限制（只允许IP是 192.168.0.2 机器访问）
  deny all;
  
  root   html;
  index  index.html index.htm;
}
```

### 4.10HTTP转发HTTPS

- 配置完 HTTPS 后，浏览器还是可以访问 HTTP 的地址 http://tony.com/ 的，可以做一个 301 跳转，把对应域名的 HTTP 请求重定向到 HTTPS 上

```sh
server {
    listen      80;
    server_name www.tony.com;

    # 单域名重定向
    if ($host = 'www.tony.com'){
        return 301 https://www.tony.com$request_uri;
    }

    # 全局非 https 协议时重定向
    if ($scheme != 'https') {
        return 301 https://$server_name$request_uri;
    }

    # 或者全部重定向
    return 301 https://$server_name$request_uri;

    # 以上配置选择自己需要的即可，不用全部加
}
```

### 4.11图片等缓存

- 由于图片、字体、音频、视频等静态文件在打包的时候通常会`增加了 hash，缓存可以设置的长一点`，`先设置强制缓存，再设置协商缓存`
- 如果存在`没有 hash 值的静态文件，建议不设置强制缓存`，仅通过协商缓存判断是否需要使用缓存。

```sh
# 图片缓存时间设置
location ~ .*\.(css|js|jpg|png|gif|swf|woff|woff2|eot|svg|ttf|otf|mp3|m4a|aac|txt)$ {
	expires 7d;    # 设置缓存日期为7days, 如果不希望缓存 expires -1;
}
```

## a.其他

### a.1nginx如何做到热部署

- 所谓`热部署`，就是配置文件nginx.conf修改后，不需要stop Nginx，不需要中断请求，就能让配置文件生效！
- `nginx -s reload` 重新加载/nginx -t检查配置/nginx -s stop）

