# docker使用简介

<!-- vim-markdown-toc Marked -->

* [1.概述](#1.概述)
    - [1.1端口映射](#1.1端口映射)
    - [1.2dockerfile使用](#1.2dockerfile使用)
    - [1.3docker内部时区问题](#1.3docker内部时区问题)
    - [1.4docker三剑客](#1.4docker三剑客)
* [2容器停止](#2容器停止)
* [3.docker构建自己的镜像](#3.docker构建自己的镜像)
    - [3.1使用makefile](#3.1使用makefile)
    - [3.2在运行中的容器构建](#3.2在运行中的容器构建)
    - [3.3docker镜像托管到docker hub](#3.3docker镜像托管到docker-hub)
    - [3.4docker自建仓库](#3.4docker自建仓库)
* [4.docker容器间通信](#4.docker容器间通信)
    - [4.1容器间通信方式](#4.1容器间通信方式)
    - [4.2docker网络驱动模型](#4.2docker网络驱动模型)
    - [4.3不同容器直接的互连](#4.3不同容器直接的互连)
* [5.docker Compose介绍](#5.docker-compose介绍)
    - [5.1常用命令](#5.1常用命令)
    - [5.2docker-compose.yml文件构建](#5.2docker-compose.yml文件构建)
* [6.docker Machine介绍](#6.docker-machine介绍)
* [7.docker Swarm介绍](#7.docker-swarm介绍)
* [8.python操作docker](#8.python操作docker)
    - [8.1介绍资料](#8.1介绍资料)
* [9.读书笔记](#9.读书笔记)

<!-- vim-markdown-toc -->

## 1.概述

- `镜像(Image)`
- `容器`(Container, [docker容器文件系统](http://guide.daocloud.io/dcs/docker-9153976.html))
- `仓库(Repository)`
- 镜像（Image）和容器（Container）的关系，就像是面向对象程序设计中的 类 和 实例 一样，镜像是静态的定义，容器是镜像运行时的实体。容器可以被创建、启动、停止、删除、暂停等。容器的实质是进程。
- Docker 运行容器前需要本地存在对应的镜像，如果本地不存在该镜像，Docker 会从镜像仓库下载该镜像。

### 1.1端口映射

`docker容器在启动的时候，如果不指定端口映射参数，在容器外部是无法通过网络来访问容器内的网络应用和服务的。`

端口映射使用：

- -p：指定要映射的端口,一个指定端口绑定一个容器
- -P：将容器内开放的网络端口随机映射到宿主机的一个端口

```sh
# 格式
ip:hostport:containerport #指定ip、指定宿主机port、指定容器port
ip::containerport #指定ip、未指定宿主机port（随机）、指定容器port
hostport:containerport #未指定ip、指定宿主机port、指定容器port
```

端口映射的5种方法：

1. 将容器暴露的所有端口都随随机映射到宿主机（`不推荐使用`）,`docker run -P it ubuntu /bin/bash`
2. 将容器的指定端口随机映射到宿主机一个端口,`docker run -P 80 -it ubuntu /bin/bash`
3. 将容器的指定端口指定到宿主机的指定端口(:前面是宿主机端口，后面是容器端口),`docker run -p 8000:80 -it ubuntu /bin/bash`
4. 将容器ip和端口随机映射到宿主机,`docker run -P 192.168.0.100::80 -it ubuntu /bin/bash`(将容器的ip和80端口随机映射到宿主机端口)
5. 将容器ip和端口指定映射到宿主机,`docker run -p 192.168.0.100:8000:80 -it ubuntu /bin/bash`(将容器的ip和80端口映射到宿主机8000端口)

### 1.2dockerfile使用

- [在windows的subsystem(ubuntu上)安装docker client](https://medium.com/@sebagomez/installing-the-docker-client-on-ubuntus-windows-subsystem-for-linux-612b392a44c4)
- [Dockerfile详解](http://seanlook.com/2014/11/17/dockerfile-introduction/)

### 1.3docker内部时区问题

- [docker修改默认时区](https://blog.csdn.net/qq_34924407/article/details/82057080)

### 1.4docker三剑客

1. `docker Machine`,用来在不同的平台快速安装Docker
2. `docker Swarm`,帮助Docker在不同的集群中运转
3. `docker Compose`,帮助用户运行容器组

## 2容器停止

- [如何优雅的终止docker，docker stop和docker kill的区别](https://xiaozhou.net/stop-docker-container-gracefully-2016-09-08.html)
- 在docker stop命令执行的时候，会先向容器中`PID为1的进程`发送系统信号SIGTERM，然后等待容器中的应用程序终止执行，如果等待时间达到设定的超时时间，或者默认的10秒，会继续发送SIGKILL的系统信号强行kill掉进程。

## 3.docker构建自己的镜像

### 3.1使用makefile

`Dockerfile`

一些常见的命令及其含义

- FROM ubuntu:14.04 ：设置基础镜像，此时会使用基础镜像 ubuntu:14.04 的所有镜像层。
- ADD run.sh / ：将 Dockerfile 所在目录的文件 run.sh 加至镜像的根目录，此时新一层的镜像只有一项内容，即根目录下的 run.sh 。
- VOLUME /data ：设定镜像的 VOLUME, 此 VOLUME 在容器内部的路径为 /data。需要注意的是，此时并未在新一层的镜像中添加任何文件，但更新了镜像的 json 文件，以便通过此镜像启动容器时获取这方面的信息。
- CMD ["./run.sh"] ：设置镜像的默认执行入口，此命令同样不会在新建镜像中添加任何文件，仅仅在上一层镜像 json 文件的基础上更新新建镜像的 json 文件。

- [官方文档](https://docs.docker.com/engine/reference/builder/)
- [多个FROM指令的意义](https://blog.csdn.net/Michaelwubo/article/details/91872076)

### 3.2在运行中的容器构建

1. 运行一个下载的容器
2. 进入容器，安装依赖以及相关操作
3. 退回宿主机的终端,使用`ctrl+P，然后ctrl+Q`,不中断容器的退出
4. 从一个正在运行的容器中创建镜像

### 3.3docker镜像托管到docker hub

1. docker hub上面注册一个账号, 然后创建自己的仓库
2. 本地使用`docker login`登录docker hub
3. 本地给镜像打标签， `docker tag tag1 liu/image1`
4. 将本地打包的docker镜像推送到远程，`docker push liu/image1`
5. 检查是否推送成功，`docker inspect liu/image1`，或者直接登录docker hub查看

### 3.4docker自建仓库

- 使用Registry软件

```sh
# 1.拉取registry的镜像
docker pull registry

# 2.运行registry容器
# Registry服务默认会将上传的镜像保存在容器的/var/lib/registry，将主机的/opt/registry目录挂载到该目录，即可实现将镜像保存到主机的/opt/registry目录了 
docker run -d -v /opt/registry:/var/lib/registry -p 5000:5000 --restart=always --name registry registry:latest

# 3.可以访问
```

## 4.docker容器间通信

- [容器间通信](https://juejin.im/post/5ce26cb9f265da1bcd37aa7c)

### 4.1容器间通信方式

如果想要外界网络访问docker容器时，需要在docker容器启动时加上参数'-p [主机端口]:[容器端口]'进行端口映射，原理也是通过修改iptables规则将访问[主机端口]的数据转发到docker容器的[容器端口]中。

媒介区分：

1. volume共享通信
2. 网络通信

通信范围区分：

1. 同主机通信
2. 跨主机通信

### 4.2docker网络驱动模型

Docker的网络驱动模型分类：

- `bridge`：Docker中默认的网络驱动模型，在启动容器时如果不指定则默认为此驱动类型；
- `host`：打破Docker容器与宿主机之间的网络隔离，直接使用宿主机的网络环境，该模型仅适用于Docker17.6及以上版本;
- `overlay`：可以连接多个docker守护进程或者满足集群服务之间的通信；适用于不同宿主机上的docker容器之间的通信；
- `macvlan`：可以为docker容器分配MAC地址，使其像真实的物理机一样运行；
- `none`：即禁用了网络驱动，需要自己手动自定义网络驱动配置；
- `plugins`：使用第三方网络驱动插件；

### 4.3不同容器直接的互连

1. 在启动docker容器时加入--link参数，但是目前已经被废弃，废弃的主要原因是需要在连接的两个容器上都创建--link选项，当互连的容器数量较多时，操作的复杂度会显著增加；
2. 启动docker容器后进入容器并修改/etc/host配置文件，缺点是手动配置较为繁杂；
3. `用户自定义bridge网桥，这是目前解决此类问题的主要方法`；

`不同的容器加入同一个bridge中之后，可以在一个容器中直接ping`

## 5.docker Compose介绍

- [官方文档](https://docs.docker.com/compose/)
- 对多个容器进行管理，是一个用于定义和运行多容器docker的应用程序工具。

### 5.1常用命令

- [docker-compose命令详解](https://blog.csdn.net/wanghailong041/article/details/52162293)

### 5.2docker-compose.yml文件构建

- [参考资料](https://www.jianshu.com/p/658911a8cff3)
- [掘金:docker compose入门指南](https://juejin.im/post/6886018425353682951)

```yml
services:
 mysql:
   image: mysql:latest
   ports:
     - '3306:3306'
   restart: always
   environment:
     MYSQL_ROOT_PASSWORD: '123456'

 webapp:
   build: .
   container_name: webapp
   restart: always
   depends_on:
     - 'mysql'
   environment:
     NODE_ENV: 'production'
   ports:
     - '80:8080'
```

## 6.docker Machine介绍

## 7.docker Swarm介绍

## 8.python操作docker

### 8.1介绍资料

- [python操作docker](https://cloud.tencent.com/developer/article/1044431)

## 9.读书笔记

- [docker实践读书笔记](../books/../../books/docker实践/docker_practice.md)
