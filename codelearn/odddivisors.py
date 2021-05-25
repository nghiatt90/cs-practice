# https://codelearn.io/training/detail/28021
def oddDivisors(a, b):
    return sum(1 for i in range(1, 100001) if a<=i*i<=b)

