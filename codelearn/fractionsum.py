# https://codelearn.io/training/detail/34661
def fractionSum(a, b):
    gcd = lambda a, b: a if b == 0 else gcd(b, a%b)
    g = gcd(a, b)
    return a // g + b // g
