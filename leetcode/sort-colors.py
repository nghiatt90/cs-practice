#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.sort-colors
# Date: 2021/11/02
# Filename: sort-colors

__author__ = "Yoshi Truong"
__date__ = "2021/11/02"

from typing import List


class Solution:
    """https://leetcode.com/problems/sort-colors/"""

    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1
        i = 0
        while i < len(nums):
            if nums[i] == 0 and i > l:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
                i -= 1
            elif nums[i] == 2 and i < r:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
                i -= 1
            i += 1
