#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.length-of-last-word
# Date: 2023/04/17
# Filename: length-of-last-word

__author__ = "Yoshi Truong"
__date__ = "2023/04/17"


# https://leetcode.com/problems/length-of-last-word/submissions/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(" ")[-1])
