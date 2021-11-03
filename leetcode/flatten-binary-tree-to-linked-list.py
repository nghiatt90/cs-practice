#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.flatten-binary-tree-to-linked-list
# Date: 2021/11/03
# Filename: flatten-binary-tree-to-linked-list

__author__ = "Yoshi Truong"
__date__ = "2021/11/03"

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """https://leetcode.com/problems/flatten-binary-tree-to-linked-list/"""

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def rec(node):
            if not node:
                return None
            if not node.left and not node.right:
                return node
            ltail = rec(node.left)
            rtail = rec(node.right)
            if ltail:
                ltail.right = node.right
                node.right = node.left
                node.left = None
            return rtail or ltail or node

        rec(root)
