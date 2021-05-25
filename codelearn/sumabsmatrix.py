# https://codelearn.io/training/detail/98088
def sumAbsMatrix(n):
    s = 0
    for i in range(n):
        s += i*(n-i)
    return s*2
