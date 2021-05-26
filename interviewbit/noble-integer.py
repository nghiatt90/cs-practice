# https://www.interviewbit.com/problems/noble-integer/

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        A.sort(reverse=True)
        if A[0] == 0: return 1
        
        for i, p in enumerate(A):
            if i == 0 or p == A[i-1]: continue
            if p == i:
                return 1
        return -1
