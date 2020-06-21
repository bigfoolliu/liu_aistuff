#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
b+树python基础实现

参考：https://github.com/apeeyush/BPlusTree
"""


import bisect
import os
import sys
import time

import numpy


class Node(object):
    """b+树的节点"""

    def __init__(self, file_name=None):
        if file_name:
            self.read_data_from_file(file_name)
    
    def read_data_from_file(self, file_name):
        """从文件读取数据"""
        global file_counter
        global disk_counter

        disk_counter += 1
        file_path = "./data/" + file_name  # 设置默认数据文件夹路径
        lines = [line.strip() for line in open(file_path)]
        self.keys = [float(key) for key in lines[0].split(",")]
        self.children = [child.strip() for child in lines[1].split(",")]
        if lines[2] == True:
            self.is_leaf = True
        else:
            self.is_leaf = False
        
        self.file_name = file_name
        if self.is_leaf and len(lines) >= 4:
            self.next = lines[3].strip()
        else:
            self.next = None
    
    def write_data_to_file(self, file_name):
        """将数据写入文件"""
        global disk_counter
        disk_counter += 1
        file_path = "./data/" + file_name

        with open(file_path, "w") as f:
            f.write(str(self.keys).strip("[]").replace("'", ""))
            f.write("\n")
            f.write(str(self.children).strip("[]").replace("'", ""))
            f.write("\n")
            f.write(str(self.is_leaf))
            f.write("\n")
            if self.is_leaf and self.next:
                f.write(str(self.next))
                f.write("\n")
    
    def print_content(self):
        """打印节点信息"""
        print(self.keys)
        print(self.children)
        print(self.is_leaf)
        print(self.file_name)
        if self.is_leaf:
            print(self.next)
        else:
            print("None")
    
    def update_node(self):
        """更新节点信息"""
        self.write_data_to_file(self.file_name)
    
    def split_node(self):
        """分裂一个节点，可参考b树分裂实现"""
        global file_counter
        new_node = Node()
        new_node.file_name  = str(file_counter)
        file_counter += 1
        if self.is_leaf:
            new_node.is_leaf = True
            mid = int(len(self.keys)/2)
            mid_key = self.keys[mid]

            # 更新兄弟节点
            new_node.keys = self.keys[mid:]
            new_node.children = self.children[mid:]
            # 更新节点参数
            self.keys = self.keys[:mid]
            self.children = self.children[:mid]
            # 更新下一个节点的指针
            new_node.next = self.next
            self.next = new_node.file_name
        else:
            new_node.is_leaf = False
            mid = int(len(self.keys)/2)
            mid_key = self.keys[mid]
            # 更新兄弟节点参数
            new_node.keys = self.keys[mid+1:]
            new_node.children = self.children[mid+1:]
            # 更新节点参数
            self.keys = self.keys[:mid]
            self.children = self.children[:mid+1]
        self.update_node()
        new_node.update_node()
        return mid_key, new_node


class BPlusTree(object):
    """b+树"""

    def __init__(self, factor, root_file=-1):
        self.factor = factor
        if root_file == -1:
            self.root = Node()
            # 初始化根节点
            global file_counter
            self.root.is_leaf = True
            self.root.keys = []
            self.root.children = []
            self.root.next = None
            self.root.file_name = str(file_counter)
            file_counter += 1
            self.root.update_node()
        else:
            self.root = Node(root_file)
    
    def search(self, key):
        """根据key值搜索节点"""
        return self.tree_search(key, self.root)
    
    def tree_search(self, key, node):
        """搜索树"""
        if node.is_leaf:
            return node
        else:
            if key < node.keys[0]:
                return self.tree_search(key, Node(node.children[0]))
            for i in range(len(node.keys) - 1):
                if key >= node.keys[i] and key < node.keys[i+1]:
                    return self.tree_search(key, Node(node.children[i+1]))
            if key >= node.keys[-1]:
                return self.tree_search(key, Node(node.children[-1]))
    
    def tree_search_for_query(self, key, node):
        if node.is_leaf:
            return node
        else:
            if key <= node.keys[0]:
                return self.tree_search_for_query(key, Node(node.children[0]))
            for i in range(len(node.keys)-1):
                if key > node.keys[i] and key <= node.keys[i+1]:  # 区别于上面的方法tree_search
                    return self.tree_search_for_query(key, Node(node.children[i+1]))
            if key >= node.keys[-1]:
                return self.tree_search_for_query(key, Node(node.children[-1]))
    
    def point_query(self, key):
        """指针查询"""
        all_keys = []
        all_values = []
        start_leaf = self.tree_search_for_query(key, self.root)
        keys, values, next_node = self.get_data_in_key_range(key, key, start_leaf)
        all_keys += keys
        all_values += values

        while next_node:
            keys, values, next_node = self.get_data_in_key_range(key, key, Node(next_node.file_name))
            all_keys += keys
            all_values += values
        return all_keys, all_values

    def range_query(self, key_min, key_max):
        """在指定key的范围内进行查询"""
        all_keys = []
        all_values = []
        start_leaf = self.tree_search_for_query(key_min, self.root)
        keys, values, next_node = self.get_data_in_key_range(key_min, key_max, start_leaf)
        all_keys += keys
        all_values += values

        while next_node:
            keys, values, next_node = self.get_data_in_key_range(key_min, key_max, Node(next_node.file_name))
            all_keys += keys
            all_values += values
        return all_keys, all_values
    
    def get_data_in_key_range(self, key_min, key_max, node):
        """在指定的范围查找"""
        keys = []
        values = []
        for i in range(len(node.keys)):
            key = node.keys[i]
            if key_min <= key and key <= key_max:
                keys.append(key)
                values.append(self.read_data_file(node.children[i]))
        
        if node.keys[-1] > key_max:
            next_node = None
        else:
            if node.next:
                next_node = Node(node.next)
            else:
                next_node = None
        return keys, values, next_node
    
    def insert(self, key, value):
        """插入指定的键值对"""
        ans, new_file_name = self.tree_insert(key, value, self.root)
        if ans:
            global file_counter
            new_root = Node()
            new_root.is_leaf = False
            new_root.file_name = str(file_counter)
            file_counter += 1
            new_root.keys = [ans]
            new_root.children = [self.root.file_name, new_file_name]
            new_root.update_node()
            self.root = new_root
    
    def tree_insert(self, key, value, node):
        """在树中插入节点"""
        if node.is_leaf:
            index = bisect.bisect(node.keys, key)
            node.keys[index:index] = [key]
            file_name = self.create_data_file(value)
            node.children[index:index] = [file_name]
            node.update_node()
            if len(node.keys) <= self.factor-1:
                return None, None
            else:
                mid_key, new_node = node.split_node()
                return mid_key, new_node.file_name
        else:
            if key < node.keys[0]:
                ans, new_file_name = self.tree_insert(key, value, Node(node.children[0]))
            for i in range(len(node.keys)-1):
                if key >= node.keys[i] and key < node.keys[i+1]:
                    ans, new_file_name = self.tree_insert(key, value, Node(node.children[i+1]))
            if key >= node.keys[-1]:
                ans, new_file_name = self.tree_insert(key, value, Node(node.children[-1]))
        if ans:
            index = bisect.bisect(node.keys, ans)
            node.keys[index:index] = [ans]
            node.children[index+1:index+1] = [new_file_name]
            if len(node.keys) <= self.factor-1:
                node.update_node()
                return None, None
            else:
                mid_key, new_node = node.split_node()
                return mid_key, new_node.file_name
        else:
            return None, None
    
    def create_data_file(self, value):
        """创建数据文件"""
        global file_counter
        global disk_counter
        disk_counter += 1
        file_name = str(file_counter)
        file_path = "./data/" + file_name
        with open(file_path, "w") as f:
            f.write(str(value))
        file_counter += 1
        return file_name
    
    def read_data_file(self, file_name):
        """读取数据文件"""
        global disk_counter
        disk_counter += 1
        file_path = "./data/" + file_name
        lines = [line.strip() for line in open(file_path)]
        return lines[0].strip()


def save_tree(root, file_counter):
    """保存二叉树"""
    file_path = ".bplustree"
    with open(file_path, "w") as f:
        f.write(root)
        f.write("\n")
        f.write(str(file_counter))
        f.write("\n")


def write_stats():
    """写入b+树的状态"""
    file_path = "stats.txt"
    global insert_time  # 节点插入时间
    global search_time  # 搜索时间
    global range_time  # 范围内搜索时间
    insert_time = numpy.array(insert_time)
    search_time = numpy.array(search_time)
    range_time = numpy.array(range_time)
    
    with open(file_path, "w") as f:
        if len(insert_time) > 0:
            f.write("Insert time statistics (In seconds)..\n")
            f.write("Min : "+str(numpy.amin(insert_time))+"\n")
            f.write("Max : "+str(numpy.amax(insert_time))+"\n")
            f.write("Mean: "+str(numpy.mean(insert_time))+"\n")
            f.write("STD : "+str(numpy.std(insert_time))+"\n")
            
            f.write("Insert disk statistics..\n")
            f.write("Min : "+str(numpy.amin(insert_disk))+"\n")
            f.write("Max : "+str(numpy.amax(insert_disk))+"\n")
            f.write("Mean: "+str(numpy.mean(insert_disk))+"\n")
            f.write("STD : "+str(numpy.std(insert_disk))+"\n")
            f.write("\n")
        if len(search_time) > 0:
            f.write("Point time statistics (In seconds)..\n")
            f.write("Min : "+str(numpy.amin(search_time))+"\n")
            f.write("Max : "+str(numpy.amax(search_time))+"\n")
            f.write("Mean: "+str(numpy.mean(search_time))+"\n")
            f.write("STD : "+str(numpy.std(search_time))+"\n")
            
            f.write("Point disk statistics..\n")
            f.write("Min : "+str(numpy.amin(search_disk))+"\n")
            f.write("Max : "+str(numpy.amax(search_disk))+"\n")
            f.write("Mean: "+str(numpy.mean(search_disk))+"\n")
            f.write("STD : "+str(numpy.std(search_disk))+"\n")
            f.write("\n")
        if len(range_time) > 0:
            f.write("Range time statistics (In seconds)..\n")
            f.write("Min : "+str(numpy.amin(range_time))+"\n")
            f.write("Max : "+str(numpy.amax(range_time))+"\n")
            f.write("Mean: "+str(numpy.mean(range_time))+"\n")
            f.write("STD : "+str(numpy.std(range_time))+"\n")
            
            f.write("Range disk statistics..\n")
            f.write("Min : "+str(numpy.amin(range_disk))+"\n")
            f.write("Max : "+str(numpy.amax(range_disk))+"\n")
            f.write("Mean: "+str(numpy.mean(range_disk))+"\n")
            f.write("STD : "+str(numpy.std(range_disk))+"\n")
            f.write("\n")


if __name__ == "__main__":
    # 初始化变量
    file_counter = 0
    disk_counter = 0
    start_time = 0
    end_time = 0
    insert_time = []
    search_time = []
    range_time = []
    insert_disk = []
    search_disk = []
    range_disk = []

    # 导入配置
    config = [line.strip() for line in open("bplustree.config")]
    max_num_keys = int(config[0].strip())
    factor = max_num_keys - 1

    # 从文件中加载b+树
    if not os.path.isfile(".bplustree"):
        file_path = ".bplustree"
        lines = [line.strip() for line in open(file_path)]
        root = lines[0].strip()
        tree = BPlusTree(factor, root)
        file_counter = int(lines[1].strip())
    # 初始化b+树
    else:
        tree = BPlusTree(factor)
    
    # 节点插入操作
    if sys.argv[1] == "insert":
        print("insert data")
        if len(sys.argv) >= 3:
            file_path = sys.argv[2]
        else:
            file_path = "assgn2_bplus_data.txt"
        lines = [line.strip() for line in open(file_path)]
        for line in lines:
            line = line.split()
            key = float(line[0].strip())
            value = line[1].strip()
            start_time = time.clock()
            disk_counter = 0
            tree.insert(key, value)
            end_time = time.clock()
            insert_time.append(end_time - start_time)
            insert_disk.append(disk_counter)
        print("insert successfully")
    
    # 节点查询操作
    if sys.argv[1] == "query":
        print("query data")
        if len(sys.argv) >= 3:
            file_path = sys.argv[2]
        else:
            file_path = "querysample.txt"
        
        lines = [line.strip() for line in open(file_path)]
        for line in lines:
            line = line.split()
            operation = int(line[0].strip())
            # 插入
            if operation == 0:
                key = float(line[1].strip())
                value = line[2].strip()
                start_time = time.clock()
                disk_counter = 0
                tree.insert(key, value)
                end_time = time.clock()
                insert_time.append(end_time - start_time)
                insert_disk.append(disk_counter)
                print("insert key:{} value:{}".format(key, value))
            # 点查询
            elif operation == 1:
                key = float(line[1].strip())
                value = line[2].strip()
                start_time = time.clock()
                disk_counter = 0
                keys, values = tree.point_query(key)
                end_time = time.clock()
                search_time.append(end_time - start_time)
                search_disk.append(disk_counter)
                print("search key:{}".format(key))
                if len(values) > 0:
                    print("values: {}".format(values))
                else:
                    print("not found")
            # 范围查询
            elif operation == 2:
                center = float(line[1].strip())
                qrange = float(line[2].strip())
                key_min = center - qrange
                key_max = center + qrange
                print("range:")
                eps = 0.00000001
                start_time = time.clock()
                disk_counter = 0
                keys, values = tree.range_query(key_min-eps, key_max+eps)
                end_time = time.clock()
                range_time.append(end_time - start_time)
                range_disk.append(disk_counter)
                if len(values) > 0:
                    zipped = zip(keys, values)
                    print("zipped")
                else:
                    print("not found")
    
    write_stats()
    save_tree(tree.root.file_name, file_counter)
