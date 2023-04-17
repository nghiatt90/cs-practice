#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.calculate-digit-sum-of-a-string
# Date: 2023/04/17
# Filename: calculate-digit-sum-of-a-string

__author__ = "Yoshi Truong"
__date__ = "2023/04/17"

# https://leetcode.com/problems/calculate-digit-sum-of-a-string/
class Solution:
    def sum(self, num):
        return str(sum(ord(c) - 48 for c in num))

    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            s = "".join(self.sum(s[i:i+k]) for i in range(0, len(s), k))
        return s


if __name__ == '__main__':
    assert Solution().digitSum("11111222223", 3) == "135"