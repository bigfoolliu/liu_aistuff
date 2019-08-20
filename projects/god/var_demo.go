package main

import (
	"fmt"
	// "unsafe"
)

/*
声明变量的示例
*/


func main() {
	// var a string = "golang"
	var a = "golang"
	fmt.Println(a)

	var b, c int = 1, 2
	fmt.Println(b, c)

	const length int = 10
	print(length)

	a = "abc"
    b = len(a)
	// c = unsafe.Sizeof(a)
	println(a, b, c)

	var r bool
	var c1, c2 bool = true, false
	r = c1 && c2
	if r {
		print("c1&&c2:", r)
	}

	var r1 bool
	r1 = c1 || c2
	if r1 {
		print("c1||c2", r1)
	}
}
