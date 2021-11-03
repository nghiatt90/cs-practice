#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.implement-trie-prefix-tree
# Date: 2021/11/03
# Filename: implement-trie-prefix-tree

__author__ = "Yoshi Truong"
__date__ = "2021/11/03"


class Node:
    def __init__(self, count=0):
        self.end_count = count
        self.children = {}


class Trie:
    """https://leetcode.com/problems/implement-trie-prefix-tree/"""

    def __init__(self):
        self.root = Node(1)

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()
            node = node.children[c]
        node.end_count += 1

    def search(self, word: str) -> bool:
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.end_count > 0

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

obj = Trie()
obj.insert('apple')
obj.search('apple')
