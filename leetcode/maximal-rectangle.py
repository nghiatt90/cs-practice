#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.maximal-rectangle
# Date: 2021/11/01
# Filename: maximal-rectangle

__author__ = "Yoshi Truong"
__date__ = "2021/11/01"

from typing import List


def largestRectangleArea(heights: List[int]) -> int:
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


class Solution:
    """https://leetcode.com/problems/maximal-rectangle"""

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        r = [int(x) for x in matrix[0]]
        max_area = largestRectangleArea(r)
        for i in range(1, len(matrix)):
            r = [r[j] + 1 if matrix[i][j] == "1" else 0 for j in range(len(matrix[0]))]
            max_area = max(max_area, largestRectangleArea(r))
        return max_area


matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
print(Solution().maximalRectangle(matrix))
