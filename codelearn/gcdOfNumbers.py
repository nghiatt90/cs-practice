gcd = lambda a, b: a if b == 0 else gcd(b, a%b)

def gcdOfNumbers(a):
    """https://codelearn.io/training/detail/33265"""
    for i in range(len(a)):
        a[0] = gcd(a[0], a[i])
    return a[0]
