#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.minimum-path-sum
# Date: 2021/11/02
# Filename: minimum-path-sum

__author__ = "Yoshi Truong"
__date__ = "2021/11/02"

from typing import List


class Solution:
    """https://leetcode.com/problems/minimum-path-sum/"""

    def minPathSum(self, dp: List[List[int]]) -> int:
        m, n = len(dp), len(dp[0])
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                if i == 0:
                    dp[i][j] += dp[i][j - 1]
                elif j == 0:
                    dp[i][j] += dp[i - 1][j]
                else:
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
        return dp[m - 1][n - 1]
