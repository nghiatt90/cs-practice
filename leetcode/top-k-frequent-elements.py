#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.top-k-frequent-elements
# Date: 2021/11/03
# Filename: top-k-frequent-elements

__author__ = "Yoshi Truong"
__date__ = "2021/11/03"

from collections import Counter
from typing import List


class Solution:
    """https://leetcode.com/problems/top-k-frequent-elements/"""

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [x[0] for x in Counter(nums).most_common(k)]
