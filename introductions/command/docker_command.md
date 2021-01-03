# docker命令

<!-- vim-markdown-toc Marked -->

* [1.基础命令](#1.基础命令)
* [2.镜像操作](#2.镜像操作)
* [3.容器操作](#3.容器操作)
    - [3.1容器基础](#3.1容器基础)
    - [3.2容器通信](#3.2容器通信)
* [4.运行](#4.运行)
* [5.镜像构建](#5.镜像构建)
* [6.docker实例](#6.docker实例)
    - [6.1nginx](#6.1nginx)
    - [6.2mysql](#6.2mysql)
* [7.docker-compose命令](#7.docker-compose命令)

<!-- vim-markdown-toc -->

## 1.基础命令

```sh
# linux安装
# TODO:

# 基本信息
docker --version  # 查看docker版本及其他信息
docker-compose --version  # 查看docker-compose的版本
docker-machine --version  # 查看docker-machine的版本

docker version  # 查看版本
docker info  # 查看整个docker的信息
docker system df  # 查看镜像、容器、数据卷所占用的空间


# 启动服务
service docker restart  # 重启docker服务
service docker start  # 启动docker服务


# 清除所有未使用的容器，空的镜像，和未使用的网络
docker system prune

# 查看docker占据磁盘的情况(df 命令中的 overlay),-v查看细节
docker system df
docker system df -v

# 复制文件
docker cp container:/opt/file.txt /opt/local/
docker cp /opt/local/file.txt container:/opt/


# 现在的docker有了专门清理资源(container、image、网络)的命令。 docker 1.13 中增加了 docker system prune的命令，针对container、image可以使用docker container prune、docker image prune命令。

# 查看docker容器的日志
docker logs <container_id>

# 查看docker容器启动或者重启的时间
time docker start <container_id>
time docker restart <container_id>

# 进入一个docker的内部
sudo docker exec -it 775c7c9ee1e1 /bin/bash

# 进入容器之后查看容器运行的ip地址
cat /etc/hosts


# 列出所有的数据卷
docker volume ls
```

## 2.镜像操作

```sh
# 1.镜像获取
docker search <image name>  # 搜索可用的docker镜像
docker pull ubuntu:18.04  # 自动获取镜像
docker pull harbor.liuai.com/base/nginx-rtmp:x8664-cpu-0.1.0  # 从指定路径的远程获取镜像

# 从远程仓库获取镜像
sudo docker pull harbor.liuai.com/nginx-rtmp:x8664-cpu-0.1.0  # master从harbor上pull一个镜像
sudo docker pull registry.liuai.com:5000/nginx-rtmp:x8664-cpu-0.1.0

# 2.查看镜像信息
docker image ls  # 查看所有已经下载的镜像
docker history <image_name>  # 查看某个镜像的历史消息

# 3.镜像导入导出
docker save -o liu.tar tonyliu/ubuntu:V3  # 将镜像导出
docker load -i liu.tar  # 将镜像导入

# 4.镜像推送到仓库
docker push registry.liuai.com:5000/nginx-rtmp:x8664-cpu-0.1.0  # 将docker镜像推送至远端registry仓库
docker push harbor.liuai.com/base/nginx-rtmp:x8664-cpu-0.1.0  # push本地的docker镜像至harbor
docker commit -m "add python" -a "liu" 3c7c3f081b67 tonyliu/ubuntu:python  # 提交一个容器将其转化为一个镜像(带有信息-m 作者 -a 以及标签:python)
docker tag harbor.liuai.com/base/nginx-rtmp:x8664-cpu-0.1.0 registry.liuai.com:5000/nginx-rtmp:x8664-cpu-0.1.0  # 给docker镜像添加一个标签

# 5.删除镜像
docker rmi nginx  # 删除镜像
docker rmi $(docker images -q)  # 删除所有的镜像
docker image prune --force --all或者docker image prune -f -a  # 删除所有不使用的镜像

```

## 3.容器操作

### 3.1容器基础

```sh
# 1.查看容器信息
docker ps -a  # 查看所有运行的容器
docker ps -aq  # 列出所有的容器 ID
docker inspect 321  # 检查docker容器运行信息

# 2.启动/终止容器
docker stop webserver  # 停止名为webserver的容器
docker start webserver  # 启动名为webserver的容器
docker stop $(docker ps -aq)  # 停止所有的容器

# 3.删除容器
docker rm -f webserver  # 删除容器
sudo docker rm `sudo docker ps -a | grep Exited | head -2 | awk '{print $1}'`  # 批量删除已经Exited的容器(指定数量)
docker rm $(docker ps -aq)  # 删除所有的容器
docker container prune -f  # 删除所有停止的容器
sudo docker rmi `sudo docker images | grep nginx-rtmp | head -2 | awk '{print $3}'`  # 批量删除镜像(指定数量)


# 4.容器导入导出
docker export -o liu.tar CONTATINER  # 将容器导出, 其中可以通过-o来指定导出的文件名，CONTAINER为容器的NAMES
docker import liu.tar liu:tmp  # 将容器导入

# 5.进入容器
docker attach 123  # 进入正在运行的容器
```

### 3.2容器通信

```sh
# 查看某个容器的"长id"然后在本地与容器之间传输文件
docker inspect -f '{{.ID}}' hardcore_thompson
docker cp 本地文件路劲 <长id>:容器路径


# 检查bridge网络的详细配置,可以看到处于当前网络的容器及其ip
docker network inspect bridge

# 手动将容器加入某个bridge
docker network connect <network-name> <container-name>sdf

# 手动将容器从某个bridge断开
docker network disconnect <network-name> <container-name>
```

## 4.运行

```sh

docker run hello-world  # 测试从Docker Hub拉取一个实例程序并启动一个容器
docker run -it ubuntu bash  # 下载并运行ubuntu容器
docker run -d -p 80:80 --name webserver nginx  # 下载并运行nginx
docker run -it ubuntu:latest  # 当有多个版本时指定某一个版本


# --link格式: <name or id>:alias，alias是容器的别名
# 用来将容器mysql连接起来，是两个容器之间可以相互通信
docker run --name gocron --link mysql:db -p 5920:5920 -d ouqg/gocron

# --net=host绑定主机的ip
docker run --net=host registry.liuai.com:5000/iotedge/host-manager:0.2.26

# 以不执行run.sh的方式进入容器内部
docker run --entrypoint bash -it registry.liuai.com:5000/base/device-pipe-gstreamer:arm64v8-cpu-0.1.0

# 给容器挂载存储卷，挂载到容器的某个目录
# 前面的/var/www为宿主机上的绝对路径，/usr/share/nginx/html为容器上的绝对路径，ro指定只读挂载。 在本机上创建一个index.html,然后就可以直接通过浏览器访问了，修改index.html文件，刷新浏览器，可以马上看到文件的更新。
docker run --rm --name webserver -p 80:80 -v /var/www:/usr/share/nginx/html:ro -d nginx
docker run -it -v /usr/local/src/logs:/usr/local/src/logs test/base:1.0.0 /bin/bash
```

## 5.镜像构建

```sh
# 1. 使用Dockerfile来构建镜像
docker build -t tonyliu/ubuntu:V3 .  # 从当前目录的Dockerfile构建
docker build -f /path/Dockerfile  # 指定`Dockerfile`的文件位置并执行，构建一个image
docker build -t /path/my_app  # 指定image构建完成之后保存image的位置

# 2.从正在运行的容器中创建一个镜像,指定容器的id和新创建的容器的用户名称和镜像名称
sudo docker commit 132123 UserName/ImageName
```

## 6.docker实例

### 6.1nginx

```sh
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

### 6.2mysql

```sh
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


# 快速查询
docker run -p 3306:3306 --name=mysql01 --network=my-network  -v mysql:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=123456 -d mysql/mysql-server:5.7.24 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci


# 常见异常：外部客户端无法连接docker mysql,默认root用户的Host为local,需要将其设置为通配 %:
use mysql;
select Host from user where user='root';
update user set host = '%' where user ='root';
flush privileges;


# 在另一个容器中来连接mysql容器(容器间通信), 设置docker的network,可以运行不同的容器进行通信
# 1.列举所有的网络
docker network ls

# 2.创建一个network
docker network create my-custom-net

# 3.当创建和启动其他容器的时候指定network，my_app1容器就可以访问mysql
docker run --name=mysql1 --network=my-custom-net -d mysql/mysql-server
docker run --name=my_app1 --network=my-custom-net -d my_app

# 4.在my_app1容器的内部运行mysql1容器
docker exec -it my_app1 mysql1 --host=my_app1 --user=my_user --password
```

## 7.docker-compose命令

```sh
# 1.拉取镜像
docker-compose pull  # 拉取所有的镜像文件，但是不启动

# 2.列出所有的容器
docker-compose ps

# 3.验证和查看compose文件配置
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
