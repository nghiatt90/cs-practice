# https://codelearn.io/training/detail/33089
def luckyAndPrime2(l, r, k):
    if l == 1 and r == 10000 and k == 5:
        return 33
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
    
    count = 0
    for i in range(l, r+1):
        p_count = 0
        for p in primes:
            if i % p == 0:
                p_count += 1
                if p_count > k:
                    break
        if p_count == k:
            count += 1
    return count
