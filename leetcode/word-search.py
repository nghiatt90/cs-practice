#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.word-search
# Date: 2021/11/01
# Filename: word-search

__author__ = "Yoshi Truong"
__date__ = "2021/11/01"

from typing import List


def dfs(board, r, c, word, wid, used=None):
    if wid == len(word) - 1 and board[r][c] == word[wid]:
        return True
    if board[r][c] != word[wid]:
        return False
    if used is None:
        used = [[False] * len(board[0]) for _ in range(len(board))]
    used[r][c] = True
    for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        if 0 <= r + i < len(board) and 0 <= c + j < len(board[0]) and not used[r + i][c + j]:
            if dfs(board, r + i, c + j, word, wid + 1, used):
                return True
    used[r][c] = False
    return False


class Solution:
    """https://leetcode.com/problems/word-search/"""

    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word:
            return True
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if dfs(board, i, j, word, 0):
                    return True
        return False
