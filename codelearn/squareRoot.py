# https://codelearn.io/training/detail/7410
def squareRoot(n, m):
    a = str(n ** .5)
    i = a.find('.')
    return a[:i+m+1]

