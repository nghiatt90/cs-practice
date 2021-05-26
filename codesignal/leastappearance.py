# https://app.codesignal.com/challenge/vvaEwn4NbpLYGMt5G
s, *c = eval(dir()[0])
f = [0] * 111
r = []
for a, b in s:
    r.append(a if f[a] < f[b] else b if f[b] < f[a] else min(a, b))
    f[r[-1]] += 1
return r
        

