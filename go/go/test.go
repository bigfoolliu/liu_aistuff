package main

import (
	"fmt"
	// "log"
	"unsafe"
)

const (
	year = "2019"
	pi = 3.1415926
)

// varSize 返回变量所占空间
// func varSize(a string) string {
// 	return unsafe.Sizeof(a)
// }

// exchange variable
func exchange() {
	a := "str1"
	b := "str2"
	a, b = b, a
	fmt.Println("a:", a, "b:", b)
}

func transvar() (string, string) {
	return "0", "1"
}

// test2 用来区分输出格式的差异
func test2() {
	// log.info("programe start")

	// a := "tony"
	var a int
	// 一段段处理
	fmt.Println(a)

	var b string
	fmt.Printf("%T\n", b)  // 格式化输出变量类型
}

func sizeof() {
	var ret int
	var ret2 string
	var ret3 float64
	fmt.Println(unsafe.Sizeof(ret))
	fmt.Println(unsafe.Sizeof(ret2))
	fmt.Println(unsafe.Sizeof(ret3))
}

// asicc 码
func asicc() {
	var a byte
	a = 97
	fmt.Printf("a: %c %d\n", a, a)
}

func main() {
	// test2()
	// exchange()

	// _, x := transvar()
	// fmt.Printf("x: %v\n", x)

	fmt.Printf("year is %v\npi is %v\n", year, pi)
	sizeof()
	asicc()
}
