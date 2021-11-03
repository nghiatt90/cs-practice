#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.binary-tree-inorder-traversal
# Date: 2021/11/03
# Filename: binary-tree-inorder-traversal

__author__ = "Yoshi Truong"
__date__ = "2021/11/03"

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """https://leetcode.com/problems/binary-tree-inorder-traversal/"""

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def rec(node):
            if not node:
                return
            rec(node.left)
            ans.append(node.val)
            rec(node.right)

        rec(root)
        return ans
