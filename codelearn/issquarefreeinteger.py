# https://codelearn.io/training/detail/9856
def isSquareFreeInteger(n):
    r = int(n ** .5)
    sieve = [True] * (r+1)
    sieve[0] = sieve[1] = False
    for i in range(2, r+1):
        if not sieve[i]:
            continue
        ii = i*2
        while ii <= r:
            sieve[ii] = False
            ii += i
    primes = [i for i in range(r+1) if sieve[i]]
    
    return all(n % (p*p) > 0 for p in primes)
