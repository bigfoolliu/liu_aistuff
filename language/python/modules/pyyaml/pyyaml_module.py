#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
pyyaml模块使用

yaml介绍：
    1.yaml: Yet Another Markup Language ：另一种标记语言。yaml 是专门用来写配置文件的语言，非常简洁和强大,之前用ini也能写配置文件，
        更直观，更方便，有点类似于json格式
    2.yaml基本语法规则：
        - 大小写敏感
        - 使用缩进表示层级关系
        - 缩进时不允许使用Tab键，只允许使用空格。
        - 缩进的空格数目不重要，只要相同层级的元素左侧对齐即可
        - #表示注释，从这个字符一直到行尾，都会被解析器忽略，这个和python的注释一样
    3.yaml支持的数据结构有三种：
        - 对象：键值对的集合，又称为映射（mapping）/ 哈希（hashes） / 字典（dictionary）
        - 数组：一组按次序排列的值，又称为序列（sequence） / 列表（list）
        - 量（scalars）：单个的、不可再分的值。字符串、布尔值、整数、浮点数、Null、时间、日期
"""


import yaml


def read_yaml():
    """返回解析的yaml配置"""
    yaml_path = './yaml_test.yaml'

    with open(yaml_path, 'r', encoding='utf-8') as f:
        config = f.read()

    loaded_config = yaml.safe_load(config)
    return loaded_config


if __name__ == '__main__':
    yaml_config = read_yaml()

    for i in yaml_config.items():
        print(i)
