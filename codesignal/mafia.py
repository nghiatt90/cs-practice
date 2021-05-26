# https://app.codesignal.com/challenge/9MGJonqLaLGREtAnW
def Mafia(a):
    f = {i:0 for i in range(100)}
    for _ in a:
        for i in _:
            f[i] += 1
    
    s = sorted(f.items(), key=lambda x: x[1], reverse=True)
    p = [0 for _ in range(100)]
    for i in range(10):
        p[s[i][0]] = 1
    for i in s:
        p[i[0]] = 0 if functools.reduce(lambda x, y: x + p[y], a[i[0]], 0) >= 4 else 1
    for i in s:
        p[i[0]] = 0 if functools.reduce(lambda x, y: x + p[y], a[i[0]], 0) >= 4 else 1
    r = sorted([i for i in range(100) if p[i] == 1])
    return r


