# https://www.interviewbit.com/problems/largest-number/

class K:
    def __init__(self, obj, *args):
        self.obj = obj
    def __lt__(self, other):
        return '%d%d'%(self.obj,other.obj) < '%d%d'%(other.obj,self.obj)

class Solution:
    # @param A : tuple of integers
    # @return a strings
    def largestNumber(self, A):
        A = sorted(A, key=K, reverse=True)
        return str(int(''.join([str(s) for s in A])))
