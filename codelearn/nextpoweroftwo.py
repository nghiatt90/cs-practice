# https://codelearn.io/training/detail/25654
def nextPowerOfTwo(n):
    s = bin(n)
    if s.count('1') == 1:
        return n
    return int('1' + ('0'*(len(s)-2)), 2)
