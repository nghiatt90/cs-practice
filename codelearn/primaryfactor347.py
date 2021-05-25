# https://codelearn.io/training/detail/54564
def primaryFactor347(n):
    if n == 1: return False
    for i in (3, 4, 7):
        while n % i == 0:
            n //= i
    return n == 1
