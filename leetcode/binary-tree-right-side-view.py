#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.binary-tree-right-side-view
# Date: 2021/11/05
# Filename: binary-tree-right-side-view

__author__ = "Yoshi Truong"
__date__ = "2021/11/05"

from typing import Optional, List

from leetcode.datastructure import TreeNode


class Solution:
    """https://leetcode.com/problems/binary-tree-right-side-view/"""

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = [root]
        ans = []
        while queue:
            ans.append(queue[-1].val)
            next_queue = []
            for node in queue:
                if node.left:
                    next_queue.append(node.left)
                if node.right:
                    next_queue.append(node.right)
            queue = next_queue
        return ans
