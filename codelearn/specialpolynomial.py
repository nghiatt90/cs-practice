# https://codelearn.io/training/detail/10697
def specialPolynomial(x, n):
    if x == 1:
        return n - 1
    s = 0
    for k in range(32):
        s += x**k
        if s > n:
            break
    return k - 1
