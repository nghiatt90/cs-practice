# https://www.interviewbit.com/problems/wave-array/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def wave(self, A):
        A.sort()
        if len(A) < 2: return A
        
        for i in range(1, len(A), 2):
            A[i], A[i-1] = A[i-1], A[i]
        
        return A
