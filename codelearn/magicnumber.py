# https://codelearn.io/training/detail/35324
def magicNumber(n):
    a = [3**i for i in range(20)]
    b = [5**i for i in range(20)]
    c = [7**i for i in range(20)]
    t = []
    for x in a:
        for y in b:
            for z in c:
                t.append(x*y*z)
    return sorted(t)[n-1]
