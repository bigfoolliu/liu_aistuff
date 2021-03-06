package main

import (
	"fmt"
	"net"
)

func main() {
	conn, err := net.Dial("tcp", "localhost:8998")
	if err != nil {
		panic(err.Error())
	}
	defer conn.Close()

	for i := 0; i < 5; i++ {
		//准备要发送的字符串
		msg := fmt.Sprintf("hello")
		fmt.Println("11")
		_, err := conn.Write([]byte(msg))
		if err != nil {
			println("Write Buffer Error:", err.Error())
			break
		}
		fmt.Println(msg)

	}
}
