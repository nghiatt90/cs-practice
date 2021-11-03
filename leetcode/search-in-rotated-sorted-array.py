#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.search-in-rotated-sorted-array
# Date: 2021/11/03
# Filename: search-in-rotated-sorted-array

__author__ = "Yoshi Truong"
__date__ = "2021/11/03"

from bisect import bisect_left
from typing import List


class Solution:
    """https://leetcode.com/problems/search-in-rotated-sorted-array/"""

    def search(self, nums: List[int], target: int) -> int:
        is_rotated = nums[0] > nums[-1]
        if not is_rotated:
            idx = bisect_left(nums, target)
            return idx if idx < len(nums) and nums[idx] == target else -1

        l, r = 0, len(nums)
        while l < r:
            mid = (l + r) >> 1
            if nums[mid] > nums[-1]:
                l = mid + 1
            else:
                r = mid

        if target >= nums[0]:
            idx = bisect_left(nums, target, 0, r)
            return idx if idx < len(nums) and nums[idx] == target else -1

        idx = bisect_left(nums, target, r)
        return idx if idx < len(nums) and nums[idx] == target else -1


assert Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=0) == 4
assert Solution().search(nums=[4, 5, 6, 7, 0, 1, 2], target=3) == -1
