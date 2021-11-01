#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.largest-rectangle-in-histogram
# Date: 2021/11/01
# Filename: largest-rectangle-in-histogram

__author__ = "Yoshi Truong"
__date__ = "2021/11/01"

from typing import List


class Solution:
    """https://leetcode.com/problems/largest-rectangle-in-histogram/"""

    def largestRectangleArea(self, heights: List[int]) -> int:
        heights = [0] + heights + [0]
        stack = []
        max_area = 0
        for r, h in enumerate(heights):
            while stack and heights[stack[-1]] > h:
                x = heights[stack.pop()]
                area = x * (r - stack[-1] - 1)
                max_area = max(max_area, area)
            stack.append(r)
        return max_area


print(Solution().largestRectangleArea([2, 1, 2]))
