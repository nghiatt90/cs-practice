# https://codelearn.io/training/detail/3418
def pagesNumbering(n):
    s = 0
    for i in range(1, 10):
        if n >= 10 ** i:
            s += (9 * 10**(i-1)) * i
        else:
            s += (n - 10**(i-1) + 1) * i
            break
    return s
