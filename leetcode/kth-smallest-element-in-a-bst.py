#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.kth-smallest-element-in-a-bst
# Date: 2021/11/05
# Filename: kth-smallest-element-in-a-bst

__author__ = "Yoshi Truong"
__date__ = "2021/11/05"

from typing import Optional

from leetcode.datastructure import TreeNode


def update(node):
    if not node:
        return 0
    l = update(node.left)
    r = update(node.right)
    node.val = (1 + l + r, node.val)
    return node.val[0]


class Solution:
    """https://leetcode.com/problems/kth-smallest-element-in-a-bst/"""

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        update(root)

        def find(node, k):
            if not node:
                return -1
            l = 0 if not node.left else node.left.val[0]
            if k == l + 1:
                return node.val[1]
            if k <= l:
                return find(node.left, k)
            return find(node.right, k - l - 1)

        return find(root, k)
