#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.edit-distance
# Date: 2021/11/01
# Filename: edit-distance

__author__ = "Yoshi Truong"
__date__ = "2021/11/01"


class Solution:
    """https://leetcode.com/problems/edit-distance"""

    def minDistance(self, word1: str, word2: str) -> int:
        l1, l2 = len(word1), len(word2)
        dp = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for r in range(l1 + 1):
            dp[r][0] = r
        for c in range(l2 + 1):
            dp[0][c] = c
        for r in range(1, l1 + 1):
            for c in range(1, l2 + 1):
                dp[r][c] = min((dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])) + 1 if (
                        word1[r - 1] != word2[c - 1]) else dp[r - 1][c - 1]

        return dp[l1][l2]
