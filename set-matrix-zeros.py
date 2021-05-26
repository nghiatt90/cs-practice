# https://www.interviewbit.com/problems/set-matrix-zeros

class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def setZeroes(self, A):
        if not A: return A
        
        r, c = len(A), len(A[0])
        row_set, col_set = set(), set()
        for i in range(r):
            for j in range(c):
                if A[i][j] == 0:
                    row_set.add(i)
                    col_set.add(j)
                    
        for i in range(r):
            for j in range(c):
                if i in row_set or j in col_set:
                    A[i][j] = 0
        return A
