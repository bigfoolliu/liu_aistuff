# go语言基础知识

<!-- TOC -->

- [go语言基础知识](#go%e8%af%ad%e8%a8%80%e5%9f%ba%e7%a1%80%e7%9f%a5%e8%af%86)
  - [1.学习资源](#1%e5%ad%a6%e4%b9%a0%e8%b5%84%e6%ba%90)
  - [2.基础概念](#2%e5%9f%ba%e7%a1%80%e6%a6%82%e5%bf%b5)
    - [2.1 GOPATH规则](#21-gopath%e8%a7%84%e5%88%99)
  - [3.基本命令](#3%e5%9f%ba%e6%9c%ac%e5%91%bd%e4%bb%a4)

<!-- /TOC -->

## 1.学习资源

[go语言入门教程](http://c.biancheng.net/golang/)

## 2.基础概念

### 2.1 GOPATH规则

api：每个版本的 api 变更差异
bin：go 源码包编译出的编译器（go）、文档工具（godoc）、格式化工具（gofmt）
blog：Go 博客的模板，使用 Go 的网页模板，有一定的学习意义
doc：英文版的 Go 文档
lib：引用的一些库文件
misc：杂项用途的文件，例如 Android 平台的编译、git 的提交钩子等
pkg：Windows 平台编译好的中间文件
src：标准库的源码
test：测试用例

## 3.基本命令

```shell
# 执行命令
go run main.go
```
