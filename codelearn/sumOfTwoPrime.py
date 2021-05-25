# https://codelearn.io/training/detail/9004
def sumOfTwoPrime(r):
    if r < 2:
        return []
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
    prime_set = set(primes)

    for p in primes:
        if p > r // 2:
            break
        if r - p in prime_set:
            return [p, r-p]
    return []
