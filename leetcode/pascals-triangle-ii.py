#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.pascals-triangle-ii
# Date: 2023/04/17
# Filename: pascals-triangle-ii

__author__ = "Yoshi Truong"
__date__ = "2023/04/17"

from typing import List
from functools import lru_cache


# https://leetcode.com/problems/pascals-triangle-ii/
class Solution:
    @lru_cache(None)
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        last = self.getRow(rowIndex - 1) + [0]
        return [1] + [last[i] + last[i+1] for i in range(rowIndex)]


if __name__ == '__main__':
    assert Solution().getRow(3) == [1,3,3,1]
    assert Solution().getRow(0) == [1]
    assert Solution().getRow(1) == [1,1]
