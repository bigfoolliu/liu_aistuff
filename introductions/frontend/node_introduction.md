# nodejs介绍

<!-- vim-markdown-toc Marked -->

* [1.概述](#1.概述)
    - [2.1node命令](#2.1node命令)
    - [2.2npm命令](#2.2npm命令)
* [3.使用cnpm](#3.使用cnpm)

<!-- vim-markdown-toc -->

## 1.概述

- node.js是javascript的一种运行环境，是对Google V8引擎进行的封装。是一个服务器端的javascript的解释器
- node.js中含有npm(node package manager), npm是nodejs的包管理器

### 2.1node命令

```sh
# mac安装
brew install node

# 查看安装版本
node -v

# 运行js代码
node server.js
```

### 2.2npm命令

```sh
# 查看版本
npm -v

# 查看帮助
npm help

# 升级npm
npm install npm -g

# 使用淘宝镜像
npm install -g cnpm --registry=https://registry.npm.taobao.org

# 安装指定包
npm install express  # 本地安装(放在当前目录的node_modules下面,如果没有则创建)
npm install express -g  # 全局安装

# 卸载包
npm uninstall express

# 更新包
npm update express

# 搜索包
npm search express

# 查看安装包
npm list  # 查看本地安装包
npm list -g  # 查看全局安装包
npm list express  # 查看指定安装包信息

```

## 3.使用cnpm

- npm的国内替代版

```sh
# 安装使用
npm install -g cnpm --registry=https://registry.npm.taobao.org

# 其他的使用方法基本和npm一致
```
