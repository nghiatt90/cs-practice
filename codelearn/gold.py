# https://codelearn.io/training/detail/43252
def gold(r):
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
    pset = set(primes)
    
    cnt = 0
    for p in primes:
        if p > r//2:
            break
        if r-p in pset:
            cnt += 1
    return cnt
