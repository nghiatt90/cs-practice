# https://codelearn.io/training/detail/29067
def firstMultiple(divisors, start):
    gcd = lambda a, b: a if b == 0 else gcd(b, a%b)
    lcm = lambda a, b: a * b // gcd(a, b)
    l = divisors[0]
    for n in divisors:
        l = lcm(l, n)
    return ((start-1)//l + 1)*l
