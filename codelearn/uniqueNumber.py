def uniqueNumber(arr):
    """https://codelearn.io/training/detail/26770"""
    s = 0
    for n in arr:
        s ^= n
    return s
