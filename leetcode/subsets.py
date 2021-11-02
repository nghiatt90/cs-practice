#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.subsets
# Date: 2021/11/02
# Filename: subsets

__author__ = "Yoshi Truong"
__date__ = "2021/11/02"

from itertools import combinations
from typing import List


class Solution:
    """https://leetcode.com/problems/subsets/submissions/"""

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for i in range(len(nums) + 1):
            for x in combinations(nums, i):
                ans.append(list(x))
        return ans
