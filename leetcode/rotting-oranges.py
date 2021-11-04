#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.rotting-oranges
# Date: 2021/11/04
# Filename: rotting-oranges

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"

from typing import List


class Solution:
    """https://leetcode.com/problems/rotting-oranges/"""

    def orangesRotting(self, grid: List[List[int]]) -> int:
        bad = []
        R, C = len(grid), len(grid[0])
        good_count = 0
        checked = [[1] * C for _ in range(R)]
        for i in range(R):
            for j in range(C):
                if grid[i][j] == 2:
                    bad.append((i, j))
                if grid[i][j] == 1:
                    checked[i][j] = 0
                    good_count += 1

        step = 0
        while bad and good_count:
            next_bad = []
            step += 1
            for i, j in bad:
                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C and not checked[ni][nj]:
                        good_count -= 1
                        next_bad.append((ni, nj))
                        checked[ni][nj] = 1
            bad = next_bad
        return step if good_count == 0 else -1
