#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
哈希表
"""
from number_theory.prime_numbers import next_prime


class HashTable(object):

    def __init__(self, size_table, charge_factor=None, lim_charge=None):
        self.size_table = size_table  # hash表的大小
        self.values = [None] * self.size_table  # 哈希表的初始值
        self.lim_charge = 0.75 if lim_charge is None else lim_charge
        self.charge_factor = 1 if charge_factor is None else charge_factor
        self.__aux_list = []
        self._keys = {}
    
    def keys(self):
        return self._keys

    def balanced_factor(self):
        """平衡因子"""
        return sum([1 for slot in self.values if slot is None]) / (self.size_table * self.charge_factor)

    def hash_function(self, key):
        """创建哈希表的哈希函数"""
        return key % self.size_table

    def _step_by_step(self, step_ord):
        print("step {0}".format(step_ord))
        print([i for i in range(len(self.values))])
        print(self.values)
    
    def bulk_insert(self, values):
        """块插入"""
        i = 1
        self.__aux_list = values
        for value in values:
            self.insert_data(value)
            self._step_by_step(i)
            i += 1

    def _set_value(self, key, data):
        """设置值"""
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
        """重新hash"""
        survivor_values = [value for value in self.values if value is not None]
        self.size_table = next_prime(self.size_table, factor=2)
        self._keys.clear()
        self.values = [None] * self.size_table
        map(self.insert_data, survivor_values)
    
    def insert_data(self, data):
        """hash表插入数据"""
        key = self.hash_function(data)
        if self.values[key] is None:
            self._set_value(key, data)
        elif self.values[key] == data:
            pass
        else:
            colison_resolution = self._colison_resolution(key, data)
            if colison_resolution is not None:
                self._set_value(colison_resolution, data)
            else:
                self.rehashing()
                self.insert_data(data)
