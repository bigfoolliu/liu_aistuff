# algorithms文件夹

<!-- TOC -->

- [algorithms文件夹](#algorithms%e6%96%87%e4%bb%b6%e5%a4%b9)
  - [1.快慢指针](#1%e5%bf%ab%e6%85%a2%e6%8c%87%e9%92%88)
  - [2.前缀和](#2%e5%89%8d%e7%bc%80%e5%92%8c)
  - [3.动态规划（DP,dynamic programming）](#3%e5%8a%a8%e6%80%81%e8%a7%84%e5%88%92dpdynamic-programming)
  - [4.二叉树相关算法](#4%e4%ba%8c%e5%8f%89%e6%a0%91%e7%9b%b8%e5%85%b3%e7%ae%97%e6%b3%95)
    - [4.1DFS(前中后序遍历)](#41dfs%e5%89%8d%e4%b8%ad%e5%90%8e%e5%ba%8f%e9%81%8d%e5%8e%86)
    - [4.2BFS层序遍历](#42bfs%e5%b1%82%e5%ba%8f%e9%81%8d%e5%8e%86)
  - [5.回溯法](#5%e5%9b%9e%e6%ba%af%e6%b3%95)
    - [5.1介绍](#51%e4%bb%8b%e7%bb%8d)

<!-- /TOC -->

**本文件夹主要放置一些算法的实现,leet_code以及剑指offer中的代码实现。**

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

对于`[a0, a1, a2, a3]`n个数，给出m次询问，每次给出[l, r]求这个区间内 
a1, a0+a1+a2, a0+a1+a2+a3]`形成新的数组`[b0, b1, b2, b3];（2）如果是 
则只需`b3-b1`

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
