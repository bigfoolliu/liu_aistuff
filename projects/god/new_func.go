package main

import (
	"fmt"
	"reflect"
)

func main() {
	// 声明一个引用类型的变量i，不光需要为其声明，还要需要为其分配内存
	var i *int
	// 用new为i分配内存
	i = new(int)
	*i = 10
	fmt.Println(*i, i)

	// 用来查看数据的类型
	fmt.Println(reflect.TypeOf(*i))
	fmt.Println(fmt.Sprintf("%T", *i))
}
