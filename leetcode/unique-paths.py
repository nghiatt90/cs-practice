#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.unique-paths
# Date: 2021/11/02
# Filename: unique-paths

__author__ = "Yoshi Truong"
__date__ = "2021/11/02"


class Solution:
    """https://leetcode.com/problems/unique-paths/"""

    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[m - 1][n - 1]
