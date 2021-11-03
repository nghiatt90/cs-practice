#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.construct-binary-tree-from-preorder-and-inorder-traversal
# Date: 2021/11/03
# Filename: construct-binary-tree-from-preorder-and-inorder-traversal

__author__ = "Yoshi Truong"
__date__ = "2021/11/03"

import sys
from typing import List

sys.setrecursionlimit(200)


# def print(*args, **kwargs):
#     pass


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/"""

    def buildTree(self, preorder: List[int], inorder: List[int]):
        node = {v: TreeNode(v) for v in preorder}
        idx = {v: i for i, v in enumerate(inorder)}
        n = len(preorder)

        def build(pl, pr, il, ir, level=''):
            print(level, pl, pr, il, ir)
            if pl >= pr:
                return None
            if pl == pr - 1:
                return node[preorder[pl]]
            root = node[preorder[pl]]
            root_idx = idx[preorder[pl]]
            lsize = root_idx - il
            rsize = ir - root_idx - 1
            print(level, f'lsize = {lsize}; rsize = {rsize}')
            if lsize:
                root.left = build(pl + 1, pl + lsize + 1, il, root_idx, level + '  ')
            if rsize:
                root.right = build(pr - rsize, pr, root_idx + 1, ir, level + '  ')
            return root

        build(0, n, 0, n)
        return node[preorder[0]]


Solution().buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])
