# docker面试准备

<!-- vim-markdown-toc Marked -->

* [1.docker基础](#1.docker基础)
        *[1.1docker与虚拟机的区别(docker的特点)](#1.1docker与虚拟机的区别(docker的特点))
        * [1.2构建镜像应该遵循的原则](#1.2构建镜像应该遵循的原则)
        *[1.3什么是docker镜像](#1.3什么是docker镜像)
        * [1.4什么是docker容器](#1.4什么是docker容器)
* [2.Devops](#2.devops)
* [3.CI持续集成](#3.ci持续集成)

<!-- vim-markdown-toc -->

- [docker介绍笔记](../introductions/service/docker_introduction.md)

## 1.docker基础

### 1.1docker与虚拟机的区别(docker的特点)

传统虚拟机是在硬件上模拟出一套完整的操作系统，在该操作系统上运行各个进程。

- 容器的进程直接运行宿主的内核，容器没有自己的内核，因此更加轻便
- 各个容器相互隔离，互不影响
- `移植性好`，便于在不同的环境系统之间迁移
- `镜像系统`，共同的镜像只需存储一份，便于分发
- `版本管理`，类似git，便于创建，管理镜像文件
- `仓库系统`，便于管理镜像
- `周边工具`，配置管理，云平台等方便CI

### 1.2构建镜像应该遵循的原则

- 尽量选取较小的基础镜像系统
- 清理编译生成文件，构建时候删除安装包以及缓存等
- 安装软件时候指定准确的版本号，避免引入不需要的依赖
- dockerfile构建镜像时候，使用.dockerignore或使用干净的工作目录

### 1.3什么是docker镜像

- docker镜像是docker容器的源码
- 镜像存储在docker注册表中
- 镜像是用多个只读镜像层组成，在网络传输时候使用最小的流量

### 1.4什么是docker容器

- docker容器包含应用程序及其依赖项
- 各个容器之间共享内核，在主操作系统的用户空间中作为独立进程运行
- 容器不依赖于任何的基础架构，可以在任何基础架构或云上运行

## 2.Devops

- [DevOps介绍](https://www.jianshu.com/p/c5d002cf25b9)
- [为什么大公司要使用DevOps](https://blog.csdn.net/g6U8W7p06dCO99fQ3/article/details/82056948)

本质上就是一种开发模型，便于开发和运维之间快速沟通，对频繁变更的需求可以快速开发交付。

## 3.CI持续集成

- [CI介绍](https://www.jianshu.com/p/61b5b549d215)
