# https://codelearn.io/training/detail/7069
def secondBiggest(n, a):
    a = sorted(set(a))
    return a[-1] if len(a) == 1 else a[-2]
