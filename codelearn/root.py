# https://codelearn.io/training/detail/144455
def root(n):
    if n < 10: return n
    s = 0
    while n:
        s += n%10
        n //=10
    return root(s)
