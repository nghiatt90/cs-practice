#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.find-median-from-data-stream
# Date: 2021/11/04
# Filename: find-median-from-data-stream

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"

from heapq import heappush, heappop


class MedianFinder:
    """https://leetcode.com/problems/find-median-from-data-stream/"""

    def __init__(self):
        self.lheap = []
        self.rheap = []
        self.lsize = 0
        self.rsize = 0

    def addNum(self, num: int) -> None:
        if self.lsize == self.rsize == 0 or -num >= self.lheap[0]:
            heappush(self.lheap, -num)
            self.lsize += 1
        else:
            heappush(self.rheap, num)
            self.rsize += 1
        if self.rsize > self.lsize:
            heappush(self.lheap, -heappop(self.rheap))
            self.rsize -= 1
            self.lsize += 1
        elif self.lsize - self.rsize == 2:
            heappush(self.rheap, -heappop(self.lheap))
            self.rsize += 1
            self.lsize -= 1

    def findMedian(self) -> float:
        if self.lsize > self.rsize:
            return -self.lheap[0]
        return (-self.lheap[0] + self.rheap[0]) / 2


a = MedianFinder()
a.addNum(1)
a.addNum(2)
print(a.findMedian())
print()
a.addNum(3)
print(a.findMedian())
print()
