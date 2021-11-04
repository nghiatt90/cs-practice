#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.house-robber-iii
# Date: 2021/11/04
# Filename: house-robber-iii

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"

from typing import Optional

from leetcode.tree import TreeNode


class Solution:
    """https://leetcode.com/problems/house-robber-iii/"""

    def rob(self, root: Optional[TreeNode]) -> int:
        def update(node):
            if not node:
                return 0, 0
            l1, l2 = update(node.left)
            r1, r2 = update(node.right)
            return max(l1, l2) + max(r1, r2), node.val + l1 + r1

        return max(update(root))
