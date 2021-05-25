# https://codelearn.io/training/detail/40522
def equalPairOfBits(n, m):
    x = n ^ m
    ans = 1
    while x & ans:
        ans <<= 1
    return ans
        
