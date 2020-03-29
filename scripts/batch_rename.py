#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
批量将leetcode文件命令为001_xxx.py格式
"""


import os
import sys


def main(batch_dir):
    """需要重命名的文件夹,现在仅支持但一层，不支持迭代文件夹"""
    walk_files = os.walk(batch_dir)
    files = list(walk_files)[0][2]
    for file in files:
        index = file.split('_')[0]
        if len(index) < 3:
            while len(index) < 3:
                index = '0' + index
            new_file_name = '_'.join([index, *file.split('_')[1:]])

            old_file_path = os.path.join(batch_dir, file)
            new_file_path = os.path.join(batch_dir, new_file_name)
            try:
                os.rename(old_file_path, new_file_path)
            except Exception as e:
                print(f"{old_file_path} rename error:{e}")
            print(f'{old_file_path}--->\n{new_file_path}\n')
    print('done')


if __name__ == '__main__':
    print(sys.argv)
    batch_dir = sys.argv[1]
    print('{}'.format(os.path.abspath(batch_dir)))
    main(batch_dir)

