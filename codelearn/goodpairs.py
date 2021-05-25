# https://codelearn.io/training/detail/131335
def goodPairs(n, m, c):
    cnt = 0
    sqrt = int(c**.5)
    for i in range(1, min(sqrt+1, n+1)):
        if c % i != 0:
            continue
        j = c // i
        if j <= m:
            cnt += 1
        if j <= n and i <= m:
            cnt += 1
    if sqrt * sqrt == c and sqrt <= m and sqrt <= n:
        cnt -= 1
    return cnt
