# https://codelearn.io/training/detail/5477
def makeTriangle(a, b, c):
    i = 0
    while True:
        a, b, c = sorted([a, b, c])
        if a + b > c:
#             print(a, b, c)
            return i
        i += 1
        a += 1
