#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""
根据传入的参数批量的更改文件夹内文件的扩展
使用方式:
python3 -work_dir ./test_dir -old_ext .txt -old_ext .conf
"""


import os
import argparse


def get_parser():
    """从命令行获取参数"""
    parser = argparse.ArgumentParser(description="Change the extension of files")
    parser.add_argument("-work_dir", metavar="WORK_DIR", type=str, nargs=1, help="The directory where to change extensions")
    parser.add_argument("-old_ext", metavar="OLD_EXT", type=str, nargs=1, help="Old extension")
    parser.add_argument("-new_ext", metavar="NEW_EXT", type=str, nargs=1, help="New extension")
    return parser


def batch_rename(work_dir, old_ext, new_ext):
    """批量修改扩展名"""
    for file_name in os.listdir(work_dir):
        print("[INFO]dealing file: {}".format(file_name))
        # 获取文件扩展名
        split_text = os.path.splitext(file_name)
        file_ext = split_text[1]

        if file_ext != new_ext:
            new_file_name = split_text[0]+ new_ext  # 构建一个新的文件名
            os.rename(os.path.join(work_dir, file_name), os.path.join(work_dir, new_file_name))
        print("[INFO]file {} complete".format(file_name))


def main():
    parser = get_parser()
    args = vars(parser.parse_args())

    work_dir = args["work_dir"][0]
    old_ext = args["old_ext"][0]
    new_ext = args["new_ext"][0]

    if old_ext[0] != ".":
        old_ext = "." + old_ext
    
    if new_ext[0] != ".":
        new_ext = "." + new_ext
    
    batch_rename(work_dir, old_ext, new_ext)
    print("[INFO]batch name complete")


if __name__ == "__main__":
    main()
