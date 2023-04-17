#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.add-digits
# Date: 2023/04/17
# Filename: add-digits

__author__ = "Yoshi Truong"
__date__ = "2023/04/17"


# https://leetcode.com/problems/add-digits/
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            n = 0
            while num > 0:
                n += num % 10
                num //= 10
            num = n
        return num
