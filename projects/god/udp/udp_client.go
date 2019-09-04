// udp_client.go udp示例客户端的文件

package main

import (
	"fmt"
	"net"
	"os"
)

func main() {
	connection, err := net.Dial("udp", "127.0.0.1:1111") // 返回一个连接以及错误信息
	defer connection.Close()
	if err != nil {
		os.Exit(1)
	}

	connection.Write([]byte("hello server"))
	fmt.Println("send msg")

	var msg [20]byte
	connection.Read(msg[0:])
	fmt.Println("msg is ", string(msg[0:10]))
}
