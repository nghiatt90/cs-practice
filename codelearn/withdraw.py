# https://codelearn.io/training/detail/29239
def withdraw(n):
    a = b = c = 0
    n //= 10
    if n % 2 == 1:
        b = 1
        n -= 5
    a = n // 10
    c = n % 10 // 2
    return [a, b, c]
