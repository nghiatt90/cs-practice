#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.coin-change
# Date: 2021/11/03
# Filename: coin-change

__author__ = "Yoshi Truong"
__date__ = "2021/11/03"

from functools import lru_cache
from typing import List


@lru_cache(maxsize=None)
def change(n, coins):
    if n == 0:
        return 0
    best = float('inf')
    for coin in coins:
        if coin > n:
            break
        diff = n - coin
        best = min(best, change(diff, coins) + 1)

    return best


class Solution:
    """https://leetcode.com/problems/coin-change/"""

    def coinChange(self, coins: List[int], amount: int) -> int:
        ans = change(amount, tuple(sorted(coins)))
        return ans if ans != float('inf') else -1


print(Solution().coinChange([2], 3))
