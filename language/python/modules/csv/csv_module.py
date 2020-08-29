#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
csv模块使用

- 逗号分隔符结构化文本文件(.csv)
- 将已存在的结构化的文本写入至本地并保存为csv格式文件
"""

import csv
import pandas


def create_csv_demo():
    """
    创建csv对象以及文件示例
    """
    # 自定义一个带有标题的csv格式的文件
    villains = [
        {"first": "doctor", "last": "no"},
        {"first": "rosa", "last": "klebb"},
        {"first": "mister", "last": "big"},
        {"first": "auric", "last": "goldfinge"},
        {"first": "ernst", "last": "blofeld"}
    ]

    # 将已存在的结构化的文本写入至本地并保存为csv格式文件
    with open("./csv_test.txt", "wt") as f:
        # 创建一个DictWriter对象
        cout = csv.DictWriter(f, ["first", "last"])

        # 将头("first", "last")写入
        cout.writeheader()

        # 写入单行或同时写入多行
        cout.writerow({"first": "doctor", "last": "yes"})
        cout.writerows(villains)
    print("create csv demo done")


def read_csv_demo():
    """
    读取已经存在的csv格式文件
    """
    with open("./csv_test.txt", "rt") as fin:
        cin = csv.DictReader(fin)
        villains = [row for row in cin]

    print(type(villains), villains)


def read_csv_demo2():
    """
    2. csv文件读取

    reader()方法读取
    或pandas库中的read_csv()方法
    """
    with open("./csv_test.csv", "r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)

    # 此种方法用的更多，更方便
    csv_file = pandas.read_csv("csv_test.csv")
    print(csv_file)


def no_header_csv_demo():
    """
    无标题的csv使用示例
    """
    villains = [
        ["doctor", "no"],
        ["rosa", "klebb"],
        ["mister", "big"],
        ["auric", "goldfinger"],
        ["sophia", "blod"]
    ]

    # 写入
    with open("./csv_no_header_test.txt", "wt") as f:
        csvout = csv.writer(f)
        csvout.writerows(villains)
    print("write done")

    # 读取
    with open("./csv_no_header_test.txt", "rt") as fin:
        cin = csv.reader(fin)
        villains = [row for row in cin]

    print(villains)


if __name__ == "__main__":
    # create_csv_demo()
    # read_csv_demo()
    read_csv_demo2()
    # no_header_csv_demo()
