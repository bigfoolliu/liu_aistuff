package main

import "fmt"

// rect 指定一个结构化类型
type rect struct {
	width  int
	height int
}

// 指定该类型的一个方法
func (r *rect) getArea() int {
	return r.height * r.width
}

func main() {
	r := rect{width: 10, height: 5}
	fmt.Println("area: ", r.getArea())
}
