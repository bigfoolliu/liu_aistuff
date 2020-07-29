# docker practice读书笔记

<!-- vim-markdown-toc Marked -->

* [1.容器](#1.容器)
* [2.镜像](#2.镜像)
* [3.dockerfile](#3.dockerfile)
        - [dockerfile参考](#dockerfile参考)
        - [dockerfile相关命令](#dockerfile相关命令)
        - [dockerfile多阶段构建](#dockerfile多阶段构建)
        - [dockerfile最佳实践](#dockerfile最佳实践)
* [4.搭建私人docker registry仓库](#4.搭建私人docker-registry仓库)
* [5.docker网络](#5.docker网络)
* [6.docker-compose](#6.docker-compose)
* [7.kubernetes](#7.kubernetes)
        - [概念](#概念)

<!-- vim-markdown-toc -->

## 1.容器

- 容器的本质是进程
- 每一个容器运行时候，以镜像为`基础层`，在其上创建一个当前层的`存储层`
- 最佳实践：容器不应该向存储层写入任何内容，容器存储层保持无状态化，所有的文件写入操作，都应该使用`数据卷`，或者`绑定宿主目录`
- 容器的应用都应该以前台执行，容器没有后台服务的概念

```sh
# 将容器快照导出为本地文件
docker export 1233 > ubuntu.tar

# 将容器快照文件导入为镜像
cat ubuntu.tar | docker import - test/ubuntu:1.0
```

## 2.镜像

- 镜像唯一的标识为ID和摘要

```sh
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

## 3.dockerfile

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

### dockerfile最佳实践

1. 容器应该是短暂的，dockerfile构建镜像的启动的容器应该尽有可能短的生命周期
2. 使用`.dockerignore`文件，类似.gitignore文件
3. 使用多阶段构建
4. 避免安装不必要的包
5. 一个容器只运行一个进程
6. 镜像层数应该尽可能的少
7. 多行参数的时候要排序
8. 构建的时候使用缓存，`--no-cache=true`就会在缓存中查找可重用的

## 4.搭建私人docker registry仓库

```sh
# 安装运行docker-registry，默认仓库将创建在/var/lib/registry目录，也可以用-v参数来指定存放位置
docker run -d -p 5000:5000 --restart=always --name registry registry

# 将镜像推到本地的registry，注意docker默认不允许非https推送镜像，可以通过docker的配置选项取消该限制
docker tag ubuntu:latest 127.0.0.1:5000/ubuntu:latest
docker push 127.0.0.1:5000/ubuntu:latest
```

## 5.docker网络

`尽量将容器加入自定义的docker网络，连接多个容器`

```sh
# 创建docker网络
docker network create -d bridge my-net

# 运行一个容器并加入到网络，其他加入的容器可以通过 ping busybox1 来验证互联关系
docker run -it --rm --name busybox1 --network mynet
```

## 6.docker-compose

`定义和运行多个docker容器的应用`。

两个概念：

- `服务(service)`，应用的容器，实际上可以是包含若干运行相同镜像的容器实例
- `项目(project)`，由一组关联的的应用容器组成一个完整的业务单元

```sh
# 尝试自动完成包括构建镜像，创建服务，启动服务
docker-compose up

# 构建或者重新构建项目中的服务容器
docker-compose build

# 验证compose文件格式是否正确
docker-compose config

# 进入指定的容器
docker-compose exec

# compose文件中包含的镜像
docker-compose images

# 该命令会停止up命令所启动的容器
docker-compose down

# 拉取服务依赖的镜像
docker-compose pull

# 推送服务依赖的镜像到docker的镜像仓库
docker-compose push
```

## 7.kubernetes

`目标是管理跨多个主机的容器，提供基本的部署，维护以及运用伸缩`。*易学*，*便携*，*可扩展*，*自修复*。

### 概念

- `节点(Node)`：一个节点是一个运行kubernetes中的主机，`可以是虚拟主机或者物理机器`
- `容器(Pod)`：一个Pod对应于由若干容器组成的一个容器组，同个组内的容器共享一个`存储卷(volume)`
- `容器组生命周期(pos-states)`：包含所有容器状态集合，包含容器组状态类型，容器组生命周期，事件，重启策略
  - 生命状态: `pending`,`running`, `succeeded`, `failed`
- `Replication Controllers`: 负责指定数量的pod在同一时间一起运行
- `服务(services)`: 一个kubernetes服务是容器组逻辑的高级抽象
- `卷(volume)`: 一个卷就是一个目录，容器对其有访问权限
- `标签(labels)`: 标签是用来连接一组对象的，比如容器组，可以被用来组织和选择子对象
- `接口权限(accessing_the_api)`: 端口，ip地址和代理的防火墙规则
- `web界面(ux)`：用户可以通过web界面操作kubernetes
- `命令行操作(cli)`: kubecfg命令
