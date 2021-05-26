# https://www.interviewbit.com/problems/min-steps-in-infinite-grid/

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        assert len(A) == len(B)
        if not A: return 0
        
        ans = 0
        for i in range(1, len(A)):
            ans += max(abs(A[i] - A[i-1]), abs(B[i] - B[i-1]))
        return ans
