#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.diameter-of-binary-tree
# Date: 2021/11/04
# Filename: diameter-of-binary-tree

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"

from typing import Optional

from leetcode.datastructure import TreeNode


class Solution:
    """https://leetcode.com/problems/diameter-of-binary-tree/"""

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            if not node:
                return -1
            llength = dfs(node.left)
            rlength = dfs(node.right)
            nonlocal ans
            ans = max(ans, llength + rlength + 2)
            return max(llength, rlength) + 1

        dfs(root)
        return ans


assert Solution().diameterOfBinaryTree(TreeNode.build_from_string("[1,2,3,4,5]")) == 3
