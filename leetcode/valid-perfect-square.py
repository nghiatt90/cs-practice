#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.valid-perfect-square
# Date: 2023/04/17
# Filename: valid-perfect-square

__author__ = "Yoshi Truong"
__date__ = "2023/04/17"


# https://leetcode.com/problems/valid-perfect-square/


class Solution:

    def sqrt(self, x: int) -> int:
        if x == 1:
            return 1
        hi = x
        lo = 0
        mid = x
        eps = 1e-6
        while hi > lo:
            mid = (hi + lo) / 2
            xx = mid ** 2
            if abs(xx - x) < eps:
                break
            if xx > x:
                hi = mid
            else:
                lo = mid
        return int(mid+eps)

    def isPerfectSquare(self, num: int) -> bool:
        return self.sqrt(num) ** 2 == num



if __name__ == '__main__':
    # assert Solution().isPerfectSquare(16)
    # assert not Solution().isPerfectSquare(14)
    assert Solution().isPerfectSquare(100)