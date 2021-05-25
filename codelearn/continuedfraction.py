# https://codelearn.io/training/detail/31410
def continuedFraction(a):
    n = 1
    d = a.pop()
    while a:
        n = a.pop() * d + n
        n, d = d, n
    
    def gcd(a, b):
        return a if b == 0 else gcd(b, a % b)
    g = gcd(n, d)
    return n // g * d // g
