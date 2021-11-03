#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.majority-element
# Date: 2021/11/03
# Filename: majority-element

__author__ = "Yoshi Truong"
__date__ = "2021/11/03"

from collections import Counter
from typing import List


class Solution:
    """https://leetcode.com/problems/majority-element/"""

    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]
