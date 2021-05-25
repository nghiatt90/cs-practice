# https://codelearn.io/training/detail/28015
def sumOfThrees(n):
    p = [3**i for i in range(40)]
    n = int(n)
    r = []
    for i in range(39, -1, -1):
        if n >= p[i]:
            n -= p[i]
            r.append(i)
    if n == 0:
        return '+'.join('3^%d' % i for i in r)
    return 'Impossible'

