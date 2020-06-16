#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
邻接矩阵

定点个数为V，则邻接矩阵可以使用V x V的二维数组表示；
g[i][j]表示定点i和定点j的关系；
无向图可以使用0/1表示是否有连接；
带权图使用INF表示；
"""
V = 4
g = [[0 for _ in range(V)] for _ in range(V)]

print(g)


class DirectedGraphNode(object):

    """有向图"""

    def __init__(self, x):
        self.label = x
        self.neighbors = []


class UnDirectedGraphNode(object):

    """无向图，只是在建图的时候双向同时加"""

    def __init__(self, x):
        self.label = x
        self.neighbors = []
