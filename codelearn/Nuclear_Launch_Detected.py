# https://codelearn.io/training/detail/89353
import math

def maxKill(x, y, r):
    p = [list(i) for i in zip(x,y)]
    if not p:
       return 0
    ans = 1
    n = len(p)
    for i in range(n):
        for j in range(i):
            (x1, y1), (x2, y2) = p[i], p[j]
            m,n = x2-x1, y2-y1
            d = math.hypot(m, n)
            if d > 2 * r : continue
            k = math.sqrt(r ** 2 - d ** 2 / 4)
            m,n = m / math.hypot(m,n) , n / math.hypot(m,n)
            x,y = (x1 + x2) / 2, (y1 + y2) / 2
            for P,Q in (-n, m), (n, -m):
                a,b = x + P * k, y + Q * k
                ans = max(ans, sum(math.hypot(X - a, Y-b) <= r for X,Y in p))

    return ans
