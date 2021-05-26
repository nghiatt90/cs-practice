# https://app.codesignal.com/challenge/RLhyzdapSvfRXCHHd
f, t = eval(dir()[0])
l = 1
x = len(f)
for d in -1, 1:
    P = f[0] + d
    for i in range(1, x):
        d *= -1
        p = f[i] + d
        if abs(p - P) > t:
            break
        l = max(l, i + 1)
        P = p
    else:
        return -1
return l

