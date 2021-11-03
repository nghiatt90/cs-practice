#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.binary-tree-maximum-path-sum
# Date: 2021/11/03
# Filename: binary-tree-maximum-path-sum

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
    """https://leetcode.com/problems/binary-tree-maximum-path-sum/"""

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = -float('inf')

        def get_sum(node):
            nonlocal ans
            if not node:
                return 0
            lsum = get_sum(node.left)
            rsum = get_sum(node.right)
            ans = max(ans, node.val + max(lsum, rsum, 0), node.val + lsum + rsum)
            node.val += max(lsum, rsum, 0)
            return node.val

        get_sum(root)
        return ans
