# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s

        ans = [[] for _ in range(numRows)]
        group_len = 2 * numRows - 2
        for i, c in enumerate(s):
            k = i % group_len
            if k < numRows:
                ans[k].append(c)
            else:
                ans[-2-(k-numRows)].append(c)
        
        return ''.join([''.join(x) for x in ans])
