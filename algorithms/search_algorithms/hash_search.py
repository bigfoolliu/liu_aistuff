#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
哈希查找python实现

涉及数据结构哈希表
"""


class HashTable(object):

    """忽略了对数据类型以及元素溢出的问题的判断"""

    def __init__(self, size):
        self.count = size  #  最大表长度
        self.elem = [None for i in range(size)]  # 使用列表最为hash元素的保存方法

    def hash(self, key):
        """构造hash表的散列函数"""
        return key % self.count   # 散列函数用除留余数法
    
    def insert_hash(self, key):
        """插入关键字到hash表"""
        address = self.hash(key)
        while self.elem[address]:  # 当前位置有数据，发生冲突
            address = (address+1) % self.count  # 冲突采取线性探测的方式看下一个地址是否可用
        self.elem[address] = key

    def search_hash(self, key):
        """在hash表中查找指定的关键字"""
        star = address = self.hash(key)
        while self.elem[address] != key:
            address = (address+1) % self.count
            if not self.elem[address] or address == star:  # 没找到对应的元素或者循环到了开始的位置
                return False
        return True


if __name__ == "__main__":
    hash_table = HashTable(100)
    array = [12, 34, 55, 63, 22, 66, 8, 100, 102, 1000]

    # 将元素存储到hash表中
    for i in array:
        hash_table.insert_hash(i)
    # 输出hash表中存储的元素以及对应下标
    for i in hash_table.elem:
        if i:
            print((i, hash_table.elem.index(i)))
    
    print(hash_table.search_hash(22))
    print(hash_table.search_hash(100))
