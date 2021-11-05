#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.lowest-common-ancestor-of-a-binary-tree
# Date: 2021/11/05
# Filename: lowest-common-ancestor-of-a-binary-tree

__author__ = "Yoshi Truong"
__date__ = "2021/11/05"

from typing import Optional

from leetcode.tree import TreeNode


class Solution:
    """https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/"""

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> Optional['TreeNode']:
        if not root:
            return None
        if root == p or root == q:
            return root

        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l and r:
            return root

        return l or r
