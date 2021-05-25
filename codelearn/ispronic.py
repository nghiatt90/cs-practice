# https://codelearn.io/training/detail/33115
def isPronic(n):
    base = int(n ** .5)
    return base * (base + 1) == n
