#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.partition-labels
# Date: 2021/11/04
# Filename: partition-labels

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"

from collections import defaultdict
from typing import List


class Solution:
    """https://leetcode.com/problems/partition-labels/"""

    def partitionLabels(self, s: str) -> List[int]:
        first, last = defaultdict(lambda: 1000), defaultdict(int)
        for i, c in enumerate(s):
            first[c] = min(first[c], i)
            last[c] = max(last[c], i)
        ranges = []
        for k, v in first.items():
            ranges.append((v, last[k]))
        ranges.sort()
        ranges.append((1000, 1000))
        cur_range = (0, 0)
        ans = []
        for s, e in ranges:
            if s <= cur_range[0] <= e or cur_range[0] <= s <= cur_range[1]:
                cur_range = (min(cur_range[0], s), max(cur_range[1], e))
            else:
                ans.append(cur_range[1] - cur_range[0] + 1)
                cur_range = (s, e)
        return ans
