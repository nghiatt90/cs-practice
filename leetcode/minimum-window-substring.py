#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.minimum-window-substring
# Date: 2021/11/02
# Filename: minimum-window-substring

__author__ = "Yoshi Truong"
__date__ = "2021/11/02"

from collections import Counter


class Solution:
    """https://leetcode.com/problems/minimum-window-substring/"""

    def minWindow(self, s: str, t: str) -> str:
        ct = Counter(t)
        min_length = float('inf')
        ans = ''
        r = l = 0
        while r < len(s):
            while any(x > 0 for x in ct.values()) and r < len(s):
                if s[r] in ct:
                    ct[s[r]] -= 1
                r += 1
            while all(x <= 0 for x in ct.values()) and l < len(s):
                if r - l < min_length:
                    min_length = r - l
                    ans = s[l:r]
                if s[l] in ct:
                    ct[s[l]] += 1
                l += 1
        return ans
