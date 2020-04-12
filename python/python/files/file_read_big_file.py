#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
流式读取大文件
with open方式读取大文件，若所有字符串在同一行则将消耗大量的内存
"""


def chunked_file_reader(fp, block_size=1024*8):
    """
    生成器函数，分块读取文件
    fp: 待操作的文件对象
    block_size: 每次读取的块的大小
    """
    while True:
        chunk = fp.read(block_size)
        if not chunk:
            break
        yield chunk


def read_file(fpath): 
    BLOCK_SIZE = 1024 
    with open(fpath, 'rb') as f: 
        while True: 
            block = f.read(BLOCK_SIZE) 
            if block: 
                yield block 
            else: 
                return


if __name__ == "__main__":
    pass

