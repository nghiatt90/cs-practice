#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.target-sum
# Date: 2021/11/04
# Filename: target-sum

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"

from functools import lru_cache
from typing import List


class Solution:
    """https://leetcode.com/problems/target-sum/"""

    # def findTargetSumWays(self, nums: List[int], target: int) -> int:
    #     n = len(nums)
    #     cnt = 0
    #     for mask in range(1 << n):
    #         total = 0
    #         for i in range(n):
    #             if mask & (1 << i):
    #                 total += nums[i]
    #             else:
    #                 total -= nums[i]
    #         cnt += total == target
    #     return cnt

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(maxsize=None)
        def rec(t, idx):
            if idx < 0:
                return t == 0
            return rec(t + nums[idx], idx - 1) + rec(t - nums[idx], idx - 1)

        return rec(target, len(nums) - 1)


assert Solution().findTargetSumWays([
    42, 36, 4, 15, 17, 15, 31, 1, 11, 2, 12, 28, 22, 9, 2, 31, 48, 18, 48, 5], 15) == 7219
