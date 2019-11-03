#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu


"""
使用邻接表表示图
A --> B
A --> C
B --> C
B --> D
C --> D
D --> C
E --> F
F --> C
"""


def find_one_path(graph, start, end, path=[]):
    """
    寻找graph中由start到end顶点的其中一条路径
    graph: dict
    start: str
    end: str
    return: list
    """
    path = path + [start]
    if start == end:
        return path
    if start not in graph.keys():
        return None
    for node in graph[start]:
        if node not in path:  # 保证路径的顶点不重复
            new_path = find_one_path(graph, node, end, path)
            if new_path:
                return new_path
    return path


def find_all_paths(graph, start, end, path=[]):
    """
    寻找graph中由start到end顶点的所有路径
    graph: dict
    start: str
    end: str
    return: [[], ...]
    """
    path = path + [start]
    if start == end:
        return [path]
    if start not in graph.keys():
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            new_paths = find_all_paths(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path) 
    return paths

v  
def find_shortest_path(graph, start, end, path=[]):
    """
    寻找graph中由start到end顶点的最短路径，思路是将如果每次找到了新路径将旧的存储的最短路径对比
    graph: dict
    start: str
    end: str
    return: list
    """
    path = path + [start]
    if start == end:
        return path
    if start not in graph.keys():
        return None
    shortest_path = None
    for node in graph[start]:
        if node not in path:
            new_path = find_shortest_path(graph, node, end, path)
            if new_path:
                if not shortest_path or len(new_path) < len(shortest_path):  # 当有多条最短路径的时候只会记录首条
                    shortest_path = new_path
    return shortest_path


if __name__ == "__main__":
    # 使邻接表定义一个有向图
    graph = {
        "A": ["B", "C"],
        "B": ["C", "D"],
        "C": ["D"],
        "D": ["C"],
        "E": ["F"],
        "F": ["C"]
    }

    print(find_one_path(graph, "A", "D"))  # 结果正确
    print(find_one_path(graph, "B", "F"))  # TODO: 结果应该报错或者怎样

    print(find_all_paths(graph, "A", "D"))
    print(find_shortest_path(graph, "A", "D"))
