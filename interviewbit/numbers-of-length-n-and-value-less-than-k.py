# https://www.interviewbit.com/problems/numbers-of-length-n-and-value-less-than-k/

def solve(digits, b, c, use_zero=True):    
    if b == 0: return 0
    ans = 0
    upper = c // (10**(b-1))
    for d in digits:
        if not use_zero and d == 0:
            continue
        if d < upper:
            ans += len(digits)**(b-1)
        elif d == upper:
            ans += solve(digits, b-1, c%(10**(b-1)))
    return ans
    

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        return solve(A, B, C, B == 1)
