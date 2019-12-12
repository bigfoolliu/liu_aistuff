package main

import (
	"fmt"
)

// 异常捕获示例

func a() {
	// 运行到此直接报出异常
	panic("0不能作为被除数")
}

// TODO:以下代码有误
// func b() {
// 	defer catch() {
// 		if err := recover(); err != nil {
// 			log.Println("panic is: s%\n", err)
// 		}
// 	}()
// 	a()
// 	fmt.Println("b fun ends")
// }

func main() {
	fmt.Println("start")
	a()
	fmt.Println("end")
}
