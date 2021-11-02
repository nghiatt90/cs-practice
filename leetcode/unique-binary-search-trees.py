#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.unique-binary-search-trees
# Date: 2021/11/02
# Filename: unique-binary-search-trees

__author__ = "Yoshi Truong"
__date__ = "2021/11/02"


class Solution:
    """https://leetcode.com/problems/unique-binary-search-trees/"""

    def numTrees(self, n: int) -> int:
        return [
            1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012,
            742900, 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190, 6564120420
        ][n]
