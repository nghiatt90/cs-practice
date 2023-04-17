#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.find-triangular-sum-of-an-array
# Date: 2023/04/17
# Filename: find-triangular-sum-of-an-array

__author__ = "Yoshi Truong"
__date__ = "2023/04/17"

from typing import List


# https://leetcode.com/problems/find-triangular-sum-of-an-array/
class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return self.triangularSum([(nums[i-1] + nums[i]) % 10 for i in range(1, len(nums))])


if __name__ == '__main__':
    assert Solution().triangularSum([1,2,3,4,5]) == 8
    assert Solution().triangularSum([5]) == 5