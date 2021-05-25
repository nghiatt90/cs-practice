# https://codelearn.io/training/detail/4535
def fibonacciIndex(n):
    if n == 1:
        return 0
    f0 = 0
    f1 = 1
    target = 10**(n-1)
    i = 1
    while f1 < target:
        i += 1
        f0, f1 = f1, f0+f1
    return i
