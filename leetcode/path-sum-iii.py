#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.path-sum-iii
# Date: 2021/11/04
# Filename: path-sum-iii

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"

from collections import Counter
from typing import Optional

from leetcode.datastructure import TreeNode


class Solution:
    """https://leetcode.com/problems/path-sum-iii/"""

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        ans = 0

        def dfs(node, cur_sum, expecting):
            nonlocal ans
            if not node:
                return
            cur_sum += node.val
            ans += expecting[cur_sum]
            expecting[cur_sum + targetSum] += 1
            dfs(node.left, cur_sum, expecting)
            dfs(node.right, cur_sum, expecting)
            expecting[cur_sum + targetSum] -= 1

        dfs(root, 0, Counter([targetSum]))
        return ans


assert Solution().pathSum(TreeNode.build_from_string("[5,4,8,11,null,13,4,7,2,null,null,5,1]"), 22) == 3
