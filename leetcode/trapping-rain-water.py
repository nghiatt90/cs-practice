#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.trapping-rain-water
# Date: 2021/11/02
# Filename: trapping-rain-water

__author__ = "Yoshi Truong"
__date__ = "2021/11/02"

import sys
from typing import List

sys.setrecursionlimit(20)


# def print(*args, **kwargs):
#     pass


class SegmentTreeMaximum(object):
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [(-1, -1)] * (2 * self.n)
        for i in range(self.n):
            self.tree[self.n + i] = (arr[i], i)
        self.build()

    def build(self):
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = max(self.tree[i << 1], self.tree[i << 1 | 1])

    def update(self, i, value):
        t = self.n + i
        self.tree[t] = value
        while t > 1:
            self.tree[t >> 1] = max(self.tree[t], self.tree[t ^ 1])
            t >>= 1

    def query(self, l, r):
        res = (-float('inf'), -1)
        l += self.n
        r += self.n
        while l < r:
            if l & 1:
                res = max(self.tree[l], res)
                l += 1
            if r & 1:
                r -= 1
                res = max(self.tree[r], res)
            l >>= 1
            r >>= 1
        return res


class Solution:
    """https://leetcode.com/problems/trapping-rain-water/"""

    def trap(self, height: List[int]) -> int:
        rmq = SegmentTreeMaximum(height)
        total = 0

        def rec(l, r, level=''):
            print(level, l, r)
            nonlocal total
            if l >= r - 2:
                return
            h1, p1 = rmq.query(l, r)
            print(level, f'p1 = {p1}')
            if p1 != l:
                hl, pl = rmq.query(l, p1)
                print(level, f'pl = {pl}')
                total += sum(hl - height[i] for i in range(pl + 1, p1))
                print(level, f'total = {total}')
                rec(l, pl + 1, level + '  ')
            if p1 != r - 1:
                hr, pr = rmq.query(p1 + 1, r)
                print(level, f'pr = {pr}')
                total += sum(hr - height[i] for i in range(p1 + 1, pr))
                print(level, f'total = {total}')
                rec(pr, r, level + '  ')

        rec(0, len(height))
        return total


assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert Solution().trap([0, 2, 0]) == 0
assert Solution().trap([5, 4, 1, 2]) == 1
