#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.palindromic-substrings
# Date: 2021/11/04
# Filename: palindromic-substrings

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"


def manacher(s):
    # Transform S into T.
    # For example, S = "abba", T = "^#a#b#b#a#$".
    # ^ and $ signs are sentinels appended to each end to avoid bounds checking
    T = '#'.join('^{}$'.format(s))
    n = len(T)
    P = [0] * n
    C = R = 0
    for i in range(1, n - 1):
        P[i] = int((R > i) and min(R - i, P[2 * C - i]))  # equals to i' = C - (i-C)
        # Attempt to expand palindrome centered at i
        while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
            P[i] += 1

        # If palindrome centered at i expand past R,
        # adjust center based on expanded palindrome.
        if i + P[i] > R:
            C, R = i, i + P[i]

    return P


class Solution:
    """https://leetcode.com/problems/palindromic-substrings/"""

    def countSubstrings(self, s: str) -> int:
        T = '|' + '|'.join('{}'.format(s)) + '|'
        P = manacher(T)
        return sum((n + (i % 4 == 0)) // 4 for i, n in enumerate(P))


assert Solution().countSubstrings('aaabb') == 9
