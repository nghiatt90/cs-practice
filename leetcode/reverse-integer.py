# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        
        sign = 1 if x >= 0 else -1
        x = abs(x)
        ans = 0
        while x > 0:
            r = x % 10
            x //= 10
            ans = ans * 10 + r
        
        if ans >= (1 << 31):
            return 0
        
        return ans * sign
