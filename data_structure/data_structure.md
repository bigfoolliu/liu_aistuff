# data_structure

本文件夹主要放置一些数据结构的实现。

<!-- TOC -->

- [data_structure](#datastructure)
  - [1.链表](#1%e9%93%be%e8%a1%a8)
  - [2.二叉树](#2%e4%ba%8c%e5%8f%89%e6%a0%91)
    - [3.霍夫曼压缩](#3%e9%9c%8d%e5%a4%ab%e6%9b%bc%e5%8e%8b%e7%bc%a9)

<!-- /TOC -->

## 1.链表

- [单链表python实现](./link_list/single_link_list.py)
- [双链表python实现](./link_list/double_link_list.py)

`线性表`的一种，最基本，最简单，最常用的一种结构。

存储方式：

1. 顺序存储
2. 链式存储
   1. 优点是定点插入和定点删除的时间复杂度为O(1)
   2. 缺点是访问的时间复杂度最坏为O(n)

## 2.二叉树

- [二叉树](./binary_tree/binary_tree.md)

### 3.霍夫曼压缩

放弃对文本文件的普通保存方式，不再使用7位或8位二进制数表示每一个字符，而是用较少的比特表示出现频率最高的字符，用较多的比特表示出现频率低的字符。
