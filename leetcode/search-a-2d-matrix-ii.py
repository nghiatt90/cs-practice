#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.search-a-2d-matrix-ii
# Date: 2021/11/04
# Filename: search-a-2d-matrix-ii

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"

from bisect import bisect_left
from typing import List


class Solution:
    """https://leetcode.com/problems/search-a-2d-matrix-ii/"""

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            if row[0] > target:
                break
            idx = bisect_left(row, target)
            if idx < len(row) and row[idx] == target:
                return True
        return False
