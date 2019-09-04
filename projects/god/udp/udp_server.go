// udp_server.go udp示例的服务端文件

// 建立socket，socket
// 绑定socket，bind
// 监听，listen
// 接受连接，accept
// 接受/发送，recv/send

package main

import (
	"fmt"
	"net"
	"os"
)

// checkError 检查错误信息并将其输出
func checkError(err error) {
	if err != nil {
		fmt.Println("Error: %s", err.Error())
		os.Exit(1)
	}
}

// receiveUDPMsg 接收客户端发送的UDP消息
func receiveUDPMsg(connection *net.UDPConn) {
	var buf [20]byte
	n, raddr, err := connection.ReadFromUDP(buf[0:])
	if err != nil {
		return
	}

	fmt.Println("msg is ", string(buf[0:n]))

	_, err = connection.WriteToUDP([]byte("nice to meet u"), raddr)
	checkError(err)
}

func main() {
	udpAddr, err := net.ResolveUDPAddr("udp", ":1111")
	checkError(err)

	connection, err := net.ListenUDP("udp", udpAddr)
	defer connection.Close()
	checkError(err)

	receiveUDPMsg(connection)
}
