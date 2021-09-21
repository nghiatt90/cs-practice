# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs.sort()
        if not strs or not strs[0]:
            return ''
        
        ans = []
        i = 0
        for i in range(len(strs[-1])):
            c = strs[-1][i]
            if len(strs[0]) <= i or strs[0][i] != c:
                break
            ans.append(c)
        
        return ''.join(ans)
