#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.subarray-sum-equals-k
# Date: 2021/11/04
# Filename: subarray-sum-equals-k

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"

from collections import defaultdict
from typing import List


class Solution:
    """https://leetcode.com/problems/subarray-sum-equals-k/"""

    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[k] = 1
        acc = [0]
        ans = 0
        for n in nums:
            acc.append(n + acc[-1])
            ans += freq[acc[-1]]
            freq[acc[-1] + k] += 1

        # print(acc, freq, ans)
        return ans


assert Solution().subarraySum(nums=[1, 1, 1], k=2) == 2
