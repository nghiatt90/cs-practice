# https://leetcode.com/problems/valid-parentheses
BRACKETS = {
    ')': '(',
    ']': '[',
    '}': '{'
}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in BRACKETS.values():
                stack.append(c)
            elif not stack or stack.pop() != BRACKETS[c]:
                return False
        return len(stack) == 0
