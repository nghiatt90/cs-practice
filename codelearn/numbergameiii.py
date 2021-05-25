# https://codelearn.io/training/detail/35158
def numberGameIII(s):
    if not s:
        return -1
    gcd = lambda a, b: a if b == 0 else gcd(b,a%b)
    g = s[0]
    for n in s:
        g = gcd(g, n)
    return g if g in s else -1
