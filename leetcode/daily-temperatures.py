#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.daily-temperatures
# Date: 2021/11/04
# Filename: daily-temperatures

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"

from typing import List


class Solution:
    """https://leetcode.com/problems/daily-temperatures/"""

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        n = len(temperatures)
        ans = []
        for i in range(n - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()
            if not stack:
                ans.append(0)
            else:
                ans.append(stack[-1] - i)
            stack.append(i)
        return ans[::-1]
