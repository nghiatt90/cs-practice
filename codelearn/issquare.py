# https://codelearn.io/training/detail/33938
def isSquare(x, y):
    d = []
    for i in range(4):
        for j in range(i+1, 4):
            d.append((x[i]-x[j])**2 + (y[i]-y[j])**2)
    d.sort()
    return d[0] == d[1] == d[2] == d[3] != d[4] == d[5]

