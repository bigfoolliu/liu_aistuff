# go语言基础知识

<!-- TOC -->

- [go语言基础知识](#go语言基础知识)
    - [1.介绍](#1介绍)
        - [1.1类型系统](#11类型系统)
    - [2.基础概念](#2基础概念)
        - [2.1 GOPATH规则](#21-gopath规则)
        - [2.2基本命令](#22基本命令)
        - [2.3基础语法](#23基础语法)
            - [2.3.1命名](#231命名)
            - [2.3.2注释](#232注释)
            - [2.3.3符号](#233符号)
            - [2.3.4包以及包的组织](#234包以及包的组织)
            - [2.3.n其他](#23n其他)
        - [2.4打包和工具链](#24打包和工具链)
    - [3.数据类型](#3数据类型)
        - [3.1布尔型 bool](#31布尔型-bool)
        - [3.2数字型 float32, float64](#32数字型-float32-float64)
        - [3.3字符串类型](#33字符串类型)
        - [3.4nil类型](#34nil类型)
        - [3.5派生类型](#35派生类型)
        - [3.5接口](#35接口)
        - [3.6占位符](#36占位符)
    - [4.变量与常量以运算](#4变量与常量以运算)
        - [4.1变量定义](#41变量定义)
        - [4.2常量定义](#42常量定义)
        - [4.3运算符](#43运算符)
    - [5.函数](#5函数)
        - [5.1声明一个函数](#51声明一个函数)
        - [5.2函数作为一个实参](#52函数作为一个实参)
        - [5.3数据结构创建函数](#53数据结构创建函数)
    - [6.基础语句](#6基础语句)
        - [6.1条件语句](#61条件语句)
    - [7.高级用法](#7高级用法)
        - [7.1goroutine](#71goroutine)
        - [7.2godoc](#72godoc)
        - [7.3GO MODULE包管理](#73go-module包管理)
        - [7.4Generate生成代码](#74generate生成代码)
    - [8.模块使用](#8模块使用)
        - [8.1statik模块](#81statik模块)
        - [8.2os模块](#82os模块)
        - [8.3flag模块](#83flag模块)
        - [8.4strconv模块](#84strconv模块)

<!-- /TOC -->

## 1.介绍

相对来说，go语言更适合`系统编程`。

[go语言入门教程](http://c.biancheng.net/golang/)
[go语言中文网](https://studygolang.com/)
[go playground,浏览器中执行go代码](https://play.golang.org/)
[Go标准库文档](https://godoc.org/)

### 1.1类型系统

- 一个类型由其他更小的类型组合而成，而不是传统的基于继承的模型
- go接口对一组行为建模，而接口描述类型的行为
- go语言的接口更小，只倾向于定义一个单一的动作

## 2.基础概念

1. 可以直接编译为机器码
2. 静态数据类型和编译语言
3. 内置支持并发
4. 内置垃圾回收
5. 部署简单
6. 强大的标准库
7. 可以直接将编译的程序移植而不需要依赖

package（包）:

- 同一个包下文件属于同一个工程文件，不必import，可直接使用
- 同一个包下面所有文件package名字一样
- 同一个包下面的文件package名字建议为目录名字，也可以不是

```go
// import点操作, 含义是导入之后调用的时候可以省略前缀包名
import (
    . "fmt"
)

// 别名操作,将包重命名
import (
    f "fmt"
)

// _ 操作，引入该包，但是不直接使用里面的标识符，而是调用了该包的init函数
// 为了让程序可读性更强，go编译器不允许声明导入一个包但不使用，下划线让编译器接受这类导入
import (
    _ "github.com/ziutek/mymysql/godrv"
)
```

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

# 不想签入编译完成的文件,即删除编译后的可执行文件
go clean hello.go

# 执行命令
go run hello.go

# 检查代码的常见错误
go vet hello.go

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

#### 2.3.1命名

`某个名称在包外是否可见，就取决于其首个字符是否为大写字母.`

1. 包名：`包应当以小写的单个单词来命名，且不应使用下划线或驼峰记法`;`包名应为其源码目录的基本名称`;
2. 获取器名：当一个包被导入后，包名就会成了内容的访问器。
3. Go中约定使用驼峰记法 MixedCaps 或 mixedCaps。

#### 2.3.2注释

有普通注释和生成文档的注释，普通注释有单行注释和多行注释。

普通注释：

```go
// 单行注释

/*
这是多行注释
*/
```

#### 2.3.3符号

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

#### 2.3.4包以及包的组织

包的概念：

- 一个.go文件就是一个包
- 每一个包都应该在单独的一个目录里面, 不能把多个包放在同一个目录里面
- 不能将同一个包的文件分拆到多个不同的目录
- 同一个目录下的所有.go文件必须声明同一个包名

`包的命名`：

- 给包命名的惯例是使用包所在目录的名字
- main包具有特殊含义，go会将这种包编译为二进制文件
- 所有go编译的二进制可执行文件所有main包即main函数

`导包`：

- go使用环境变量设置的路径，通过相对路径来查找磁盘上的包，标准库中的包会在安抓go的位置找到
- 远程导入，如果包不存在的话会默认使用go get获取到该包，然后导入
- 包重名的时候可以使用重命名解决

安装依赖包一般的4个路径：

1. github.com/
2. golang.org/
3. gopkg.in/
4. honnet.go/

#### 2.3.n其他

1. Go的正式语法使用分号来结束语句，词法分析器会使用一条简单的规则来自动插入分号，因此因此源码中基本就不用分号
2. `不再使用 do 或 while 循环，只有一个更通用的 for`
3. `if 和 switch 像 for一样可接受可选的初始化语句`

### 2.4打包和工具链

TODO:

## 3.数据类型

变量的声明我们可以通过var关键字，然后就可以在程序中使用。当我们不指定变量的默认值时，这些`变量的默认值是他们的零值`。

### 3.1布尔型 bool

### 3.2数字型 float32, float64

### 3.3字符串类型

### 3.4nil类型

- 空值
- 任何类型在未初始化时都对应一个零值：布尔类型是false，整型是0，字符串是""，而指针，函数，interface，slice，channel和map的零值都是`nil`

### 3.5派生类型

1. 指针类型(Pointer)
2. 数组类型
3. 结构化类型(struct)
4. Channel类型
5. 函数类型
6. 切片类型(动态数组)
7. 接口类型(interface)
8. Map类型(集合,无序键值对)

```go
// 创建map集合的两种方式
var m1 map[string]string
m2 = make(map[string]string)
```

### 3.5接口

所有的具有共性的方法定义在一起，任何其他类型只要实现了这些方法就是实现了这个接口。

`注意`：

1. 接口内只实现了函数的声明,没有实现
2. 接口中只能有方法的声明, 不能有变量的声明
3. 只要某种数据类型实现了接口, 那么就可以使用接口变量保存这种数据类型
4. 只要某种数据类型实现了接口, 那么就可以使用接口变量调用接口中声明的方法
5. 实现一个接口, 不需要做额外的声明, 只要某种数据类型绑定了所有接口中的方法就是实现了这个接口
6. 只有实现了接口中声明的所有方法, 才算实现了接口, 才能使用接口变量保存
7. 在实现接口的时候, 方法名称,形参列表,返回值列表必须一模一样

### 3.6占位符

[完整占位符介绍](https://www.jianshu.com/p/66aaf908045e)

普通占位符：

- `%v` 相应值的默认格式
- `%+v` 打印结构体时候，会添加字段名
- `%#v` 相应值的Go语法表示
- `%T` 相应值的类型的Go语法表示

布尔占位符：

- `%t` true或者false

整数占位符:

- `%b` 二进制表示
- `%c` 相应Unicode表示
- `%d` 十进制表示
- `%x` 十六进制表示

字符串与字节切片占位符:

- `%s` 输出字符串表示

## 4.变量与常量以运算

### 4.1变量定义

- 不可以再次对于相同名称的变量使用初始化声明
- 声明了一个局部变量却没有在相同的代码块中使用它，同样会得到编译错误

```go
// 单变量声明
// 1.指定变量类型，不赋值则为默认值
var name type
name = value
// 2.自行判断变量类型
var name = value
// 3.省略var,但是 := 左侧的变量不应该为声明过的，否则编译错误
c := 10

// 多变量声明
// 1.逗号分隔，声明赋值分开,不赋值则给默认值
var name1, name2 type
name1, name2 = value1, value2
// 2.直接赋值，可以是不同类型
var name1, name2 = value1, value2
// 3.集合类型
var (
    name1 type
    name2 type
)
```

### 4.2常量定义

- 不曾使用的常量，在编译的时候，是不会报错的
- 特殊常量`iota`,一个可以被编译器修改的常量，每一个const出现被重置为0,在下一个const出现之前，其所代表的数字会自增1

```go
// 1.显示定义
const a string = "ha"
// 2.隐式定义
const b = "ha"
// 用作枚举
const (
    UNKNOWN = 0
    MALE = 1
    FEMALE = 2
)
```

### 4.3运算符

1. 算术运算：`+ - * / %(求余) ++ --`
2. 关系运算：`== != > < >= <=`
3. 逻辑运算：`&& || !`
4. 其他 TODO:

## 5.函数

`注意`：

1. Go语言中的函数可以和任何类型绑定, 但是一般用于和结构体绑定.
2. 定义一个结构体,将函数和结构体绑定在一起的东西就是方法
3. 方法和函数的区别在于, 函数可以直接调用(通过包名.函数名称), 而方法只能通过绑定的数据类型对应的变量来调用(变量.函数名称)
4. 函数名称和方法名称可以重名
5. go的函数需要显示返回，即不会自动返回最后一个表达式的值

### 5.1声明一个函数

```go
// 后一个int表明返回值得类型
func max(num1, num2 int) int {
    if num1 > num2 {
        return num1
    } else {
        return num2
    }
}
```

### 5.2函数作为一个实参

函数作为实参，可以实现回调。

### 5.3数据结构创建函数

`new`:

- 动态分配一个空间，只需要使用，不必考虑内存释放其生命周期
- 只接受一个参数，这个参数是一个类型
- 分配好内存之后，返回一个指向该类型内存地址的指针，同时将分配的内存置为0
- 不常用

```go
i = new(int)
a := new(Student)
```

`make`:

- 同样用于内存分配
- 只用于chan, map以及切片的内存创建
- 返回的类型就是类型本身，而不是指针类型

```go
// 创建了一个有10个元素的Slice对象
var v []int = make([]int, 10)
```

## 6.基础语句

### 6.1条件语句

```go
// if
if 布尔表达式 {
   /* 在布尔表达式为 true 时执行 */
} else {
  /* 在布尔表达式为 false 时执行 */
}

// switch
switch var1 {
    case val1:
        ...
    case val2:
        ...
    default:
        ...
}

// type switch,判断某个interface变量中实际存储的变量类型
var x interface{}
switch i := x.(type) {
    case nil:
        fmt.Printf(" x 的类型 :%T",i)
    case int:
        fmt.Printf("x 是 int 型")
    default:
        fmt.Printf("未知型")

// select语句，类似switch,随机执行一个case,没有case执行则会阻塞至有case执行
// 每个case都必须是一个通信
// 所有channel表达式都会被求值
// 所有被发送的表达式都会被求值
// 如果任意某个通信可以进行，它就执行；其他被忽略。
// 如果有多个case都可以运行，Select会随机公平地选出一个执行。其他不会执行。
// 否则：
// 如果有default子句，则执行该语句。
// 如果没有default字句，select将阻塞，直到某个通信可以运行；Go不会重新对channel或值进行求值。
var i1, int
var c1 chan int
select {
    case i1 = <-c1:
        fmt.Printf("received ", i1, " from c1\n")
    default:
        fmt.Printf("no communication\n")
```

## 7.高级用法

### 7.1goroutine

[goroutine参考文章](https://www.jianshu.com/p/f8949c2953f5)，可以被看作go特有的应用程序线程。

几个概念：

- M：machine的缩写。一个M代表一个内核线程，或者“工作线程”。
- P：processor的缩写。一个P代表执行一个Go代码片段所必需的资源（或称“上下文环境”）。
- G：goroutine的缩写。一个G代表一个Go代码片段。前者是对后者的一种封装。

### 7.2godoc

使用`godoc`或者指定端口`godoc -http=:6660`可以在本地开启一个文档服务器。

godoc生成规则：

```go
// math_test.go 测试文件

package smath

import "fmt"

// Add 两数相加（这一行会被截取为简短介绍）
// 两数相加的注意事项以及原理（这一行作为超级详细的介绍）
func Add(n1,n2 int)int{
    return n1 + n2
}

func ExampleAdd() {
    fmt.Println(Add(1,2))
    // Output: 3
}
```

### 7.3GO MODULE包管理

- 主要用于解决当项目建立不在GOPATH路径下的导包问题
- 环境变量不再用于解析import路径，即GOPATH/src下的包，import找不到了
- GO MODULE功能开启之后，下载的包将放在GOPATH/
- GOPATH/bin下面的功能依旧

```shell

```

### 7.4Generate生成代码

扫描与当前包相关的源码文件，找出所有包含`//go:generate`的特殊注释，提取并执行该注释后面的命令，命令为可执行程序，形同shell下面执行。

- generate 指令只能在go文件中使用
- 需要注意的是和传统注释不同的是 // 后面不能有空格
- go build等其他命令不会调用go generate,必须手动调用

```shell
# 参数说明：
# -run 正则表达式匹配命令行，仅执行匹配的命令
# -v 打印已被检索处理的文件。
# -n 打印出将被执行的命令，此时将不真实执行命令
# -x 打印已执行的命令
go generate [-run regexp] [-n] [-v] [-x] [build flags] [file.go... | packages]

# $GOARCH
# 架构 (arm, amd64, etc.)
# $GOOS
# OS (linux, windows, etc.)
# $GOFILE
# 当前处理中的文件名
# $GOLINE
# 当前命令在文件中的行号
# $GOPACKAGE
#     当前处理文件的包名
# $DOLLAR
# 固定的"$",不清楚用途
```

## 8.模块使用

### 8.1statik模块

将静态资源编译进二进制文件，将静态文件封装到go语言的source code，然后提供一个统一的接口，通过该接口传入文件，返回对应路径的文件数据。

简而言之：将静态文件生成.go文件，然后编译为二进制，项目启动的时候，再把这个.go文件释放为静态文件。

```shell
# 安装
go get github.com/rakyll/statik
go install github.com/rakyll/statik
```

### 8.2os模块

### 8.3flag模块

### 8.4strconv模块
