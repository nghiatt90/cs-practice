# https://codelearn.io/training/detail/33112
def primeSquare(n):
    is_prime = lambda x: all(x%i for i in range(2, int(x**.5)+1))
    if is_prime(n):
        return n**2
    
    s = 1
    for i in range(2, n+1):
        s += i**2 if is_prime(i) else i
    return s

