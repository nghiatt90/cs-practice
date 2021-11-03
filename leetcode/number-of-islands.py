#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.number-of-islands
# Date: 2021/11/03
# Filename: number-of-islands

__author__ = "Yoshi Truong"
__date__ = "2021/11/03"

from typing import List


class Solution:
    """https://leetcode.com/problems/number-of-islands/"""

    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])
        checked = [[0] * C for _ in range(R)]
        count = 0
        for i in range(R):
            for j in range(C):
                if checked[i][j] or grid[i][j] == '0':
                    continue
                stack = [(i, j)]
                count += 1
                while stack:
                    r, c = stack.pop()
                    for rr, cc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        nr, nc = r + rr, c + cc
                        if 0 <= nr < R and 0 <= nc < C and not checked[nr][nc] and grid[nr][nc] == '1':
                            stack.append((nr, nc))
                            checked[nr][nc] = 1
        return count
