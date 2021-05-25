# https://codelearn.io/training/detail/46465
def iterMask(n):
    res = []
    for i in range(1 << 18, -1, -1):
        if n & i == i:
            res.append(i)
    return res
