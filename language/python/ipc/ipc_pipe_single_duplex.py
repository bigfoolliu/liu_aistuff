#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
python进程间通信

- 使用标准库提供的管道，单工，读写方向固定
- 只允许具有亲缘关系的两个进程通信
"""


import os
import sys


def main():

    # 创建读写管道
    read_pipe, write_pipe = os.pipe()
    print(f'read_pipe:{read_pipe}, write_pipe: {write_pipe}')
    
    # 非windows系统,创建子进程
    process_id = os.fork()

    print(f'process_id: {process_id}')

    if process_id:
        os.close(write_pipe)

        read_pipe = os.fdopen(read_pipe)

        print('Parent reading')

        s = read_pipe.read()

        print(f'text: {s}')
        sys.exit(0)
    else:
        os.close(read_pipe)

        write_pipe = os.fdopen(write_pipe, 'w')
        print('Child writing')

        write_pipe.write('text written by child')
        write_pipe.close()

        print('child closing')
        sys.exit(0)


if __name__ == "__main__":
    main()
