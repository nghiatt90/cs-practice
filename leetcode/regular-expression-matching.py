# https://leetcode.com/problems/regular-expression-matching/

class Solution:
    def splitPattern(self, p):
        assert p[0] != '*'
        
        P = []
        for c in p:
            if c != '*':
                P.append(c)
            else:
                P[-1] += c
        return P
    
    def matchSinglePattern(self, s, p):
        assert len(p) <= 2
        
        if p == '.*':
            return True
        
        if self.isStarPattern(p):
            return all(c == p[0] for c in s)
        else:
            return s == p or p == '.' and len(s) == 1
    
    def isStarPattern(self, p):
        return len(p) == 2
        
    
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            return not s
        
        p = self.splitPattern(p)
#         print(p)
        n, m = len(s), len(p)
        s += '.'
        
        dp = [[False] * (m+1) for _ in range(n+1)]
        dp[n][m] = True
        for j in range(m-1, -1, -1):
            if not self.isStarPattern(p[j]): break
            dp[n][j] = True
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if self.isStarPattern(p[j]):
                    dp[i][j] = (
                        dp[i][j+1]
                        or (self.matchSinglePattern(s[i], p[j]) and (dp[i+1][j+1] or dp[i+1][j]))
                    )
                else:
                    dp[i][j] = dp[i+1][j+1] and self.matchSinglePattern(s[i], p[j])
        
#         for row in dp: print(row)
        
        return dp[0][0]
