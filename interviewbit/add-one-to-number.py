# https://www.interviewbit.com/problems/add-one-to-number/
class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, n):
        for i in range(len(n)-1, -1, -1):
            if n[i] == 9:
                n[i] = 0
            else:
                n[i] += 1
                break
        else:
            n = [1] + n
        for i, v in enumerate(n):
            if v > 0:
                return n[i:]
