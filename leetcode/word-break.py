#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.word-break
# Date: 2021/11/03
# Filename: word-break

__author__ = "Yoshi Truong"
__date__ = "2021/11/03"

from typing import List


class Solution:
    """https://leetcode.com/problems/word-break/"""

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            dp[i] = any(dp[j] and s[j:i] in words for j in range(i))
        return dp[n]
