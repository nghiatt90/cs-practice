# https://codelearn.io/training/detail/33052
def moreTimesLess(n):
    if n == 1:
        return 0
    upperbound = int(n ** .5) + 1
    results = 0
    for a in range(1, upperbound):
        if n % a == 0 and a % 2 == (n // a) % 2:
            results += 1
    return results
