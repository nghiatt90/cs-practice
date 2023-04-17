#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.add-binary
# Date: 2023/04/17
# Filename: add-binary

__author__ = "Yoshi Truong"
__date__ = "2023/04/17"


# https://leetcode.com/problems/add-binary/


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2)
        b = int(b, 2)
        return bin(a + b)[2:]


if __name__ == '__main__':
    assert Solution().addBinary("11", "1") == "100"
    assert Solution().addBinary("1010", "1011") == "10101"
