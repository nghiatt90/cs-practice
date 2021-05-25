# https://codelearn.io/training/detail/33059
def nearSquare(n):
    s = int(n**.5)
    for i in range(s, 0, -1):
        if n % i == 0:
            return [i, n // i]

