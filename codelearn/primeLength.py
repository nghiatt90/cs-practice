# https://codelearn.io/training/detail/31402
import math

def primeLength(n):
    if n < 3:
        return 0
    sieve = [1] * n
    ans = 1
    for i in range(3, n, 2):
        if sieve[i] == 0: continue
        ans += int(math.log(i, 10)) + 1
        for j in range(i+i, n, i):
            sieve[j] = 0
    return ans
