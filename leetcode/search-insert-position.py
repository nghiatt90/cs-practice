#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.search-insert-position
# Date: 2021/11/02
# Filename: search-insert-position

__author__ = "Yoshi Truong"
__date__ = "2021/11/02"

from bisect import bisect_left
from typing import List


class Solution:
    """https://leetcode.com/problems/search-insert-position/"""

    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)
