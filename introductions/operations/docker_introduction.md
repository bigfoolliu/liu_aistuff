# docker使用简介

<!-- vim-markdown-toc Marked -->

* [1.基本概念](#1.基本概念)
        * [1.1端口映射](#1.1端口映射)
        * [1.2dockerfile使用](#1.2dockerfile使用)
        * [1.3docker内部时区问题](#1.3docker内部时区问题)
        * [1.4docker三剑客](#1.4docker三剑客)
* [2.基本命令](#2.基本命令)
        * [2.1常用命令](#2.1常用命令)
        * [2.2命令使用示例](#2.2命令使用示例)
                * [2.2.1docker运行nginx](#2.2.1docker运行nginx)
                * [2.2.2docker运行ngix-rtmp](#2.2.2docker运行ngix-rtmp)
        * [2.3容器停止](#2.3容器停止)
* [3.docker构建自己的镜像](#3.docker构建自己的镜像)
        * [3.1使用makefile](#3.1使用makefile)
        * [3.2在运行中的容器构建](#3.2在运行中的容器构建)
        * [3.3在linux中部署mysql](#3.3在linux中部署mysql)
                * [3.3.1常规部署语句](#3.3.1常规部署语句)
                * [3.3.2一步到位语句](#3.3.2一步到位语句)
                * [3.3.3常见异常](#3.3.3常见异常)
                * [3.3.4在另一个容器中来连接mysql容器(容器间通信)](#3.3.4在另一个容器中来连接mysql容器(容器间通信))
                * [3.3.5mysql数据库容器数据持久化](#3.3.5mysql数据库容器数据持久化)
* [4.docker容器间通信](#4.docker容器间通信)
        * [4.1容器间通信方式](#4.1容器间通信方式)
        * [4.2docker网络驱动模型](#4.2docker网络驱动模型)
        * [4.3不同容器直接的互连](#4.3不同容器直接的互连)
* [5.docker Compose介绍](#5.docker-compose介绍)
        * [5.1常用命令](#5.1常用命令)
        * [5.2docker-compose.yml文件构建](#5.2docker-compose.yml文件构建)
* [6.docker Machine介绍](#6.docker-machine介绍)
* [7.docker Swarm介绍](#7.docker-swarm介绍)
* [8.python操作docker](#8.python操作docker)
        * [8.1介绍资料](#8.1介绍资料)
* [9.读书笔记](#9.读书笔记)

<!-- vim-markdown-toc -->

## 1.基本概念

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

```shell
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

[在windows的subsystem(ubuntu上)安装docker client](https://medium.com/@sebagomez/installing-the-docker-client-on-ubuntus-windows-subsystem-for-linux-612b392a44c4)
[Dockerfile详解](http://seanlook.com/2014/11/17/dockerfile-introduction/)

### 1.3docker内部时区问题

[docker修改默认时区](https://blog.csdn.net/qq_34924407/article/details/82057080)

### 1.4docker三剑客

1. `docker Machine`,用来在不同的平台快速安装Docker
2. `docker Swarm`,帮助Docker在不同的集群中运转
3. `docker Compose`,帮助用户运行容器组

## 2.基本命令

### 2.1常用命令

```shell
service docker restart  # 重启docker服务

docker --version  # 查看docer版本及其他信息
docker-compose --version  # 查看docker-compose的版本
docker-machine --version  # 查看docker-machine的版本

docker ps -a  # 查看所有运行的容器
docker version  # 查看版本
docker info  # 查看整个docker的信息
docker system df  # 查看镜像、容器、数据卷所占用的空间
docker image ls  # 查看所有已经下载的镜像

docker run hello-world  # 测试从Docker Hub拉取一个实例程序并启动一个容器
docker run -it ubuntu bash  # 下载并运行ubuntu容器
docker run -d -p 80:80 --name webserver nginx  # 下载并运行nginx
docker run -it ubuntu:latest  # 当有多个版本时指定某一个版本

docker stop webserver  # 停止名为webserver的容器
docker start webserver  # 启动名为webserver的容器

docker rm -f webserver  # 删除容器
docker rmi nginx  # 删除镜像

docker search <image name>  # 搜索可用的docker镜像

docker pull ubuntu:18.04  # 自动获取镜像
docker pull harbor.jiangxingai.com/base/nginx-rtmp:x8664-cpu-0.1.0  # 从指定路径的远程获取镜像

# 提交一个容器将其转化为一个镜像(带有信息-m 作者 -a 以及标签:python)
docker commit -m "add python" -a "liu" 3c7c3f081b67 tonyliu/ubuntu:python

# 将容器导出
docker export -o liu.tar CONTATINER  # 其中可以通过-o来指定导出的文件名，CONTAINER为容器的NAMES

# 将容器导入
docker import liu.tar liu:tmp

# 将镜像导出
docker save -o liu.tar tonyliu/ubuntu:V3
# 将镜像导入
docker load -i liu.tar

# 进入一个docker的内部
sudo docker exec -it 775c7c9ee1e1 /bin/bash

# 进入容器之后查看容器运行的ip地址
cat /etc/hosts

# 以不执行run.sh的方式进入容器内部
docker run --entrypoint bash -it registry.jiangxingai.com:5000/base/device-pipe-gstreamer:arm64v8-cpu-0.1.0

# 使用Dockerfile来构建镜像
docker build -t tonyliu/ubuntu:V3 .

# 查看某个容器的"长id"然后在本地与容器之间传输文件
docker inspect -f '{{.ID}}' hardcore_thompson
docker cp 本地文件路劲 <长id>:容器路径

# 查看某个镜像的历史消息
docker history <image_name>

# 给容器挂载存储卷，挂载到容器的某个目录
# 前面的/var/www为宿主机上的绝对路径，/usr/share/nginx/html为容器上的绝对路径，ro指定只读挂载。 在本机上创建一个index.html,然后就可以直接通过浏览器访问了，修改index.html文件，刷新浏览器，可以马上看到文件的更新。
docker run --rm --name webserver -p 80:80 -v /var/www:/usr/share/nginx/html:ro -d nginx
docker run -it -v /usr/local/src/logs:/usr/local/src/logs test/base:1.0.0 /bin/bash

# 列出所有的数据卷
docker volume ls

# push本地的docker镜像至harbor
docker push harbor.jiangxingai.com/base/nginx-rtmp:x8664-cpu-0.1.0

# master从harbor上pull一个镜像
sudo docker pull harbor.jiangxingai.com/nginx-rtmp:x8664-cpu-0.1.0
sudo docker pull registry.jiangxingai.com:5000/nginx-rtmp:x8664-cpu-0.1.0

# 给docker镜像添加一个标签
docker tag harbor.jiangxingai.com/base/nginx-rtmp:x8664-cpu-0.1.0 registry.jiangxingai.com:5000/nginx-rtmp:x8664-cpu-0.1.0

# 将docker镜像推送至远端registry仓库
docker push registry.jiangxingai.com:5000/nginx-rtmp:x8664-cpu-0.1.0

# 批量删除已经Exited的容器(指定数量)
sudo docker rm `sudo docker ps -a | grep Exited | head -2 | awk '{print $1}'`

# 批量删除镜像(指定数量)
sudo docker rmi `sudo docker images | grep nginx-rtmp | head -2 | awk '{print $3}'`

# 列出所有的容器 ID
docker ps -aq

# 停止所有的容器
docker stop $(docker ps -aq)

# 删除所有的容器
docker rm $(docker ps -aq)

# 删除所有的镜像
docker rmi $(docker images -q)

# 复制文件
docker cp mycontainer:/opt/file.txt /opt/local/
docker cp /opt/local/file.txt mycontainer:/opt/

# 删除所有不使用的镜像
docker image prune --force --all或者docker image prune -f -a

# 删除所有停止的容器
docker container prune -f

# 清除所有未使用的容器，空的镜像，和未使用的网络
docker system prune

# 查看docker占据磁盘的情况(df 命令中的 overlay),-v查看细节
docker system df
docker system df -v

# 更新: @snakeliwei 的提醒， 现在的docker有了专门清理资源(container、image、网络)的命令。 docker 1.13 中增加了 docker system prune的命令，针对container、image可以使用docker container prune、docker image prune命令。

# 查看docker容器的日志
docker logs <container_id>

# 查看docker容器启动或者重启的时间
time docker start <container_id>
time docker restart <container_id>

# 检查docker容器运行信息
docker inspect 321

# 进入正在运行的容器
docker attach 123

# --link格式: <name or id>:alias，alias是容器的别名
# 用来将容器mysql连接起来，是两个容器之间可以相互通信
docker run --name gocron --link mysql:db -p 5920:5920 -d ouqg/gocron

# --net=host绑定主机的ip
docker run --net=host registry.jiangxingai.com:5000/iotedge/host-manager:0.2.26
```

### 2.2命令使用示例

#### 2.2.1docker运行nginx

```shell
docker run \
  --name myNginx \
  -d -p 80:80 \
  -v /usr/docker/myNginx/html:/usr/share/nginx/html \
  -v /etc/docker/myNginx/nginx.conf:/etc/nginx/nginx.conf:ro \
  -v /etc/docker/myNginx/conf.d:/etc/nginx/conf.d \
  nginx

# 挂载宿主机的目录到docker下是为了可以共享宿主机的文件。
# （1）第一个“-v”，是项目位置，把项目放到挂载到的目录下即可；
# （2）第二个“-v”，是挂载的主配置文件"nginx.conf"，注意"nginx.conf"文件内有一行"include /etc/nginx/conf.d/*.conf;"，这个include指向了子配置文件的路径，此处注意include后所跟的路径一定不要出错。
# （3）第三个“-v”，把docker内子配置文件的路径也挂载了出来，注意要与（2）中include指向路径一致
# （4）重点强调一下，nginx.conf是挂载了一个文件（docker是不推荐这样用的），conf.d挂载的是一个目录
```

#### 2.2.2docker运行ngix-rtmp

```shell
# 前面的/data/edgebox/remote/nginx/rtmp为master机器上的位置，/data/rtmp为docker里面的位置，开启nginx需要指定端口
docker run -v /data/edgebox/remote/nginx/rtmp:/data/rtmp -p 1935:1935 registry.jiangxingai.com:5000/nginx-rtmp:x8664-cpu-0.1.0


docker run --name edgebox-rtmp-server -p 1935:1935 -p 8080:8080 -d --restart unless-stopped registry.jiangxingai.com:5000/nginx-rtmp:arm64v8_cpu_latest

docker run --name edgebox-rtmp-server -v /data/edgebox/remote/nginx/rtmp:/data/rtmp -p 1935:1935 -p 8080:8080 -d --restart unless-stopped registry.jiangxingai.com:5000/base/nginx-rtmp:x8664-cpu-0.1.0 pull
```

### 2.3容器停止

[如何优雅的终止docker，docker stop和docker kill的区别](https://xiaozhou.net/stop-docker-container-gracefully-2016-09-08.html)
在docker stop命令执行的时候，会先向容器中`PID为1的进程`发送系统信号SIGTERM，然后等待容器中的应用程序终止执行，如果等待时间达到设定的超时时间，或者默认的10秒，会继续发送SIGKILL的系统信号强行kill掉进程。

## 3.docker构建自己的镜像

### 3.1使用makefile

`Dockerfile`

一些常见的命令及其含义

- FROM ubuntu:14.04 ：设置基础镜像，此时会使用基础镜像 ubuntu:14.04 的所有镜像层。
- ADD run.sh / ：将 Dockerfile 所在目录的文件 run.sh 加至镜像的根目录，此时新一层的镜像只有一项内容，即根目录下的 run.sh 。
- VOLUME /data ：设定镜像的 VOLUME, 此 VOLUME 在容器内部的路径为 /data。需要注意的是，此时并未在新一层的镜像中添加任何文件，但更新了镜像的 json 文件，以便通过此镜像启动容器时获取这方面的信息。
- CMD ["./run.sh"] ：设置镜像的默认执行入口，此命令同样不会在新建镜像中添加任何文件，仅仅在上一层镜像 json 文件的基础上更新新建镜像的 json 文件。

[官方文档](https://docs.docker.com/engine/reference/builder/)
[多个FROM指令的意义](https://blog.csdn.net/Michaelwubo/article/details/91872076)

```shell
docker build -f /path/Dockerfile  # 指定`Dockerfile`的文件位置并执行，构建一个image
docker build -t /path/myapp  # 指定image构建完成之后保存image的位置
```

### 3.2在运行中的容器构建

1. 运行一个下载的容器
2. 进入容器，安装依赖以及相关操作
3. 退回宿主机的终端,使用`ctrl+P，然后ctrl+Q`,不中断容器的退出
4. 从一个正在运行的容器中创建镜像

```shell
# 从正在运行的容器中创建一个镜像,指定容器的id和新创建的容器的用户名称和镜像名称
sudo docker commit 132123 UserName/ImageName
```

### 3.3在linux中部署mysql

#### 3.3.1常规部署语句

```shell
# 1.拉取指定版本的镜像
docker pull mysql/mysql-server:5.7.24

# 2.开启一个mysql容器实例,-d选项让容器在背景运行
docker run --name=mysql1 -d mysql/mysql-server:5.7.24

# 3.查看（监控）容器的输出
docker logs mysql1

# 4.容器初始化完成之后，就会为root用户生成一个随机密码，使用该命令查看生成的密码
docker logs mysql1 2>&1 | grep GENERATED

# 5.通过mysql的容器在容器内部创建一个mysql客户端,输入密码时首先需要上面生成的随机密码
docker exec -it mysql1 mysql -uroot -p

# 6.首先需要更改root用户的密码
mysql> ALTER USER 'root'@'localhost' IDENTIFIED BY 'password';

# 进入mysql1容器的bash
docker exec -it mysql1 bash
```

#### 3.3.2一步到位语句

```shell
docker run -p 3306:3306 --name=mysql01 --network=my-network  -v mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql/mysql-server:5.7.24 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
```

#### 3.3.3常见异常

`外部客户端无法连接docker mysql,默认root用户的Host为local,需要将其设置为通配 %`:

```mysql
use mysql;
select Host from user where user='root';
update user set host = '%' where user ='root';
flush privileges;
```

#### 3.3.4在另一个容器中来连接mysql容器(容器间通信)

设置docker的network,可以运行不同的容器进行通信

```shell
# 列举所有的网络
docker network ls
# 创建一个network
docker network create my-custom-net

# 当创建和启动其他容器的时候指定network，myapp1容器就可以访问mysql
docker run --name=mysql1 --network=my-custom-net -d mysql/mysql-server
docker run --name=myapp1 --network=my-custom-net -d myapp

# 在myapp1容器的内部运行mysql1容器
docker exec -it myapp1 mysql1 --host=myapp1 --user=myuser --password
```

#### 3.3.5mysql数据库容器数据持久化

将宿主机的目录加载为容器的数据卷来存储数据库文件。

```shell
```

## 4.docker容器间通信

[容器间通信](https://juejin.im/post/5ce26cb9f265da1bcd37aa7c)

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

```shell
# 检查bridge网络的详细配置,可以看到处于当前网络的容器及其ip
docker network inspect bridge
```

### 4.3不同容器直接的互连

1. 在启动docker容器时加入--link参数，但是目前已经被废弃，废弃的主要原因是需要在连接的两个容器上都创建--link选项，当互连的容器数量较多时，操作的复杂度会显著增加；
2. 启动docker容器后进入容器并修改/etc/host配置文件，缺点是手动配置较为繁杂；
3. `用户自定义bridge网桥，这是目前解决此类问题的主要方法`；

```shell
# 手动将容器加入某个bridge
docker network connect <network-name> <container-name>sdf

# 手动将容器从某个bridge断开
docker network disconnect <network-name> <container-name>
```

`不同的容器加入同一个bridge中之后，可以在一个容器中直接ping`

## 5.docker Compose介绍

[官方文档](https://docs.docker.com/compose/)
对多个容器进行管理，是一个用于定义和运行多容器docker的应用程序工具。

### 5.1常用命令

[docker-compose命令详解](https://blog.csdn.net/wanghailong041/article/details/52162293)

```shell
# 拉取所有的镜像文件，但是不启动
docker-compose pull

# 列出所有的容器
docker-compose ps

# 验证和查看compose文件配置
docker-compose config
docker-compose config --services

# 查看服务日志输出
docker-compose logs

# 修改dockerfile或者docker-compose时，构建或者重新构建服务,重建镜像
docker-compose build

# 启动指定服务已经存在的容器
docker-compose start
docker-compose start nginx
docker-compose restart  # 重新启动所有的容器

# 停止已经已经运行服务的容器
docker-compose stop nginx

# 删除所有compose服务
docker-compose rm
docker-compose rm nginx  # 删除指定服务的容器

# 构建，启动容器
docker-compose up
docker-compose up -d  # 以守护进程的方式启动

# 杀死容器
docker-compose kill
docker-compose kill -s SIGINT  # 发送SIGKILL信号强制停止服务容器
```

### 5.2docker-compose.yml文件构建

[参考资料](https://www.jianshu.com/p/658911a8cff3)

## 6.docker Machine介绍

## 7.docker Swarm介绍

## 8.python操作docker

### 8.1介绍资料

[python操作docker](https://cloud.tencent.com/developer/article/1044431)

## 9.读书笔记

[docker实践读书笔记](../books/../../books/docker实践/docker_practice.md)
