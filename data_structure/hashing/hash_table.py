#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
哈希表

基本思想是以关键字为自变量，通过函数（散列函数或者哈希函数），计算出对应的函数值（哈希地址），
以这个值作为数据元素的地址，并将数据元素存入到相应地址的存储单元。

应用是实现字典操作的一种有效的数据结构。

常用哈希函数:
1.除留余数法，H(key)=key%p
2.直接地址法，H(key=a*key+b
3.数字分析法
4.平方取中法
5.折叠法
"""
from number_theory.prime_numbers import next_prime


class HashTable(object):

    def __init__(self, size_table, charge_factor=None, lim_charge=None):
        self.size_table = size_table
        self.values = [None] * self.size_table
        self.lim_charge = 0.75 if lim_charge is None else lim_charge
        self.charge_factor = 1 if charge_factor is None else charge_factor
        self.__aux_list = []
        self._keys = {}
    
    def keys(self):
        return self._keys

    def balanced_factor(self):
        return sum([1 for slot in self.values if slot is None]) / (self.size_table * self.charge_factor)

    def hash_function(self, key):
        """创建哈希表的哈希函数"""
        return key % self.size_table

    def _step_by_step(self, step_ord):
        print("step {0}".format(step_ord))
        print([i for i in range(len(self.values))])
        print(self.values)
    
    def bulk_insert(self, values):
        i = 1
        self.__aux_list = values
        for value in values:
            self.insert_data(value)
            self._step_by_step(i)
            i += 1

    def _set_value(self, key, data):
        self.values[key] = data
        self._keys[key] = data
    
    def _colison_resolution(self, key, data=None):
        """碰撞解决"""
        new_key = self.hash_function(key + 1)
        while self.values[new_key] is not None and self.values[new_key] != key:
            if self.values.count(None) > 0:
                new_key = self.hash_function(new_key += 1)
            else:
                new_key = None
                break
    
    def rehashing(self):
        survivor_values = [value for value in self.values if value is not None]
        self.size_table = next_prime(self.size_table, factor=2)
        self._keys.clear()
        self.values = [None] * self.size_table
        map(self.insert_data, survivor_values)
    
    def insert_data(self, data):
        key = self.hash_function()