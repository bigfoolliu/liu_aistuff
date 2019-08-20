// 表名当前代码所属的包，main是程序的入口包
package main

// 导包: 导包的时候，必须使用，否则就报错
import (
	"fmt"
)

// 定义函数
func sayHello() {
	fmt.Println("hello, world")
}

// 入口函数
func main() {
	// fmt.Println("hello, world")
	sayHello()
}
