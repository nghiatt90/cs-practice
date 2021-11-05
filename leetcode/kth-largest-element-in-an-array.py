#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.kth-largest-element-in-an-array
# Date: 2021/11/05
# Filename: kth-largest-element-in-an-array

__author__ = "Yoshi Truong"
__date__ = "2021/11/05"

from typing import List


class Solution:
    """https://leetcode.com/problems/kth-largest-element-in-an-array/"""

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[-k]
