#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.combination-sum
# Date: 2021/11/02
# Filename: combination-sum

__author__ = "Yoshi Truong"
__date__ = "2021/11/02"

from typing import List


def rec(target, candidates, idx, path):
    if target == 0:
        return [path]
    if target < 0 or idx < 0:
        return []
    return rec(target - candidates[idx], candidates, idx, path + [candidates[idx]]) + rec(target, candidates, idx - 1,
                                                                                          path)


class Solution:
    """https://leetcode.com/problems/combination-sum/"""

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return rec(target, candidates, len(candidates) - 1, [])
