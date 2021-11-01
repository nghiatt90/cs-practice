#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.group-anagrams
# Date: 2021/11/01
# Filename: group-anagrams

__author__ = "Yoshi Truong"
__date__ = "2021/11/01"

from collections import Counter, defaultdict
from typing import List


def hash_t(s):
    c = Counter(s)
    return tuple(c[i] for i in 'abcdefghijklmnopqrstuvwxyz')


class Solution:
    """https://leetcode.com/problems/group-anagrams"""

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = defaultdict(list)
        for s in strs:
            sets[hash_t(s)].append(s)
        return sets.values()
