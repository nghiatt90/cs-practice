#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.course-schedule
# Date: 2021/11/05
# Filename: course-schedule

__author__ = "Yoshi Truong"
__date__ = "2021/11/05"

from collections import defaultdict
from typing import List


class Solution:
    """https://leetcode.com/problems/course-schedule/"""

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = defaultdict(list)
        for v, k in prerequisites:
            adj_list[k].append(v)

        checked = [False] * numCourses

        def dfs(node, path=set()):
            if checked[node]:
                return node not in path
            checked[node] = True
            if not adj_list[node]:
                return True
            path.add(node)
            ret = all(dfs(child, path) for child in adj_list[node])
            path.remove(node)
            return ret

        for i in range(numCourses):
            if not checked[i] and not dfs(i):
                return False
        return True


assert Solution().canFinish(2, [[0, 1]])
