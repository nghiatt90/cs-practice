#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.sqrtx
# Date: 2023/04/17
# Filename: sqrtx

__author__ = "Yoshi Truong"
__date__ = "2023/04/17"


# https://leetcode.com/problems/sqrtx/

class Solution:
    def mySqrt(self, x: int) -> int:
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
        return int(mid)



if __name__ == '__main__':
    assert Solution().mySqrt(4) == 2
    assert Solution().mySqrt(8) == 2
    assert Solution().mySqrt(1) == 1

