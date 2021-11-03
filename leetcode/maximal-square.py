#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.maximal-square
# Date: 2021/11/03
# Filename: maximal-square

__author__ = "Yoshi Truong"
__date__ = "2021/11/03"

from typing import List


class Solution:
    """https://leetcode.com/problems/maximal-square/"""

    def maximalSquare(self, matrix: List[List[str]]) -> int:
        R, C = len(matrix), len(matrix[0])
        dp = [[0] * C for _ in range(R)]

        ans = 0
        for i in range(R):
            dp[i][0] = int(matrix[i][0] == "1")
            ans = max(ans, dp[i][0])
        for j in range(C):
            dp[0][j] = int(matrix[0][j] == "1")
            ans = max(ans, dp[0][j])

        for i in range(1, R):
            for j in range(1, C):
                if matrix[i][j] == "0":
                    continue
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                ans = max(ans, dp[i][j] ** 2)

        return ans
