#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.partition-equal-subset-sum
# Date: 2021/11/04
# Filename: partition-equal-subset-sum

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"

from typing import List


class Solution:
    """https://leetcode.com/problems/partition-equal-subset-sum/"""

    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if s & 1:
            return False

        target = s >> 1
        nums.insert(0, 0)
        dp = [[0] * (target + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            for j in range(target + 1):
                if j - nums[i] >= 0:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - nums[i]])
                else:
                    dp[i][j] = dp[i - 1][j]

        return bool(dp[n][target])
