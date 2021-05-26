# https://www.interviewbit.com/problems/prime-sum/

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    return all(n % i != 0 for i in range(3, int(n**0.5)+1, 2))

class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        if A == 4:
            return [2, 2]
        for i in range(3, A, 2):
            if is_prime(i) and is_prime(A-i):
                return [i, A-i]
        return None, None
