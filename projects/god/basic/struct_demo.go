package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log"
	"os"
)

// Task 任务, 关于标签：https://www.jianshu.com/p/c4ec92afeca8
type Task struct {
	ID   int    `json:"id" xorm:"int pk autoincr"` // 后面定义的是标签
	Name string `json:"name" xorm:"varchar(32) notnull"`
}

func main() {
	task := Task{
		ID:   1,
		Name: "demo",
	}

	fmt.Println("task:", task)

	// 将格式化数据转化为json字符串
	b, err := json.Marshal(task)
	if err != nil {
		log.Fatalln(err)
	}

	var out bytes.Buffer
	err = json.Indent(&out, b, "", "\t")

	if err != nil {
		log.Fatal(err)
	}

	out.WriteTo(os.Stdout)
	print("\n")
}
