# https://www.interviewbit.com/problems/rearrange-array/

class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        for i in range(len(A)):
            A[i] <<= 16
        for i in range(len(A)):
            A[i] |= A[A[i] >> 16] >> 16
        for i in range(len(A)):
            A[i] &= 65535
