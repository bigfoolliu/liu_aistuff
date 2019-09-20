package main

import (
	"os"
	"strconv"
)

func main() {
	if len(os.Args) != 2 {
		os.Exit(1)
	}
	n, err := strconv.Atoi(os.Args[1])
	print(n, "\n")
	if err != nil {
		println("error:", err)
		return
	}
	defer print("after error")
	println("its this arg: ", os.Args[1])
}
