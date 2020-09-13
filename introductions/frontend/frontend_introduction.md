# 前端相关知识

<!-- vim-markdown-toc Marked -->

- [前端相关知识](#前端相关知识)
  - [1.基础知识](#1基础知识)
  - [2.前端流行的9大框架](#2前端流行的9大框架)
    - [2.1Vue](#21vue)
    - [2.2React](#22react)
    - [2.3Angular](#23angular)
  - [3.js包管理工具](#3js包管理工具)
    - [3.1npm](#31npm)
    - [3.2yarn](#32yarn)
  - [其他](#其他)

<!-- vim-markdown-toc -->

## 1.基础知识

### 1.1web标准

- 结构标准（HTML）：用于对网页元素进行整理和分类。
- 表现标准（CSS）：用于设置网页元素的版式、颜色、大小等外观样式。
- 行为标准（JS）：用于定义网页的交互和行为。

根据上面的三个标准，将web前端分为三层(HTML, CSS, JS)

### 1.2浏览器

- **渲染引擎(浏览器内核，rendering engine)** + **JS引擎** 组成
- 内核读取网页内容，计算显示方式并展示
- js引擎读取js代码并执行

## 2.前端流行的9大框架

- [前端流行的9大框架](https://zhuanlan.zhihu.com/p/76463271)

### 2.1Vue

- 可以自底向上逐层应用
- 便于上手和第三方库或项目整合

### 2.2React

- 主要用于构建ui
- 较高的性能

### 2.3Angular

- MVVM,模块化
- 自动化双向数据绑定
- 语义化标签

## 3.js包管理工具

### 3.1npm

预处理：

```sh
npm config get registry  # 获取当前npm的版本
npm install -g npm  # 更新npm

# 安装源切换
npm config set registry=https://registry.npm.taobao.org  # 切换为淘宝源
npm config set registry=http://registry.npmjs.org  # 切换为官方源
```

使用：

```sh
npm init  # 初始化
npm install module_name -S  # 安装具体的模块
```

### 3.2yarn

- 一个包管理器
- [使用文档](https://yarn.bootcss.com/docs/)

```sh
# 安装升级
brew install yarn
brew upgrade yarn

yarn --version

# 1.初始化一个项目
yarn init

# 2.管理依赖
yarn add <package>  # 添加依赖包，自动添加至package.json
yarn add --dev  # 将依赖只添加到devDependencies
yarn add --optional  # 将依赖只添加到optionalDependencies中

yarn upgrade <package>  # 升级依赖，会修改package.json和yarn.lock

yarn remove <package>  # 删除依赖，会修改package,json和yarn.lock

# 3.安装依赖
yarn install  # 安装所有的依赖
```

## 其他

- `OpenSSL`组织。
- `W3C`组织。
