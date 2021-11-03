#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.perfect-squares
# Date: 2021/11/03
# Filename: perfect-squares

__author__ = "Yoshi Truong"
__date__ = "2021/11/03"

import sys
from functools import lru_cache

sys.setrecursionlimit(100000)


class Solution:
    """https://leetcode.com/problems/perfect-squares/"""

    @lru_cache(maxsize=None)
    def numSquares(self, n: int) -> int:
        if n == 0:
            return 0
        best = n
        for i in range(1, 102):
            if i ** 2 > n:
                return best
            diff = n - i ** 2
            best = min(best, self.numSquares(diff) + 1)

        return best


print(Solution().numSquares(2000))
