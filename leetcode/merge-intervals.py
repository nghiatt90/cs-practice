#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.merge-intervals
# Date: 2021/11/01
# Filename: merge-intervals

__author__ = "Yoshi Truong"
__date__ = "2021/11/01"

from typing import List


class Solution:
    """https://leetcode.com/problems/merge-intervals"""

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        intervals.sort()
        ans = [intervals[0]]
        for s, e in intervals:
            ls, le = ans[-1]
            if ls <= s <= le or s <= ls <= e or ls <= e <= le or s <= le <= e:
                ans[-1] = [min(s, ls), max(e, le)]
            else:
                ans.append([s, e])
        return ans
