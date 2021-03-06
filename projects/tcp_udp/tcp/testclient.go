package main

import (
	"fmt"
	"net"
	"strconv"
	"time"
)

func main() {
	conn, err := net.Dial("tcp", "localhost:8998")
	// conn, err := net.Dial("tcp", "localhost:8998")
	if err != nil {
		panic(err.Error())
	}
	defer conn.Close()

	for {
		//准备要发送的字符串
		time.Sleep(2 * time.Second)
		// msg := fmt.Sprintf("127.0.0.1/23:j76")
		// fmt.Println("11")

		timeStamp := time.Now().Unix()
		msg := strconv.FormatInt(timeStamp, 10)

		_, err := conn.Write([]byte(msg))
		if err != nil {
			println("Write Buffer Error:", err.Error())
			break
		}
		fmt.Println(msg)

	}
}
