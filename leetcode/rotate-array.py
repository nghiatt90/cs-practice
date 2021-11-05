#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.rotate-array
# Date: 2021/11/04
# Filename: rotate-array

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"

from typing import List


class Solution:
    """https://leetcode.com/problems/rotate-array/"""

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return
        n = len(nums)
        k %= n

        swap_count = 0
        start = 0
        while swap_count < n - 1:
            idx = start
            while swap_count < n - 1:
                dest = (idx + k) % n
                nums[start], nums[dest] = nums[dest], nums[start]
                swap_count += 1
                idx = dest
                if idx == start:
                    start += 1
                    break


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
Solution().rotate(nums, k)
