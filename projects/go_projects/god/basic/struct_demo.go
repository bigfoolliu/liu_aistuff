package main

import (
	"fmt"
)

// Task 任务, 关于标签：https://www.jianshu.com/p/c4ec92afeca8
type Task struct {
	ID   int    `json:"id" xorm:"int pk autoincr"` // 后面定义的是标签
	Name string `json:"name" xorm:"varchar(32) notnull"`
}

// notify 使用值接受者实现了一个方法
func (t Task) notify() {
	fmt.Printf("%s task notify\n", t.Name)
}

// changeID 使用指针接受者实现了一个方法
func (t *Task) changeID(id int) {
	t.ID = id
}

func main() {
	task := Task{
		ID:   1,
		Name: "demo",
	}

	// fmt.Println("task:", task)
	task.notify()
	task.changeID(2)
	fmt.Println(task.ID)
}
