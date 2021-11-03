#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.longest-consecutive-sequence
# Date: 2021/11/03
# Filename: longest-consecutive-sequence

__author__ = "Yoshi Truong"
__date__ = "2021/11/03"

from typing import List


class Solution:
    """https://leetcode.com/problems/longest-consecutive-sequence/"""

    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = {}

        def get_longest(n):
            if n in longest:
                return longest[n]
            if n + 1 not in s:
                longest[n] = 1
                return longest[n]
            return 1 + get_longest(n + 1)

        return max(get_longest(n) for n in s)
