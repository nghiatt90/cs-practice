#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.longest-increasing-subsequence
# Date: 2021/11/04
# Filename: longest-increasing-subsequence

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"

from bisect import bisect_left
from typing import List


class Solution:
    """https://leetcode.com/problems/longest-increasing-subsequence/"""

    # def lengthOfLIS(self, nums: List[int]) -> int:
    #     n = len(nums)
    #     dp = [1] * n
    #     for i in range(n):
    #         for j in range(i):
    #             if nums[i] > nums[j]:
    #                 dp[i] = max(dp[i], dp[j] + 1)
    #     return max(dp)
    def lengthOfLIS(self, nums: List[int]) -> int:
        tail = []  # tail[i] = min element for LIS of length i+1
        for n in nums:
            idx = bisect_left(tail, n)
            if idx < len(tail):
                tail[idx] = n
            else:
                tail.append(n)
        print(tail)
        return len(tail)


assert Solution().lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 6]) == 6
