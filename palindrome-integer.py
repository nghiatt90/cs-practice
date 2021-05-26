# https://www.interviewbit.com/problems/palindrome-integer/

class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        if A < 0: return 0
        if A == 0: return 1
        
        rev = 0
        a = A
        while a:
            rev = rev * 10 + (a % 10)
            a //= 10
        return int(rev == A)
