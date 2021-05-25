# https://codelearn.io/training/detail/22564
def candles(a, b):
    s = 0
    r = 0
    while a:
        s += a
        r += a
        a = r // b
        r %= b
    return s
