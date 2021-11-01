#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.rotate-image
# Date: 2021/11/01
# Filename: rotate-image

__author__ = "Yoshi Truong"
__date__ = "2021/11/01"

from typing import List


class Solution:
    """https://leetcode.com/problems/rotate-image/"""

    def rotate_ring(self, matrix, ring_id):
        if ring_id >= (len(matrix) // 2):
            return
        s = len(matrix)
        e = s - ring_id - 1
        # Rotate once
        t = matrix[ring_id][ring_id]
        for r in range(ring_id + 1, e + 1):
            matrix[r - 1][ring_id] = matrix[r][ring_id]
        for c in range(ring_id + 1, e + 1):
            matrix[e][c - 1] = matrix[e][c]
        for r in range(e - 1, ring_id - 1, -1):
            matrix[r + 1][e] = matrix[r][e]
        for c in range(e - 1, ring_id - 1, -1):
            matrix[ring_id][c + 1] = matrix[ring_id][c]
        matrix[ring_id][ring_id + 1] = t

        # for i in range(s):
        #     print(' '.join('%2d' % n for n in matrix[i]))
        # print('=' * 30)

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if not matrix:
            return
        size = len(matrix)  # Matrix is square
        for i in range(size):
            rotation_count = size - i * 2 - 1
            for _ in range(rotation_count):
                self.rotate_ring(matrix, i)


s = Solution()
tests = [
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
     [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
    ([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
     [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),
    ([[1]],
     [[1]]),
    ([[1, 2], [3, 4]],
     [[3, 1], [4, 2]]),
]


def are_lists_equal(list1, list2):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if len(list1[i]) != len(list2[i]):
            return False
        if any(l1 != l2 for l1, l2 in zip(list1[i], list2[i])):
            return False
    return True


for i, o in tests:
    s.rotate(i)
    print(are_lists_equal(i, o))

# print(s.rotate([
#     [2, 29, 20, 26, 16, 28],
#     [12, 27, 9, 25, 13, 21],
#     [32, 33, 32, 2, 28, 14],
#     [13, 14, 32, 27, 22, 26],
#     [33, 1, 20, 7, 21, 7],
#     [4, 24, 1, 6, 32, 34]]))
#
# [[ 4, 33, 13, 32, 12,  2],
#  [24,  1, 14, 33, 27, 29],
#  [ 1, 20, 32, 32,  9, 20],
#  [ 6,  7, 27,  2, 26, 26],
#  [32, 21, 26, 28, 13, 16],
#  [34,  7, 26, 14, 21, 28]]
