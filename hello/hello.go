package main

import (
	"fmt"
)


// 定义一个people类型
type people struct {
	name string
	age int
	isadmin bool
}

// notify 为方法
func (p people) notify() {
	fmt.Printf("this is %v\n", p.name)
}

// struct_demo 用户定义类型操作
func struct_demo() {
	fmt.Println("类型操作------------------------------")

	// 函数内部声明的类型不能调用外部声明的方法
	type user struct {
		name string
		age int
		admin bool
	}

	type admin struct {
		person user  // 需要一个user作为管理者
		level string
	}

	// 声明一个user类型的变量
	var tony user
	tony.name = "tony"
	fmt.Println(tony)

	// 声明一个admin类型的变量
	var tom admin
	fmt.Println(tom)

	jim := people {
		name: "jim",
		age: 20,
		isadmin: true,
	}
	jim.notify()

	fmt.Println("类型操作------------------------------")
}

// dict_demo 简单映射操作
func dict_demo() {
	fmt.Println("映射操作------------------------------")

	// 声明映射
	dict1 := make(map[string]int)
	fmt.Println(dict1)

	dict2 := map[string]int{"age":10, "score":40}
	fmt.Println(dict2)

	fmt.Println("映射操作------------------------------")
}

// array_demo 简单数组操作
func array_demo() {
	fmt.Println("数组操作------------------------------")

	// 不知道长度时
	a := [...]int{1, 4}
	fmt.Println(a)

	// 指定元素位置，其余位置为默认值0
	b := [5]int{1:10, 2:20}
	fmt.Println(b)

	// 访问指针数组的元素,首先分配空间,然后赋值
	c := [2]*int{new(int), new(int)}
	fmt.Println(c)
	*c[0] = 1
	*c[1] = 2
	fmt.Println(c, c[0], *c[0])

	// 多维数组
	d := [2][3]int{1:{3, 4, 5}}
	fmt.Println(d)

	fmt.Println("数组操作------------------------------")
}

// array_pointer 接受指向100万个整型元素的数组的指针,节省空间
// 只需要分配8个字节的空间，而不是8M
func array_pointer(array *[1e6]int) {
	fmt.Println(array)
}

// slice_demo 简单切片的操作
func slice_demo() {

	fmt.Println("切片操作------------------------------")

	// i指定切片的长度和容量以及类型，字符串切片,长度和容量都是10
	slice := make([]string, 10)
	fmt.Println(slice)

	// 切片的长度为3，容量为5
	slice2 := make([]string, 3, 5)
	fmt.Println(slice2)

	// 声明空切片以及nil切片
	slice3 := make([]int, 0)
	var slice4 []int
	fmt.Println(slice3, slice4)

	// 使用append向切片增加元素
	slice5 := []int{10, 20, 30, 40, 50}
	newslice := slice5[1:3]  // 长度为2，容量为4
	fmt.Println(newslice)
	newslice = append(newslice, 60)
	fmt.Println(slice5, newslice)

	// 将一个切片追加到另一个切片
	slice6 := []int{1, 2, 5}
	slice7 := []int{3, 4}
	fmt.Println(append(slice6, slice7...))

	// 迭代切片
	for index, value := range slice6 {
		fmt.Println(index, value)
	}

	fmt.Println("切片操作------------------------------")
}

func main() {
	// fmt.Println("vim-hello")
	array_demo()

	//var array [1e6]int
	//array_pointer(&array)
	slice_demo()

	dict_demo()

	struct_demo()

}
