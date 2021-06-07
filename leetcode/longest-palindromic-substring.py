# https://leetcode.com/problems/longest-palindromic-substring
DEBUG = False


def debug(*message, **kwargs):
    if DEBUG:
        print(*message, **kwargs)


class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.solve(s)
    
    def solve(self, s: str, *args, **kwargs) -> str:
        max_len = 1
        ans = 1
        
        s = '#' + '#'.join(list(s)) + '#'
        L = len(s)
        lps = [0] * L
        debug(f's={s}')
        
        center, r = 0, 0
        for i, c in enumerate(s):
            debug(f'i={i:2d}')
            mirror = center - (i-center)
            lps[i] = min(lps[mirror], r-i) if r > i else 0
            
            while 0 <= i-lps[i]-1 and i+lps[i]+1 < L and s[i+lps[i]+1] == s[i-lps[i]-1]:
                lps[i] += 1
            
            if i + lps[i] > r:
                center = i
                r = i + lps[i]
            
            if lps[i] > max_len:
                max_len = lps[i]
                ans = center
            debug(f'  s={s}')
            debug(f'lps={"".join(str(x) for x in lps)}')
        
        debug(f'center={ans}')
        debug(f'max_len={max_len}')
        return s[ans-max_len: ans+1+max_len].replace('#', '')
