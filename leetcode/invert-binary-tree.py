#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.invert-binary-tree
# Date: 2021/11/05
# Filename: invert-binary-tree

__author__ = "Yoshi Truong"
__date__ = "2021/11/05"

from typing import Optional

from leetcode.tree import TreeNode


class Solution:
    """https://leetcode.com/problems/invert-binary-tree/"""

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left
        return root
