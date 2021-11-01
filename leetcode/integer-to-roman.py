# https://leetcode.com/problems/integer-to-roman/

class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        letters = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        ans = []
        for i in range(len(values)):
            while num >= values[i]:
                num -= values[i]
                ans.append(letters[i])
        return ''.join(ans)
