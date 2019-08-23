package main

import (
	"fmt"
	// "unsafe"
)

/*
声明变量的示例
*/

// 声明全局变量
var g int

func max(num1, num2 int) int {
	if num1 > num2 {
		return num1
	}
	return num2
}

func main() {
	// var a string = "golang"
	// 声明一个字符串
	var a = "golang"
	fmt.Println(a)

	// 同时声明多个变量
	var b, c int = 1, 2
	fmt.Println(b, c)

	// 声明常量
	const length int = 10
	print(length)

	a = "abc"
	b = len(a)
	// c = unsafe.Sizeof(a)
	println(a, b, c)

	// 声明布尔型变量
	var r bool
	var c1, c2 bool = true, false
	r = c1 && c2
	if r {
		print("c1&&c2:", r)
	}

	var r1 bool
	r1 = c1 || c2
	if r1 {
		print("c1||c2", r1, "\n")
	}

	print("!c1: ", !c1, "\n")

	ret := max(3, 4)
	print("ret: ", ret, "\n")

	// 声明数组变量,长度为10，元素均为int类型
	var n [10]int
	fmt.Println("数组n: ", n)

	// 指针之获取变量内存地址
	var l = 10
	ret, err := fmt.Printf("n的内存地址为: %x \n", &l)
	print("ret: ", ret, "err:", err, "\n")

	// 定义结构体,类似python中的类
	type Student struct {
		name  string
		age   int
		score int
	}
	var student1 Student
	student1.name = "tony"
	student1.age = 10
	student1.score = 100
	fmt.Println("student1: ", student1)

	// 声明一个Map集合，类似python中的字典
	var nameAgeMap map[string]int
	nameAgeMap = make(map[string]int) // 创建一个map,不执行该步骤则会创建一个nil map，从而失败

	nameAgeMap["tony"] = 10
	nameAgeMap["alice"] = 11
	nameAgeMap["tom"] = 12
	fmt.Println("map nameAgeMap: ", nameAgeMap)

	var phone Phone
	phone = new(NokiaPhone)
	phone.call()
	phone = new(IPhone)
	phone.call()
}

// Phone 声明一个接口
type Phone interface {
	// 接口内部的方法，所有Phone的接口都可以调用该方法
	call()
}

// NokiaPhone 声明一个结构体
type NokiaPhone struct {
}

// IPhone 声明一个结构体
type IPhone struct {
}

// 实现结构体NokiaPhone的方法,即将两者绑定
func (nokiaPhone NokiaPhone) call() {
	fmt.Println("I am Nokia, I can call you!")
}

// 实现结构体IPhone的方法,即将两者绑定
func (iPhone IPhone) call() {
	fmt.Println("I am iPhone, I can call you!")
}
