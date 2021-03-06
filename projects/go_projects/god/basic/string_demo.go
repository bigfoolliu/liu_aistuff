package main

import (
	"fmt"
)

func main() {

	var a byte
	var s string

	// 单引号字符往往只有一个字符,转义字符 \n 除外
	a = 'a'
	fmt.Println("a: ", a)

	// 字符串隐藏结束符 \0
	s = "a"
	fmt.Println("s: ", s)

	var s1 string
	s1 = "hello go"
	fmt.Printf("s1: %c, s1[0]: %c, s1[1]: %c\n", s1, s1[0], s1[1])

	// 复数的展示
	c := 2.1 + 3.2i
	fmt.Printf("c: %v  type is %T\n", c, c)
	fmt.Println("real(c):", real(c), "img(c):", imag(c))
}
