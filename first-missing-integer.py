# https://www.interviewbit.com/problems/first-missing-integer/

class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        pos_count = 0
        l = len(A)
        for i in range(l):
            if A[i] > 0:
                A[i], A[pos_count] = A[pos_count], A[i]
                pos_count += 1
        for i in range(pos_count):
            n = abs(A[i])
            if n-1 < l:
                A[n-1] = -abs(A[n-1])
        for i in range(pos_count):
            if A[i] > 0:
                return i+1
        return pos_count+1
