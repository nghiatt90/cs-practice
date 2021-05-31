# https://www.interviewbit.com/problems/city-tour/

import operator as op
from functools import reduce

def ncr(n, r):
    """n choose r"""
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer // denom


MOD = int(1e9) + 7

class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):
        B = set(B)
        total = A - len(B)
        s = []
        x = set()
        for i in range(1, A+1):
            if i in B:
                if len(x):
                    s.append(x)
                x = set()
            else:
                x.add(i)
        if x:
            s.append(x)
        
        print(s)
        ans = 1
        for l in s:
            if 1 in l or A in l:
                ans *= ncr(total, len(l))
            else:
                ans *= 2**(len(l)-1) * ncr(total, len(l))
            total -= len(l)
        return ans % MOD
