# docker practice读书笔记

<!-- TOC -->

- [docker practice读书笔记](#docker-practice%e8%af%bb%e4%b9%a6%e7%ac%94%e8%ae%b0)
  - [1.容器](#1%e5%ae%b9%e5%99%a8)
  - [2.镜像](#2%e9%95%9c%e5%83%8f)
  - [dockerfile](#dockerfile)
    - [dockerfile参考](#dockerfile%e5%8f%82%e8%80%83)
    - [dockerfile相关命令](#dockerfile%e7%9b%b8%e5%85%b3%e5%91%bd%e4%bb%a4)
    - [dockerfile多阶段构建](#dockerfile%e5%a4%9a%e9%98%b6%e6%ae%b5%e6%9e%84%e5%bb%ba)
  - [命令](#%e5%91%bd%e4%bb%a4)
  - [搭建私人docker registry仓库](#%e6%90%ad%e5%bb%ba%e7%a7%81%e4%ba%badocker-registry%e4%bb%93%e5%ba%93)
  - [docker网络](#docker%e7%bd%91%e7%bb%9c)

<!-- /TOC -->

## 1.容器

- 容器的本质是进程
- 每一个容器运行时候，以镜像为`基础层`，在其上创建一个当前层的`存储层`
- 最佳实践：容器不应该向存储层写入任何内容，容器存储层保持无状态化，所有的文件写入操作，都应该使用`数据卷`，或者`绑定宿主目录`
- 容器的应用都应该以前台执行，容器没有后台服务的概念

```shell
# 将容器快照导出为本地文件
docker export 1233 > ubuntun.tar

# 将容器快照文件导入为镜像
cat ubutun.tar | docker import - test/ubuntu:1.0
```

## 2.镜像

- 镜像唯一的标识为ID和摘要

```shell
# 配合删除镜像,删除所有的redis的镜像
docker image rm $(docker image ls -q redis)

# 删除所有在mongo:3.2版本之前的镜像
docker image rm $(docker image ls -q -f before=mongo:3.2)

# 查看容器的存储层的变化
docker diff redis

# 将容器保存为镜像
docker commit \
    --author "tony" \
    --message "修改了首页" \
    webserver \
    nginx:v2

# 查看镜像的历史记录
docker history nginx:v2
```

## dockerfile

### dockerfile参考

[dockerfile官方文档](https://docs.docker.com/engine/reference/builder/)
[dockerfile最佳实践](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)

### dockerfile相关命令

- `FROM`: 指定基础镜像，特别注意有一个空白镜像`scratch`,直接将可执行文件复制到镜像里面，如GO语言开发编译后的程序
- `RUN`: 执行命令行的命令，每一个RUN都是启动一个容器，执行命令，然后提交存储层的文件变更
- `COPY`: 复制文件，COPY --chown=1 files* / ,注意此时的文件的元数据，包括读写等权限都会保存
- `ADD`: COPY命令的加强版，可以下载一个连接，但是`不推荐使用`
- `CMD`: 容器启动命令，用于指定默认的容器主进程的启动命令,`docker run加镜像名，镜像之后接的命令会替换CMD的默认值`
- `ENTRYPOINT`: 和CMD一样，都是指定容器启动程序以及参数，比CMD略繁琐
  - 相对CMD,可以让镜像像命令一样使用，`docker run镜像之后接的命令`
  - 可以在应用运行之前做些准备工作
- `ENV`: 设置环境变量
- `ARG`: 设置环境变量，但是之后容器运行的时候不会使用这些变量
- `VOLUME`: 定义匿名卷，这样在运行时候就不必挂载
- `EXPOSE`：声明运行时候容器提供的服务端口，只是声明，当运行使用随机端口映射时候，会自动映射该端口，区别于`-p <宿主端口>:<容器端口>`
- `WORKDIR`：指定工作目录，其之后各层的工作目录都是这个目录
- `USER`：指定当前用户，以root执行的脚本，不要使用sudo，建议使用`[gosu](https://github.com/tianon/gosu)`
- `HEALTHCHECK`：健康检查
- `ONBUILD`：其后面的命令，RUN,COPY等在当前镜像构建的时候不会被执行，只有以当前镜像为基础镜像去构建下一级镜像的时候才会被执行

### dockerfile多阶段构建

- `所有编译构建，包括依赖库的编译等过程放入一个dockerfile，会导致镜像的体积过大；镜像的层次多，部署时间变长；源代码存在泄漏的风险`

```dockerfile
# 只构建某一阶段的镜像使用target指定: docker build --target builder -t user/go:1.0 .
FROM golang:1.9-alpine as builder

# 第二阶段构建
FROM alpine as prod
```

注意：*使用manifest列表可以根据系统不同的架构来查找不同的镜像*[manifest官方博客介绍](https://www.docker.com/blog/multi-arch-all-the-things/)

## 命令

```shell
# 启动docker-ce
sudo systemctl enable docker
sudo systemctl start docker

# 查看镜像，容器，数据卷所占的空间
docker system df

# 在dockerfile的目录编译镜像
docker build -t nginx:v3 .
```

## 搭建私人docker registry仓库

```shell
# 安装运行docker-registry，默认仓库将创建在/var/lib/registry目录，也可以用-v参数来指定存放位置
docker run -d -p 5000:5000 --restart=always --name registry registry

# 将镜像推到本地的registry，注意docker默认不允许非https推送镜像，可以通过docker的配置选项取消该限制
docker tag ubuntu:latest 127.0.0.1:5000/ubuntu:latest
docker push 127.0.0.1:5000/ubuntu:latest
```

## docker网络

`尽量将容器加入自定义的docker网络，连接多个容器`

```shell
# 创建docker网络
docker network create -d bridge my-net
```
