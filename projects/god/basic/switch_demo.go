package main

import (
	"fmt"
)

func main() {
	// input := bufio.NewScanner(os.Stdin)
	// fmt.Println("input something: ")
	// for input.Scan() {
	// 	line := input.Text()
	// 	println(line)
	// }

	a := "d"
	switch a {
	case "a":
		{
			fmt.Println("aa")
		}
	case "b":
		{
			fmt.Println("bb")
		}
	default:
		{
			fmt.Println("cc")
		}
	}
}
