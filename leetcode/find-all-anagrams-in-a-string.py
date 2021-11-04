#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.find-all-anagrams-in-a-string
# Date: 2021/11/04
# Filename: find-all-anagrams-in-a-string

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"

from collections import Counter
from typing import List


class Solution:
    """https://leetcode.com/problems/find-all-anagrams-in-a-string/"""

    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        cp = Counter(p)
        lp = len(p)
        cs = Counter(s[:lp])
        ans = [0] if cs == cp else []
        for i in range(lp, len(s)):
            cs[s[i]] += 1
            cs[s[i - lp]] -= 1
            if not (cs - cp):
                ans.append(i - lp + 1)
        return ans


print(Solution().findAnagrams(s="cbaebabacd", p="abc"))
