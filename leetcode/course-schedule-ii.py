#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.course-schedule-ii
# Date: 2021/11/05
# Filename: course-schedule-ii

__author__ = "Yoshi Truong"
__date__ = "2021/11/05"

from collections import defaultdict
from typing import List


class Solution:
    """https://leetcode.com/problems/course-schedule-ii/"""

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        incoming = [0] * numCourses
        edges = defaultdict(list)
        for v, k in prerequisites:
            edges[k].append(v)
            incoming[v] += 1

        # Kahn's algorithm
        ans = []
        sources = [x for x in range(numCourses) if incoming[x] == 0]
        while sources:
            s = sources.pop()
            ans.append(s)
            while edges[s]:
                e = edges[s].pop()
                incoming[e] -= 1
                if incoming[e] == 0:
                    sources.append(e)

        if any(incoming):
            # Has cycle, cannot sort
            return []

        return ans
