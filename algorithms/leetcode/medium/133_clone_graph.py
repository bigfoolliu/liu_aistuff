#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph. Each node in the graph contains a val (int) and a list (List[Node]) of its neighbors.

Input:
{"$id":"1","neighbors":[{"$id":"2","neighbors":[{"$ref":"1"},{"$id":"3","neighbors":[{"$ref":"2"},{"$id":"4","neighbors":[{"$ref":"3"},{"$ref":"1"}],"val":4}],"val":3}],"val":2},{"$ref":"4"}],"val":1}

Explanation:
Node 1's value is 1, and it has two neighbors: Node 2 and 4.
Node 2's value is 2, and it has two neighbors: Node 1 and 3.
Node 3's value is 3, and it has two neighbors: Node 2 and 4.
Node 4's value is 4, and it has two neighbors: Node 1 and 3.
 

Note:

The number of nodes will be between 1 and 100.
The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
You must return the copy of the given node as a reference to the cloned graph.

https://leetcode-cn.com/problems/clone-graph/
给定无向连通图中一个节点的引用，返回该图的深拷贝（克隆）。图中的每个节点都包含它的值 val（Int） 和其邻居neighbors的列表（list[Node]）。
"""


class Node(object):

    def __init__(self, val, neighbors=None):
        """
        val:
        neighbors: list
        """
        self.val = val
        self.neighbors = neighbors


def clone_graph(node):
    """
    使用深度优先遍历图节点然后将其复制，
    为每个节点创建副本到哈希表
    node: Node
    """
    d = {}
    def dfs(old):
        if old not in in d:
            d[old] = new = Node(old.val, None)
            new.neighbors = [*map(dfs, old.neighbors)]
        return d[old]
    return dfs(node)


def clone_graph2(node):
    """
    使用copy模块来复制
    node: Node
    """
    import copy
    return copy.deepcopy(node)


if __name__ == "__main__":
    pass
