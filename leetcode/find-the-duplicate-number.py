#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.find-the-duplicate-number
# Date: 2021/11/04
# Filename: find-the-duplicate-number

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"

from typing import List


class Solution:
    """https://leetcode.com/problems/find-the-duplicate-number/"""

    def findDuplicate(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            val = abs(nums[i])
            if nums[val - 1] < 0:
                return val
            nums[val - 1] *= -1
        return -1
