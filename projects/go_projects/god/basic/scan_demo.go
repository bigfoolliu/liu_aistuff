package main

import "fmt"

func main(){
	// 等待用户输入
	var a int
	fmt.Printf("输入数字:")

	fmt.Scan(&a)
	fmt.Println("a=", a)
}