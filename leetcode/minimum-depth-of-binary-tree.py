#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.minimum-depth-of-binary-tree
# Date: 2023/04/18
# Filename: minimum-depth-of-binary-tree

__author__ = "Yoshi Truong"
__date__ = "2023/04/18"

from typing import Optional

from leetcode.datastructure import TreeNode


# https://leetcode.com/problems/minimum-depth-of-binary-tree/
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        current = [root]
        ans = 0
        while current:
            nexts = []
            ans += 1
            for node in current:
                if not node:
                    continue
                if not node.left and not node.right:
                    return ans
                nexts.append(node.left)
                nexts.append(node.right)
            current = nexts

        return 0
