# https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        letters = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        ans = 0
        for i in range(len(values)):
            while s.startswith(letters[i]):
                ans += values[i]
                s = s[len(letters[i]):]
        
        return ans
