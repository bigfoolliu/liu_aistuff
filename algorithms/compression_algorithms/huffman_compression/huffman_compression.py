#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# author: bigfoolliu

"""
Use serveral ways to compress string `everyday is awesome!`
1. use simple bits to replace ASCII value
2. use huffman coding
"""
import heapq
import collections


def get_rate(compressed_binary, uncompressed_bits):
    return len(compressed_binary) * 100 / uncompressed_bits


class SimpleCompression(object):

    def __init__(self, string):
        self.symbols = set(string)
        self.bit_len = 1
        while 2**self.bit_len < len(self.symbols):
            self.bit_len += 1
        self.string = string

        self.s2b = {}
        self.b2s = {}
        i = 0
        for s in self.symbols:
            b = bin(i)[2:]
            if len(b) < self.bit_len:
                b = (self.bit_len - len(b)) * '0' + b
            self.s2b[s] = b
            self.b2s[b] = s
            i += 1

    def compress(self):
        bits = ''
        for s in self.string:
            bits += self.s2b[s]
        return bits

    def uncompress(self, bits):
        string = ''
        for i in range(0, len(bits), self.bit_len):
            string += self.b2s[bits[i:i + self.bit_len]]
        return string


class HuffmanCompression(object):

    class Trie:
        def __init__(self, val, char=''):
            self.val = val
            self.char = char
            self.coding = ''
            self.left = self.right = None

        def __eq__(self, other):
            return self.val == other.val

        def __lt__(self, other):
            return self.val < other.val

        def __gt__(self, other):
            return self.val > other.val

    def __init__(self, string):
        self.string = string
        counter = collections.Counter(string)
        heap = []
        for char, cnt in counter.items():
            heapq.heappush(heap, HuffmanCompression.Trie(cnt, char))

        while len(heap) != 1:
            left = heapq.heappop(heap)
            right = heapq.heappop(heap)
            trie = HuffmanCompression.Trie(left.val + right.val)
            trie.left, trie.right = left, right
            heapq.heappush(heap, trie)

        self.root = heap[0]
        self.s2b = {}
        self.bfs_encode(self.root, self.s2b)

    def bfs_encode(self, root, s2b):
        queue = collections.deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node.char:
                s2b[node.char] = node.coding
                continue
            if node.left:
                node.left.coding = node.coding + '0'
                queue.append(node.left)
            if node.right:
                node.right.coding = node.coding + '1'
                queue.append(node.right)

    def compress(self):
        bits = ''
        for char in self.string:
            bits += self.s2b[char]
        return bits

    def uncompress(self, bits):
        string = ''
        root = self.root
        for bit in bits:
            if bit == '0':
                root = root.left
            else:
                root = root.right
            if root.char:
                string += root.char
                root = self.root
        return string


if __name__ == '__main__':
    s = 'everyday is awesome!'
    # ASCII
    bits = len(s) * 8
    print('Total bits: %d' % bits)

    # simple compression
    sc = SimpleCompression(s)
    compressed = sc.compress()
    print('Compressed binary: ' + compressed)
    print('Uncompressed: ' + sc.uncompress(compressed))
    print(sc.s2b)
    print('Simple Compression-compress rate: %d%%' % get_rate(compressed, bits))

    print('===================')
    # huffman compression
    hc = HuffmanCompression(s)
    compressed = hc.compress()
    print('Compressed binary: ' + compressed)
    print('Uncompressed: ' + hc.uncompress(compressed))
    print(hc.s2b)
    print('Huffman Compression-compress rate: %d%%' % get_rate(compressed, bits))
