/*
接口和方法集的概念

interface 可以定义一组方法，但是不必急于实现

- 是为了实现多态
- 可以根据类型的具体实现方法采取不同的行为
- 任何实现了interface中声明的全部方法即表明实现了该接口

*/

package main

import (
	"fmt"
)


// 定义一个接口
type notifier interface {
	notify()
	speak()
}

// 发送通知,其只接收实现了notifier接口的值作为参数
// 可以根据对象的实际定义来实现不同的功能
func sendNotification(n notifier) {
	n.notify()
	n.speak()
}

// 定义一个user类型
type user struct {
	name string
	age int
}

// 定义user的方法,使用指针接受者实现
func (u *user) notify() {
	fmt.Println(u.name, u.age)
}

func (u *user) speak() {
	fmt.Println("speak")
}

func main() {
	tony := user{
		name: "tony",
		age: 12,
	}

	// tony.notify()

	// 注意此处取的是tony user的地址
	sendNotification(&tony)
}
