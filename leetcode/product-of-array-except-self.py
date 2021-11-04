#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.product-of-array-except-self
# Date: 2021/11/04
# Filename: product-of-array-except-self

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"

from typing import List


class Solution:
    """https://leetcode.com/problems/product-of-array-except-self/"""

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1]
        for i, n in enumerate(nums[:-1]):
            ans.append(ans[-1] * n)
        i = len(nums) - 1
        n = 1
        while i >= 0:
            ans[i] *= n
            n *= nums[i]
            i -= 1
        return ans
