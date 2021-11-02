#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.next-permutation
# Date: 2021/11/02
# Filename: next-permutation

__author__ = "Yoshi Truong"
__date__ = "2021/11/02"

from typing import List


def search(desc_arr, val, low=0, high=None):
    high = high or len(desc_arr)
    while low < high:
        mid = (low + high) >> 1
        if desc_arr[mid] <= val:
            high = mid
        else:
            low = mid + 1
    return high


class Solution:
    """https://leetcode.com/problems/next-permutation/"""

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i = l - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        if i < 0:
            nums.sort()
            return
        index = search(nums, nums[i], i + 1) - 1
        nums[i], nums[index] = nums[index], nums[i]
        nums[i + 1:] = nums[l - 1:i:-1]


Solution().nextPermutation([1, 3, 2])
