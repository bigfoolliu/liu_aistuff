# go语言基础知识

<!-- TOC -->

- [go语言基础知识](#go%e8%af%ad%e8%a8%80%e5%9f%ba%e7%a1%80%e7%9f%a5%e8%af%86)
  - [1.学习资源](#1%e5%ad%a6%e4%b9%a0%e8%b5%84%e6%ba%90)
  - [2.基础概念](#2%e5%9f%ba%e7%a1%80%e6%a6%82%e5%bf%b5)
    - [2.1 GOPATH规则](#21-gopath%e8%a7%84%e5%88%99)
    - [2.2基本命令](#22%e5%9f%ba%e6%9c%ac%e5%91%bd%e4%bb%a4)
    - [2.3基础语法](#23%e5%9f%ba%e7%a1%80%e8%af%ad%e6%b3%95)
    - [2.3.1命名](#231%e5%91%bd%e5%90%8d)
    - [2.3.2其他](#232%e5%85%b6%e4%bb%96)
    - [2.3.4符号](#234%e7%ac%a6%e5%8f%b7)

<!-- /TOC -->

## 1.学习资源

[go语言入门教程](http://c.biancheng.net/golang/)
[go语言中文网](https://studygolang.com/)

## 2.基础概念

1. 可以直接编译为机器码
2. 静态数据类型和编译语言
3. 内置支持并发
4. 内置垃圾回收
5. 部署简单
6. 强大的标准库

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

### 2.2基本命令

```shell
# 将文件直接编译为机器码
go build hello.go
# 执行命令
go run hello.go
# 查看版本
go version
# 查看环境
go env
# 查看当前目录中所有可用包
go list
# 清空生成的可执行文件
go clean
# 从远程下载第三方的库至GOPATH
go get
# 查看包或者函数的源码的api
go doc [package] [function]
# 对文件进行格式化
gofmt hello.py
```

### 2.3基础语法

### 2.3.1命名

`某个名称在包外是否可见，就取决于其首个字符是否为大写字母.`

1. 包名：`包应当以小写的单个单词来命名，且不应使用下划线或驼峰记法`;`包名应为其源码目录的基本名称`;
2. 获取器名：当一个包被导入后，包名就会成了内容的访问器。
3. Go中约定使用驼峰记法 MixedCaps 或 mixedCaps。

### 2.3.2其他

1. Go的正式语法使用分号来结束语句，词法分析器会使用一条简单的规则来自动插入分号，因此因此源码中基本就不用分号
2. `不再使用 do 或 while 循环，只有一个更通用的 for`
3. `if 和 switch 像 for一样可接受可选的初始化语句`

### 2.3.4符号

1. `:=`：短声明
2. 遍历数组、切片、字符串或者映射，或从信道中读取消息,用range

```go
for i := 0; i < 10; i++ {
    sum += i
}
```

```go
for key, value := range oldMap {
    newMap[key] = value
}
```
