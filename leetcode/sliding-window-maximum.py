#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.sliding-window-maximum
# Date: 2021/11/04
# Filename: sliding-window-maximum

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"

from collections import deque
from typing import List


class Solution:
    """https://leetcode.com/problems/sliding-window-maximum/"""

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        for i, n in enumerate(nums):
            if queue and queue[0] <= i - k:
                queue.popleft()
            while queue and nums[queue[-1]] <= n:
                queue.pop()
            queue.append(i)
            if i >= k - 1:
                yield nums[queue[0]]
