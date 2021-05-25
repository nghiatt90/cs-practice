# https://codelearn.io/training/detail/31474
def candies(n):
    sieve = [1] * n
    sieve[0] = sieve[1] = 0
    primes = set([2])
    for i in range(3, n, 2):
        if sieve[i]:
            for j in range(i*2, n, i):
                sieve[j] = 0
            primes.add(i)
    return any(n-p in primes for p in primes)
