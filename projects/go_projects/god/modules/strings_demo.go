package main

import (
	"fmt"
	"strings"
)

func main() {
	s := " E: ID _VENDOR_ID=1871 "
	// 字符串是否包含
	fmt.Println(strings.Contains(s, "ID"))

	// 以字符串切片的形式拼接
	s1 := []string{"a", "b", "c"}
	fmt.Println(strings.Join(s1, "-"))

	// 将字符串分割
	ret := strings.Split(s, "=")
	fmt.Println(ret, "\n", "ret[0]:", ret[0], "\nret[1]:", ret[1])

	// 查找字符串的位置
	fmt.Println(strings.Index(s, "="))

	// 去除字符串头尾特定的字符
	fmt.Println(strings.Trim(s, " "))

	// 去除字符串的空格并分割返回
	fmt.Println(strings.Fields(s))
}
