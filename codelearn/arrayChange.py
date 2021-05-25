def arrayChange(a):
    """https://codelearn.io/training/detail/3880"""
    s = 0
    for i in range(1, len(a)):
        t = max(0, a[i-1] - a[i] + 1)
        s += t
        a[i] += t
    return s
