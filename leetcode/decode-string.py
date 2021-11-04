#!/usr/bin/env python
# -*- coding: utf-8 -*-

# cs-practice.decode-string
# Date: 2021/11/04
# Filename: decode-string

__author__ = "Yoshi Truong"
__date__ = "2021/11/04"


class Solution:
    """https://leetcode.com/problems/decode-string/"""

    def decodeString(self, s: str) -> str:
        stack = []
        # ans = ''
        current_word = ''
        for char in s:
            if char == '[':
                stack.append(int(current_word))
                current_word = ''
            elif char == ']':
                rep = current_word * stack.pop()  # Top of stack must be a number
                current_word = stack.pop() if stack and isinstance(stack[-1], str) else ''
                current_word += rep
            elif current_word and current_word[-1].isdigit() and char.isalpha():
                raise ValueError('Incorrect input')
            elif current_word and current_word[-1].isalpha() and char.isdigit():
                stack.append(current_word)
                current_word = char
            else:
                current_word += char
        return current_word


# assert Solution().decodeString("3[a]2[bc]") == "aaabcbc"
assert Solution().decodeString(
    "3[z]2[2[y]pq4[2[jk]e1[f]]]ef") == "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"
