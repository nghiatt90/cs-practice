# https://leetcode.com/problems/palindrome-number/

class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0: return False
        if x < 10: return True
        
        rev = 0
        t = x
        while x > 0:
            r = x % 10
            x //= 10
            rev = rev * 10 + r
        
        return rev == t
