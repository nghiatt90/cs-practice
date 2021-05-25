# https://codelearn.io/training/detail/46202
def sumOfTwoPowers(n, k):
    upperbound = int(n ** (1/k)) + 1
    results = []
    EPS = 1e-9
    for a in range(upperbound):
        b_pow = (n - a**k)
        b = int(b_pow ** (1/k) + EPS)
        if b < a: break
        if b ** k == b_pow:
            results.append([a**k, b_pow])
    return results
