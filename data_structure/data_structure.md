# data_structure

本文件夹主要放置一些数据结构的实现。

<!-- TOC -->

- [data_structure](#datastructure)
  - [1.链表(linked list)](#1%e9%93%be%e8%a1%a8linked-list)
  - [2.二叉树(binary tree)](#2%e4%ba%8c%e5%8f%89%e6%a0%91binary-tree)
  - [3.霍夫曼压缩(huffman compression)](#3%e9%9c%8d%e5%a4%ab%e6%9b%bc%e5%8e%8b%e7%bc%a9huffman-compression)
  - [4.队列(queue)](#4%e9%98%9f%e5%88%97queue)
    - [4.1优先队列(priority queue)](#41%e4%bc%98%e5%85%88%e9%98%9f%e5%88%97priority-queue)
    - [4.2双端队列(double-ended queue, dequeue)](#42%e5%8f%8c%e7%ab%af%e9%98%9f%e5%88%97double-ended-queue-dequeue)
  - [5.堆](#5%e5%a0%86)
  - [6.栈](#6%e6%a0%88)
    - [6.1介绍](#61%e4%bb%8b%e7%bb%8d)
    - [6.2应用](#62%e5%ba%94%e7%94%a8)

<!-- /TOC -->

## 1.链表(linked list)

- [单链表python实现](./link_list/single_link_list.py)
- [双链表python实现](./link_list/double_link_list.py)

`线性表`的一种，最基本，最简单，最常用的一种结构。

存储方式：

1. 顺序存储
2. 链式存储
   1. 优点是定点插入和定点删除的时间复杂度为O(1)
   2. 缺点是访问的时间复杂度最坏为O(n)

## 2.二叉树(binary tree)

- [二叉树](./binary_tree/binary_tree.md)

## 3.霍夫曼压缩(huffman compression)

放弃对文本文件的普通保存方式，不再使用7位或8位二进制数表示每一个字符，而是用较少的比特表示出现频率最高的字符，用较多的比特表示出现频率低的字符。

## 4.队列(queue)

一个 FIFO（先进先出）的数据结构，并发中使用较多，可以安全地将对象从一个任务传给另一个任务。

- 基本的队列和栈在Python中由list实现

### 4.1优先队列(priority queue)

优先队列中的每个元素都有各自的优先级，优先级高的元素先获得服务；优先级相同的元素根据其在优先队列中的顺序获得服务。

- Python中通过`heapq`库来实现优先队列

### 4.2双端队列(double-ended queue, dequeue)

可以在任何一端添加或者移除元素，是具有队列和栈性质的数据结构。

- python中，为提高效率，使用collections库，`collections.dqueue()`

## 5.堆

- 通常指`二叉堆`，物理结构为数组，逻辑结构为完全二叉树
- 根节点最大的堆为最大堆或者大根堆，根节点最小的堆为最小堆或者小根堆
- `常被用作实现优先队列`

## 6.栈

- [栈的实现以及其他类型的栈](https://blog.csdn.net/wenqiang1208/article/details/77193449)
- [栈的python实现](./stack/stack.py)

栈是一种 LIFO(Last In First Out) 的数据结构，常用方法有添加元素，取栈顶元素，弹出栈顶元素，判断栈是否为空。

### 6.1介绍

**特点**:

- 先进后出，后进先出(LIFO)

**类型**:

- 共享栈，其实就是一个数组
- 链式栈，通过节点构成的单链表构成

### 6.2应用

- 括号匹配
- 十进制表示N进制
- 行编辑
