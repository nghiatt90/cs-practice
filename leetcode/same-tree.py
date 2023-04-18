#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.same-tree
# Date: 2023/04/18
# Filename: same-tree

__author__ = "Yoshi Truong"
__date__ = "2023/04/18"

from typing import Optional

from leetcode.datastructure import TreeNode


# https://leetcode.com/problems/same-tree/
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == '__main__':
    t1 = TreeNode.build_from_string('[1,2,3]')
    t2 = TreeNode.build_from_string('[1,2,3]')
    assert Solution().isSameTree(t1, t2)

    t1 = TreeNode.build_from_string('[1,2]')
    t2 = TreeNode.build_from_string('[1,null,2]')
    assert not Solution().isSameTree(t1, t2)

    t1 = TreeNode.build_from_string('[1,2,1]')
    t2 = TreeNode.build_from_string('[1,1,2]')
    assert not Solution().isSameTree(t1, t2)