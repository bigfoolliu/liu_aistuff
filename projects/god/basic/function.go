package main

import "fmt"

// 具有可变参数的函数
func sum(nums ...int) {
	fmt.Println(nums, "")
	total := 0
	for _, num := range nums {
		total += num
	}
	fmt.Println(total)
}

func main() {
	sum(1, 2)
	sum(3, 4, 5, 6)
}
