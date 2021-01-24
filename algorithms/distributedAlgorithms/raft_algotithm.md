# raft算法介绍

<!-- vim-markdown-toc Marked -->

* [1.概述](#1.概述)
* [2.原理](#2.原理)
* [3.选举过程详解](#3.选举过程详解)

<!-- vim-markdown-toc -->

## 1.概述

- [博客:一文搞懂raft算法](https://www.cnblogs.com/xybaby/p/10124083.html)
- [动画解释raft算法](http://thesecretlivesofdata.com/raft/)
- raft工程上使用的强一致性、去中心化、高可用的分布式协议
- raft算法是一种`共识算法`, 即多个节点对某一件事情达成一致,即使是在部分节点故障、网络延时、网络分割的情况下

## 2.原理

- raft中的4个子问题：`leader选取(leader election)`, ` log replication`, `safety`, `membership changes`
- 任一时刻一个节点都处于三种状态之一：`leader`, `follower`, `candidate`

1. 所有节点启动时都是follower状态
2. 一段时间内如果没有收到来自leader的心跳，从follower切换到candidate，发起选举
3. 如果收到majority的造成票（含自己的一票）则切换到leader状态
4. 如果发现其他节点比自己更新，则主动切换到follower

## 3.选举过程详解

