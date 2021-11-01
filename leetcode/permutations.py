#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.permutations.py
# Date: 2021/11/01
# Filename: permutations.py

__author__ = "Yoshi Truong"
__date__ = "2021/11/01"


from itertools import permutations
from typing import List


class Solution:
    """https://leetcode.com/problems/permutations/"""
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(permutations(nums))


s = Solution()
tests = [
    [1, 2, 3],
    [0, 1],
    [1]
]
for nums in tests:
    print(s.permute(nums))
