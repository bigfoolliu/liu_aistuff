// go 实现最简单的curl的功能

package main

import (
	"fmt"
	"os"
	"io"
	"net/http"
)

func init() {
	if len(os.Args) != 2 {
		fmt.Println("Usage: example")
		os.Exit(-1)
	}
}

func main() {
	// 得到响应
	r, err := http.Get(os.Args[1])
	if err != nil {
		fmt.Println(err)
		return
	}

	// 从body复制到Stdout
	io.Copy(os.Stdout, r.Body)
	if err := r.Body.Close(); err != nil {
		fmt.Println(err)
	}
}
