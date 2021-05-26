# https://www.interviewbit.com/problems/excel-column-number/

class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        l = len(ALPHABET)
        mapping = dict(zip(ALPHABET, range(1, l+1)))
        ans = 0
        for c in A:
            ans = ans * l + mapping[c]
        return ans
