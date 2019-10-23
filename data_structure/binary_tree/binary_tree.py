#!/usr/bin/env python
#!coding:utf-8


"""
二叉树的实现
"""


class Node(object):
    """树的节点"""
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right


class BinaryTree(object):
    """二叉树"""
    def __init__(self, root=None):
        self.__root = root

    def add(self, item):
        """为树添加节点,依次从左到右增加"""
        node = Node(item)
        queue = []  # 初始化根节点入队列
        queue.insert(0, self.__root)
        while queue:
            cur = queue.pop(0)
            if cur.left == None:
                cur.left = node
                return
            queue.insert(0, cur.left)
            if cur.right == None:
                cur.right = node
                return
            queue.insert(0, cur.right)

    def travel(self):
        """遍历显示树的节点，广度优先，层次遍历"""
        queue = []
        queue.insert(0, self.__root)
        while queue:
            cur = queue.pop(0)
            print(cur.item)

            if cur.left:
                queue.insert(0, cur.left)
            if cur.right:
                queue.insert(0, cur.right)

    def pre_order(self):
        """使用深度优先的先序遍历进行节点输出,根节点-->左子树-->右子树"""
        root = self.__root
        def preorder(root):
            if not root:
                return None
            print(root.item)
            preorder(root.left)
            preorder(root.right)
        return preorder(root)


def main():
    root_node = Node(1)
    tree = BinaryTree(root_node)
    tree.add(Node(2))
    tree.add(Node(3))
    tree.add(Node(4))
    tree.add(Node(5))
    tree.add(Node(6))
    tree.add(Node(7))

    print("travel*****************")
    tree.travel()
    print("pre_order**************")
    tree.pre_order()


if __name__ == '__main__':
    main()
