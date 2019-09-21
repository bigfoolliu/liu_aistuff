package main

import "fmt"

func main() {
	// 使用make创建一个map
	m := make(map[string]int)

	// 增加，修改键值对， k不存在为增加，k存在为修改
	m["k1"] = 7
	m["k2"] = 13
	fmt.Println("map:", m)
	fmt.Println("len:", len(m))

	// 删除键值对
	delete(m, "k2")
	fmt.Println("map:", m)

	// 查找键值对
	v1 := m["k1"]
	v2 := m["k3"]
	fmt.Println("v1:", v1, "v2:", v2) // 不存在默认给了0

	// 这种不存在键值报false
	_, prs := m["k2"]
	fmt.Println("prs:", prs)

	// 直接使用map来创建
	n := map[string]int{
		"foo": 1,
		"bar": 2,
	}
	fmt.Println("map:", n)

	// map的遍历
	for k, v := range n {
		fmt.Printf("k:[%v] v:[%v]\n", k, v)
	}

}
