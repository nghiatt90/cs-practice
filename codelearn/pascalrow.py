# https://codelearn.io/training/detail/40628
def pascalRow(n):
    a = []
    a.append([1])
    a.append([1, 1])
    for i in range(2, n+1):
        b = [1]
        for j in range(1, len(a[-1])):
            b.append(a[-1][j] + a[-1][j-1])
        b.append(1)
        a.append(b)
    return a[n]
