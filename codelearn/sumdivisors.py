# https://codelearn.io/training/detail/30445
def _try_composite(a, d, n, s):
    if pow(a, d, n) == 1:
        return False
    for i in range(s):
        if pow(a, 2**i * d, n) == n-1:
            return False
    return True

def miller_rabin(n,
                 _known_primes=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],
                 _precision_for_huge_n=16):
    if n < 2:
        return False
    if n in _known_primes:
        return True
    if any((n % p) == 0 for p in _known_primes):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001: 
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467: 
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    return not any(_try_composite(a, d, n, s) 
                   for a in _known_primes[:_precision_for_huge_n])

def sumDivisors(n):    
    s = 0
    t = int(n**.5)
    for i in range(1, t+1):
        if n % i:
            continue
        if not miller_rabin(i):
            s += i
        if not miller_rabin(n//i) and n//i != i:
            s += n//i
    return s
