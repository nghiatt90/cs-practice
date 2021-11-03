#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.maximum-product-subarray
# Date: 2021/11/03
# Filename: maximum-product-subarray

__author__ = "Yoshi Truong"
__date__ = "2021/11/03"

from typing import List


def max_product(arr):
    acc = [1]
    for n in arr:
        acc.append(n * acc[-1])
    if acc[-1] > 0 or len(arr) == 1:
        return acc[-1]
    ret = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            continue
        if i > 0:
            ret = max(ret, acc[i])
        if i < len(arr) - 1:
            ret = max(ret, acc[-1] // acc[i + 1])
    return ret


class Solution:
    """https://leetcode.com/problems/maximum-product-subarray/"""

    def maxProduct(self, nums: List[int]) -> int:
        has_zero = 0 in nums
        nums.append(0)
        sub_arrays = []
        current = []
        for n in nums:
            if n != 0:
                current.append(n)
            elif current:
                sub_arrays.append(current)
                current = []

        if not sub_arrays:
            return 0
        ans = max(max_product(arr) for arr in sub_arrays)
        if ans < 0 and has_zero:
            ans = 0
        return ans
