# Kubernetes介绍

<!-- TOC -->

- [Kubernetes介绍](#kubernetes%e4%bb%8b%e7%bb%8d)
  - [1.基本介绍](#1%e5%9f%ba%e6%9c%ac%e4%bb%8b%e7%bb%8d)
    - [1.1核心概念](#11%e6%a0%b8%e5%bf%83%e6%a6%82%e5%bf%b5)
  - [2.基本命令](#2%e5%9f%ba%e6%9c%ac%e5%91%bd%e4%bb%a4)
  - [3.一键部署](#3%e4%b8%80%e9%94%ae%e9%83%a8%e7%bd%b2)

<!-- /TOC -->

## 1.基本介绍

Kubernetes基于容器技术的分布式架构领先方案，开源的容器集群管理系统。[中文文档](https://www.kubernetes.org.cn/docs)

### 1.1核心概念

1. `Master`，k8s集群的管理节点，负责管理集群，提供集群的资源数据访问入口。
2. `Node`，Kubernetes集群架构中运行Pod的服务节点（亦叫agent或minion）。
3. `Pod`，运行于Node节点上，若干相关容器的组合。
4. `Replication Controller`，用来管理Pod的副本，保证集群中存在指定数量的Pod副本。
5. `Service`，定义了Pod的逻辑集合和访问该集合的策略，是真实服务的抽象。
6. `Label`，Kubernetes中的任意API对象都是通过Label进行标识，Label的实质是一系列的Key/Value键值对，其中key于value由用户自己指定。

## 2.基本命令

```shell
# 查看集群信息
kubectl cluster-info

# 创建pod
kubectl create -f xxx.yaml

# 删除pod
kubectl delete -f xxx.yaml

# 直接应用新的pod
kubectl apply -f xxx.yaml

# 列出当前所有的pods
kubectl get pods

# 查看节点的信息
kubectl get nodes

# 查看service的信息
kubectl get service

# 查看某pod的日志
kubectl log -f pod_name

# 删除pod
kubectl delete deployment host-manager-deploy

# 获取部署的节点
kubectl get deployment

# 获取svc
kubectl get svc

# 获取指定的pod的信息并将输出重定向至yaml文件
kubectl describe pod nginx-storage-pod > nginx-storage-pod.yaml

# 进入容器内部
kubectl exec -it <pod_name> -- sh
```

## 3.一键部署

`ansible`
