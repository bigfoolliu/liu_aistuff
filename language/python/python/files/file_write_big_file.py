#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
写入超大文件和写入指定大小文件
"""


import time


def create_big_file(file_size, file_name):
    """
    :param file_size: int, 单位为Mb
    :param file_name: str
    """
    f = open(file_name, 'w', encoding='utf-8')
    f.seek(1024 * 1024 * file_size)    
    f.write('test')
    f.write('test')
    f.close()


def create_file(file_size, file_name):
    """
    生成指定大小的文件，文件内容为随机数字
    :param file_size: int, Mb
    :param file_name: str
    """
    f = open(file_name, 'w', encoding='utf-8')
    for _ in range(file_size):
        try:
            f.write('01' * 512 * 1024)
        except Exception:
            f.close()
            exit(-1)
    f.close()


if __name__ == "__main__":

    s = time.time()
    # create_big_file(100, './big_file_test')
    create_file(10, './file_test')
    e = time.time()
    print(f'spend {e-s} s')
