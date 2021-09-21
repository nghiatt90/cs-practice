# https://leetcode.com/problems/generate-parentheses/

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.ans = []
        self.rec(n*2)
        return self.ans

    def rec(self, remain, current_level=0, current_string=''):
        if remain == current_level:
            self.ans.append(current_string + (')' * remain))
            return
        if current_level > 0:
            self.rec(remain-1, current_level-1, current_string+')')
        self.rec(remain-1, current_level+1, current_string+'(')


