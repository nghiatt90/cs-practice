#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.balanced-binary-tree
# Date: 2023/04/18
# Filename: balanced-binary-tree

__author__ = "Yoshi Truong"
__date__ = "2023/04/18"

from typing import Optional

from leetcode.datastructure import TreeNode


# https://leetcode.com/problems/balanced-binary-tree/
class TreeNodeWithHeight(TreeNode):
    def __init__(self, val=0, left=None, right=None, height=0):
        super().__init__(val, left, right)
        self._height = height

    @property
    def height(self):
        if self._height == 0:
            l = self.left.height if self.left else 0
            r = self.right.height if self.right else 0
            self._height = max(l, r) + 1
        return self._height

    @staticmethod
    def convert(treenode):
        if not treenode:
            return None
        return TreeNodeWithHeight(
            treenode.val,
            TreeNodeWithHeight.convert(treenode.left),
            TreeNodeWithHeight.convert(treenode.right),
        )

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        root = TreeNodeWithHeight.convert(root)
        return self._isBalanced(root)

    def _isBalanced(self, root):
        if not root:
            return True
        l = root.left.height if root.left else 0
        r = root.right.height if root.right else 0
        if abs(l - r) >= 2:
            return False
        return self._isBalanced(root.left) and self._isBalanced(root.right)

