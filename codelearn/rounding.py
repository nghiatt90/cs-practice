# https://codelearn.io/training/detail/35202
def rounding(n, m):
    k = n / m - n // m
    return n if k == .5 else n//m*m if k < .5 else (n//m+1)*m
