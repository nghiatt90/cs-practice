def coprimeSum(n):
    """https://codelearn.io/training/detail/32273"""
    gcd = lambda a, b: gcd(b, a%b) if b else a
    s = 0
    for i in range(n+1):
        s += i if gcd(i, n) == 1 else 0
    return s
