#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.first-missing-positive
# Date: 2021/11/01
# Filename: first-missing-positive

__author__ = "Yoshi Truong"
__date__ = "2021/11/01"

from typing import List


class Solution:
    """https://leetcode.com/problems/first-missing-positive"""

    def firstMissingPositive(self, nums: List[int]) -> int:
        l = len(nums)
        for i in range(l):
            if nums[i] <= 0:
                nums[i] = 99999999

        for i in range(l):
            v = abs(nums[i])
            if 1 <= v <= l:
                nums[v - 1] = -abs(nums[v - 1])

        for i in range(l):
            if nums[i] > 0:
                return i + 1

        return l + 1


print(Solution().firstMissingPositive([1, 2, 0]))
