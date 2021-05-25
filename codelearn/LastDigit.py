# https://codelearn.io/training/detail/8956
def lastDigit(a, b):
    if b == 0:
        return 1
    c = [
        [0],
        [1],
        [2, 4, 8, 6],
        [3, 9, 7, 1],
        [4, 6],
        [5],
        [6],
        [7, 9, 3, 1],
        [8, 4, 2, 6],
        [9, 1]
    ]
    return c[a%10][(b-1)%len(c[a%10])]
