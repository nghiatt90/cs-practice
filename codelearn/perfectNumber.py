# https://codelearn.io/training/detail/119644
def perfectNumber(k):
    x = 10
    while k:
        s = 0
        t = x
        while t:
            s += t % 10
            t //= 10
        if s == 10:
            k -= 1
        x += 9
    return x - 9
