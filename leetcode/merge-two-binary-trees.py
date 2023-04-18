#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.merge-two-binary-trees
# Date: 2021/11/04
# Filename: merge-two-binary-trees

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"

from typing import Optional

from leetcode.datastructure import TreeNode


class Solution:
    """https://leetcode.com/problems/merge-two-binary-trees/"""

    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        new_root = TreeNode(root1.val + root2.val)
        new_root.left = self.mergeTrees(root1.left, root2.left)
        new_root.right = self.mergeTrees(root1.right, root2.right)

        return new_root
