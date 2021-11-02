#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.find-first-and-last-position-of-element-in-sorted-array
# Date: 2021/11/02
# Filename: find-first-and-last-position-of-element-in-sorted-array

__author__ = "Yoshi Truong"
__date__ = "2021/11/02"

from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    """https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/"""

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        i = bisect_left(nums, target)
        if i >= len(nums) or nums[i] != target:
            return [-1, -1]
        return [i, bisect_right(nums, target) - 1]
