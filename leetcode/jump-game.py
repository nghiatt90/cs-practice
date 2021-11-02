#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.jump-game
# Date: 2021/11/02
# Filename: jump-game

__author__ = "Yoshi Truong"
__date__ = "2021/11/02"

from typing import List


class Solution:
    """https://leetcode.com/problems/jump-game/"""

    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True

        reach = 0
        pos = 0
        while pos <= reach and pos < len(nums):
            if pos == len(nums) - 1:
                return True
            reach = max(reach, pos + nums[pos])
            pos += 1
        return False
