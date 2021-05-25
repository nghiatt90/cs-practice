# https://codelearn.io/training/detail/40940
def removeDigits(n, k):
    min_ = n
    max_ = 0
    n = str(n)
    for i in range(len(n)-k+1):
        sub = n[i:i+k]
        min_ = min(min_, int(sub))
        max_ = max(max_, int(sub))
    return [min_, max_]
