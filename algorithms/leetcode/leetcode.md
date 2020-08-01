# leetcode

<!-- vim-markdown-toc Marked -->

* [1.参考](#1.参考)
* [2.解法分类以及刷题顺序](#2.解法分类以及刷题顺序)
        - [2.1Pattern: Sliding window，滑动窗口类型](#2.1pattern:-sliding-window，滑动窗口类型)
        - [2.2Pattern: two points, 双指针类型](#2.2pattern:-two-points,-双指针类型)
        - [2.3Pattern: Fast & Slow pointers, 快慢指针类型](#2.3pattern:-fast-&-slow-pointers,-快慢指针类型)
        - [2.4Pattern: Merge Intervals，区间合并类型](#2.4pattern:-merge-intervals，区间合并类型)
        - [2.5Pattern: Cyclic Sort，循环排序](#2.5pattern:-cyclic-sort，循环排序)
        - [2.6Pattern: In-place Reversal of a LinkedList，链表翻转](#2.6pattern:-in-place-reversal-of-a-linkedlist，链表翻转)
        - [2.7Pattern: Tree Breadth First Search，树上的BFS](#2.7pattern:-tree-breadth-first-search，树上的bfs)
        - [2.8Pattern: Tree Depth First Search，树上的DFS](#2.8pattern:-tree-depth-first-search，树上的dfs)
        - [2.9Pattern: Two Heaps，双堆类型](#2.9pattern:-two-heaps，双堆类型)
        - [2.10Pattern: Subsets，子集类型，一般都是使用多重DFS](#2.10pattern:-subsets，子集类型，一般都是使用多重dfs)
        - [2.11Pattern: Modified Binary Search，改造过的二分](#2.11pattern:-modified-binary-search，改造过的二分)
        - [2.12Pattern: Top ‘K’ Elements，前K个系列](#2.12pattern:-top-‘k’-elements，前k个系列)
        - [2.13Pattern: K-way merge，多路归并](#2.13pattern:-k-way-merge，多路归并)
        - [2.14Pattern: 0/1 Knapsack (Dynamic Programming)，0/1背包类型](#2.14pattern:-0/1-knapsack-(dynamic-programming)，0/1背包类型)
        - [2.15Pattern: Topological Sort (Graph)，拓扑排序类型](#2.15pattern:-topological-sort-(graph)，拓扑排序类型)
        - [2.16DP：动态规划](#2.16dp：动态规划)
                + [2.16.10/1 Knapsack, 0/1背包](#2.16.10/1-knapsack,-0/1背包)
                + [2.16.2Unbounded Knapsack，无限背包](#2.16.2unbounded-knapsack，无限背包)
                + [2.16.3Fibonacci Numbers，斐波那契数列](#2.16.3fibonacci-numbers，斐波那契数列)
                + [2.16.4Palindromic Subsequence，回文子系列](#2.16.4palindromic-subsequence，回文子系列)
                + [2.16.5Longest Common Substring，最长子字符串系列](#2.16.5longest-common-substring，最长子字符串系列)

<!-- vim-markdown-toc -->

## 1.参考

- [leetcode github解法](https://github.com/azl397985856/leetcode)
- [leetcode全部解法](https://github.com/csujedihy/lc-all-solutions)

## 2.解法分类以及刷题顺序

- [Patterns for Coding Questions](https://www.educative.io/courses/grokking-the-coding-interview?aff=K7qB)
- [知乎Leetcode刷题顺序，看这一篇就够了](https://zhuanlan.zhihu.com/p/161036474)

### 2.1Pattern: Sliding window，滑动窗口类型

- 通常是执行数组或者链表某个区间（窗口上的操作）
- 这个问题的输入是一些线性结构：比如链表呀，数组啊，字符串啊之类的
- 让你去求最长/最短子字符串或是某些特定的长度要求 

### 2.2Pattern: two points, 双指针类型

- 两个指针朝着左右方向移动（同向或者异向），直至他们满足某种条件
- 通常用在排好序的数组或是链表中寻找对子
- 一般来说，数组或是链表是排好序的，你得在里头找一些组合满足某种限制条件, 这种组合可能是一对数，三个数，或是一个子数组

### 2.3Pattern: Fast & Slow pointers, 快慢指针类型

- 两个指针的在数组上（或是链表上，序列上）的移动速度不一样,解决有环的链表和数组时特别有用
- 问题需要处理环上的问题，比如环形链表和环形数组, 当你需要知道链表的长度或是某个特别位置的信息的时候

### 2.4Pattern: Merge Intervals，区间合并类型

- 处理有区间重叠的
- 当你需要产生一堆相互之间没有交集的区间的时候, 当你听到重叠区间的时候

### 2.5Pattern: Cyclic Sort，循环排序

- 处理数组中的数值限定在一定的区间的问题
- 这些问题一般设计到排序好的数组，而且数值一般满足于一定的区间
- 如果问题让你需要在排好序/翻转过的数组中，寻找丢失的/重复的/最小的元素

### 2.6Pattern: In-place Reversal of a LinkedList，链表翻转

- 需要去翻转链表，要求不能使用额外空间的时候

### 2.7Pattern: Tree Breadth First Search，树上的BFS

- 基于广度搜索（Breadth First Search (BFS)），适用于需要遍历一颗树。借助于队列数据结构，从而能保证树的节点按照他们的层数打印出来
- 遍历树，需要按层操作的方式（也称作层序遍历）

### 2.8Pattern: Tree Depth First Search，树上的DFS

- 树形DFS基于深搜（Depth First Search (DFS)）技术来实现树的遍历
- 你需要按前中后序的DFS方式遍历树, 如果该问题的解一般离叶子节点比较近

### 2.9Pattern: Two Heaps，双堆类型

- 该模式用到了两个堆，一个最小堆用来找最小元素；一个最大堆
- 这种模式在优先队列，计划安排问题（Scheduling）中有奇效
- 如果问题让你找一组数中的最大/最小/中位数, 涉及到二叉树数据结构时也特别有用

### 2.10Pattern: Subsets，子集类型，一般都是使用多重DFS

- 问题需要咱们去找数字的组合或是排列

### 2.11Pattern: Modified Binary Search，改造过的二分

- 问题的输入是排好序的数组，链表，或是排好序的矩阵，要求咱们寻找某些特定元素

### 2.12Pattern: Top ‘K’ Elements，前K个系列

- 求解最大/最小/最频繁的K个元素
- 如果你需要求最大/最小/最频繁的前K个元素, 或者你需要通过排序去找一个特定的数

### 2.13Pattern: K-way merge，多路归并

- 解决那些涉及到多组排好序的数组
- 该问题的输入是排好序的数组，链表或是矩阵, 让咱们合并多个排好序的集合，或是需要找这些集合中最小的元素

### 2.14Pattern: 0/1 Knapsack (Dynamic Programming)，0/1背包类型

### 2.15Pattern: Topological Sort (Graph)，拓扑排序类型

- 用来寻找一种线性的顺序，这些元素之间具有依懒性
- 待解决的问题需要处理无环图, 需要以一种有序的秩序更新输入元素, 需要处理的输入遵循某种特定的顺序

### 2.16DP：动态规划

#### 2.16.10/1 Knapsack, 0/1背包

#### 2.16.2Unbounded Knapsack，无限背包

#### 2.16.3Fibonacci Numbers，斐波那契数列

#### 2.16.4Palindromic Subsequence，回文子系列

#### 2.16.5Longest Common Substring，最长子字符串系列
