# algorithms

<!-- TOC -->

- [algorithms](#algorithms)
  - [1.快慢指针](#1%e5%bf%ab%e6%85%a2%e6%8c%87%e9%92%88)
  - [2.前缀和](#2%e5%89%8d%e7%bc%80%e5%92%8c)
  - [3.动态规划（DP,dynamic programming）](#3%e5%8a%a8%e6%80%81%e8%a7%84%e5%88%92dpdynamic-programming)
  - [4.二叉树相关算法](#4%e4%ba%8c%e5%8f%89%e6%a0%91%e7%9b%b8%e5%85%b3%e7%ae%97%e6%b3%95)
    - [4.1DFS(前中后序遍历)](#41dfs%e5%89%8d%e4%b8%ad%e5%90%8e%e5%ba%8f%e9%81%8d%e5%8e%86)
    - [4.2BFS层序遍历](#42bfs%e5%b1%82%e5%ba%8f%e9%81%8d%e5%8e%86)
  - [5.回溯法](#5%e5%9b%9e%e6%ba%af%e6%b3%95)
    - [5.1介绍](#51%e4%bb%8b%e7%bb%8d)
  - [6.排序算法](#6%e6%8e%92%e5%ba%8f%e7%ae%97%e6%b3%95)
    - [6.1冒泡排序(bubble sort)](#61%e5%86%92%e6%b3%a1%e6%8e%92%e5%ba%8fbubble-sort)
    - [6.2选择排序(selection sort)](#62%e9%80%89%e6%8b%a9%e6%8e%92%e5%ba%8fselection-sort)
    - [6.3插入排序(insertion sort)](#63%e6%8f%92%e5%85%a5%e6%8e%92%e5%ba%8finsertion-sort)
    - [6.4归并排序(merge sort)](#64%e5%bd%92%e5%b9%b6%e6%8e%92%e5%ba%8fmerge-sort)
    - [6.5快速排序(quick sort)](#65%e5%bf%ab%e9%80%9f%e6%8e%92%e5%ba%8fquick-sort)
    - [6.6堆排序(heap sort)](#66%e5%a0%86%e6%8e%92%e5%ba%8fheap-sort)
    - [6.7桶排序(bucket sort)](#67%e6%a1%b6%e6%8e%92%e5%ba%8fbucket-sort)
    - [6.8计数排序(counting sort)](#68%e8%ae%a1%e6%95%b0%e6%8e%92%e5%ba%8fcounting-sort)
    - [6.9基数排序(radix sort)](#69%e5%9f%ba%e6%95%b0%e6%8e%92%e5%ba%8fradix-sort)
  - [7.分治法(divide and conquer)](#7%e5%88%86%e6%b2%bb%e6%b3%95divide-and-conquer)
    - [求解问题的特征](#%e6%b1%82%e8%a7%a3%e9%97%ae%e9%a2%98%e7%9a%84%e7%89%b9%e5%be%81)
    - [求解步骤](#%e6%b1%82%e8%a7%a3%e6%ad%a5%e9%aa%a4)
    - [应用](#%e5%ba%94%e7%94%a8)
  - [8.二分搜索](#8%e4%ba%8c%e5%88%86%e6%90%9c%e7%b4%a2)

<!-- /TOC -->

**本文件夹主要放置一些算法的实现,leet_code以及剑指offer中的代码实现。**

[数据结构与算法/leetcode题解](https://algorithm.yuanbin.me/zh-hans/)

## 1.快慢指针

- [快慢指针的应用总结](https://blog.csdn.net/qq_21815981/rticle/detai76)

*应用*：

- 判断单链表是否存在环
- 在有序链表中寻找中位数
- 输出链表中的倒数第K个节点（正数第k-1个）
- 判断链表是否存在环，如果有，找到环入口
- 判断两个单链表是否相交，如果相交，找到他们的第一个公共节点

## 2.前缀和

- [前缀和介绍](https://blog.csdn.net/k_r_forever/rticle/details/81775899)

*思路*:

对于`[a0, a1, a2, a3]`n个数，给出m次询问，每次给出[l, r]求这个区间内a1, a0+a1+a2, a0+a1+a2+a3]`形成新的数组`[b0, b1, b2, b3];（2）如果是则只需`b3-b1`。

*应用*:

- 降低查询的时间复杂度

## 3.动态规划（DP,dynamic programming）

- [动态规划入门](https://blog.csdn.net/baidu_28312631/article/details/47418773)
- [动态规划简介](https://www.jianshu.com/p/40064cb0d5f3)

*核心思想*：

将问题拆解为子问题，即`分治`的思想，形式为`f(n)=f(n-1)f(n-2)`

1. `划分状态`，划分子问题
2. `状态表示`，让计算机理解
3. `状态转移`，父问题如何由子问题推导
4. `确定边界`，确定初始状态，最小的子问题，最终状态

*应用*：

- 斐波那契数列
- 最长子序列和

## 4.二叉树相关算法

- [github二叉树的遍历算法](https://github.com/azl397985856/leetcode/blob/master/thinkings/binary-tree-traversal.md)

### 4.1DFS(前中后序遍历)

使用栈来简化操作。

- *前序遍历*：根-->左-->右
- *中序遍历*：左-->根-->右
- *后序遍历*：左-->右-->根

### 4.2BFS层序遍历

## 5.回溯法

### 5.1介绍

将问题的解空间转化为图或者树的结构，然后使用优先搜索策略遍历，遍历的过程记录和寻找所有可行解或者最优解。

参考：[算法入门之回溯法](https://blog.csdn.net/weiyuefei/article/details/79316653)

## 6.排序算法

### 6.1冒泡排序(bubble sort)

- [冒泡排序python实现](./sort_algorithms/sort_algorithm.py)
- [冒泡排序算法图解](https://blog.csdn.net/zhangshk_/article/details/82911093)

**复杂度**:

- 平均时间复杂度:$O(n^2)$
- 空间复杂度:$O(1)$

**算法描述**：

1. 比较相邻的元素，如果第一个大于第二个，则交换；
2. 对每一对相邻元素做比较，从第一对到最后一对，最后的元素是最大的数；
3. 针对所有元素重复以上步骤，除了最后一个元素；
4. 重复步骤1-3至完成

### 6.2选择排序(selection sort)

在没有排序的数组中找到最大或者最小的放到位置，然后从剩余中继续寻找直至最后一个元素。

**复杂度**:

- 平均时间复杂度:$O(n^2)$
- 空间复杂度:$O(1)$

### 6.3插入排序(insertion sort)

- [插入排序python实现](./sort_algorithms/sort_algorithm.py)
- [插入排序算法图解](https://blog.csdn.net/zhangshk_/article/details/82911093)

**复杂度**:

- 平均时间复杂度:$O(n^2)$
- 空间复杂度:$O(1)$

希尔排序

- [希尔排序算法图解](https://blog.csdn.net/zhangshk_/article/details/82911093)

### 6.4归并排序(merge sort)

- [归并排序算法图解](https://blog.csdn.net/zhangshk_/article/details/82911093)

**复杂度**:

- 平均时间复杂度:$O(nlogn)$
- 空间复杂度:$O(n)$

### 6.5快速排序(quick sort)

核心思想：基准数大的都放在基准数的右边,把比基准数小的放在基准数的左边,这样就找到了该数据在数组中的正确位置。

- [快速排序python实现](./sort_algorithms/sort_algorithm.py)
- [快速排序算法图解](https://blog.csdn.net/zhangshk_/article/details/82911093)
- [快速排序算法详解](http://www.sohu.com/a/246785807_684445)

**复杂度**:

- 平均时间复杂度:$O(nlogn)$
- 空间复杂度:$O(logn)$

**算法描述**：

使用分治法将一个串分成两个子串

1. 从数列中挑出一个元素作为基准`pivot`(随意挑选，可以选择第一个)；
2. 重新排列数列，所有元素比基准小的放在基准前面，比基准大的放在后面，在这个基准退出之后，该基准就处在数列的中间位置，这称为`分区操作`；
3. `递归`的将小于基准值元素的子数列和大于基准元素的子数列排列

### 6.6堆排序(heap sort)

- [堆排序算法图解](https://blog.csdn.net/zhangshk_/article/details/82911093)

**复杂度**:

- 平均时间复杂度:$O(nlogn)$
- 空间复杂度:$O(1)$

### 6.7桶排序(bucket sort)

- [桶排序算法图解](https://blog.csdn.net/zhangshk_/article/details/82911093)

**复杂度**:

- 平均时间复杂度:$O(n+k)$, `k`为桶的个数
- 空间复杂度:$O(n+k)$

### 6.8计数排序(counting sort)

- [计数排序算法图解](https://blog.csdn.net/zhangshk_/article/details/82911093)

**复杂度**:

- 平均时间复杂度:$O(n+k)$, `k`为桶的个数
- 空间复杂度:$O(k)$

### 6.9基数排序(radix sort)

- [基数排序算法图解](https://blog.csdn.net/zhangshk_/article/details/82911093)

**复杂度**:

- 平均时间复杂度:$O(n*k)$, `k`为桶的个数
- 空间复杂度:$O(n+k)$

## 7.分治法(divide and conquer)

将一个复杂的问题分成多个相同或者相似的子问题，直至最后的子问题可以简单的求解。

### 求解问题的特征

- 问题规模缩小到一定的规模就可以容易解决
- 问题可以分解为若干规模较小的相同问题，即具有`最优子结构`性质
- 利用该问题分解的子问题的解可以合并为该问题的解
- 分解出来的问题是相互独立的

### 求解步骤

1. **分解**，原问题分解为若干子问题
2. **解决**，递归求解各个子问题
3. **合并**，将子问题的解合并为原问题的解

### 应用

1. 二分搜索
2. 大整数乘法
3. 归并排序
4. 快速排序
5. 汉诺塔
6. 循环赛日程表

## 8.二分搜索

- 在`有序数组`中寻找目标值，当然有时候需要自己构建有序数组
- [二分搜索python实现](./search_algorithms/binary_search.py)
