# https://codelearn.io/training/detail/9202
def setOddBits(n):
    x = 1
    while x < n:
        n |= x
        x <<= 2
    return n
