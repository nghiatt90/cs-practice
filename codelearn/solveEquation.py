# https://codelearn.io/training/detail/188615
def solveEquation(n):
    k = int(n**.5) if n > 10000 else 0
    for i in range(max(0, k-5000), k+10000):
        t = i
        s = 0
        while t:
            s += t%10
            t //= 10
        if i**2 + s*i == n:
            return i
    return -1
