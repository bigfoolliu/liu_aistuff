import socket
 
def main():
    # 创建udp套接字,
    # AF_INET表示ip地址的类型是ipv4，
    # SOCK_DGRAM表示传输的协议类型是udp
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
 
    # 要发送的ip地址和端口（元组的形式）
    # send_addr = ('192.168.147.136', 8080)
    send_addr = ('127.0.0.1', 8080)
    print('send_addr = ', send_addr)

    while True:
        # 要发送的信息
        test_data = input('请输入要发送的消息：')
        print('send_data: ', test_data)
 
        # 发送消息
        udp_socket.sendto(test_data.encode("utf-8"), send_addr)
 
    # 关闭套接字
    # udp_socket.close()


if __name__ == "__main__":
    main()
