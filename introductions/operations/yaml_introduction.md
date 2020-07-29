# yaml介绍

<!-- vim-markdown-toc Marked -->

* [1.基本语法规则](#1.基本语法规则)
* [2.基本概念](#2.基本概念)
        - [2.1对象](#2.1对象)
        - [2.2数组](#2.2数组)
        - [2.2纯量](#2.2纯量)
* [3.Kubernetes使用yaml文件的配置](#3.kubernetes使用yaml文件的配置)
        - [3.1基本的使用yaml做k8s的配置实例](#3.1基本的使用yaml做k8s的配置实例)
        - [3.2创建Deployment](#3.2创建deployment)

<!-- vim-markdown-toc -->

## 1.基本语法规则

- 大小写敏感
- 使用缩进表示层级关系
- 缩进时不允许使用Tab键，`只允许使用空格`
- `缩进的空格数目不重要，只要相同层级的元素左侧对齐即可`
- `#`表示注释，从这个字符一直到行尾，都会被解析器忽略

## 2.基本概念

### 2.1对象

```yaml
# 专为js则为{animal: "pets"}
animal: pets
```

### 2.2数组

```yaml
- cat
- dog

# 当数组为子成员时,该项缩进
- animal
  - cat
  - dog
```

### 2.2纯量

- 字符串
- 布尔值
- 整数
- 浮点数
- ull
- 时间
- 日期

```yaml
# 数值
age: 12
# 布尔值
isSet: true
# 当为null值
name: ~
# 字符串
str: 字符串
str: "字符 串"
str: "it''s you"
```

## 3.Kubernetes使用yaml文件的配置

### 3.1基本的使用yaml做k8s的配置实例

```yaml
# 可以在特定Kubernetes API找到完整的Kubernetes Pod的属性

apiVersion: v1  # 版本号需要根据安装的Kubernetes版本和资源类型进行变化，不是写死的
kind: Pod  # Deployment、Job、Ingress、Service等
metadata:  # Pod的一些meta信息，比如名称、namespace、标签等信息
  name: kube100-site
  labels:
    app: web
spec:  # 包括一些container，storage，volume以及其他Kubernetes需要的参数，以及诸如是否在容器失败时重新启动容器的属性
  containers:
    - name: front-end
      image: nginx
      ports:
        - containerPort: 80
```

### 3.2创建Deployment

目的是让Kubernetes去管理一组Pod的副本，也就是`副本集` ，这样就能够*保证一定数量的副本一直可用*，不会因为某一个Pod挂掉导致整个服务挂掉。
[使用YAML 文件创建 Kubernetes Deployment](https://www.qikqiak.com/post/use-yaml-create-kubernetes-deployment/)

```yaml
apiVersion: extensions/v1beta1
kind: Deployment
metadata:
  name: kube100-site
spec:
  replicas: 2  # 指定副本的数量
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
        - name: front-end
          image: nginx
          ports:
            - containerPort: 80
```
